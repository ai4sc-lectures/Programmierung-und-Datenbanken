#!/usr/bin/env python3
"""
Incrementally translate Jupyter notebooks (German -> English), updating only changed cells.

Now also translates:
- Markdown + Raw cells (full text).
- Code cells: variable names, function/class names, comments, and docstrings,
  preserving valid Python code.

Mechanics:
- Uses cell IDs + src_hash in metadata to detect changes.
- Only re-translates cells that changed.
- Stores translation info in metadata.translation and marks with tag.
"""

import argparse
import hashlib
import os
import sys
import uuid
import time
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

import nbformat
from nbformat import NotebookNode
from tqdm import tqdm
from openai import OpenAI

MODEL_DEFAULT = "gpt-5-nano"
TEMPERATURE = 0.2
MAX_RETRIES = 5
RETRY_BACKOFF_SECONDS = 2.0

TRANSLATION_TAG_DEFAULT = "translated_en"
TRANSLATION_META_KEY = "translation"

PROMPT_MD = (
    "You are a precise, conservative translator. "
    "Translate the user's content from German to natural, idiomatic English. "
    "Preserve Markdown structure, headings, lists, code fences, inline code, math, "
    "LaTeX blocks, and links. Do not add explanations."
)

PROMPT_CODE = (
    "You are a precise translator. Translate only the variable names, function/class names, "
    "docstrings, and inline comments in the following Python code from German to natural English. "
    "Do not change the program logic. Do not explain. Output valid Python code."
)

def ensure_cell_ids(nb: NotebookNode) -> None:
    """Ensure every cell has a unique 'id' field (nbformat v4.5+)."""
    for cell in nb.cells:
        if "id" not in cell:
            cell["id"] = uuid.uuid4().hex

def ensure_cell_ids(nb: NotebookNode) -> bool:
    """Ensure every cell has an 'id'. Returns True if any were added."""
    changed = False
    for cell in nb.cells:
        if "id" not in cell:
            cell["id"] = uuid.uuid4().hex
            changed = True
    return changed

def mirror_ids_if_missing(src_nb: NotebookNode, tgt_nb: NotebookNode) -> int:
    """
    If target cells lack IDs, mirror IDs from source by position.
    Returns how many IDs were mirrored.
    """
    mirrored = 0
    n = min(len(src_nb.cells), len(tgt_nb.cells))
    for i in range(n):
        if "id" not in tgt_nb.cells[i]:
            tgt_nb.cells[i]["id"] = src_nb.cells[i]["id"]
            mirrored += 1
    return mirrored

def translate_text(client: Optional[OpenAI], text: str, model: str, prompt: str) -> str:
    if not text.strip() or client is None:
        return text
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.responses.create(
                model=model,
                instructions=prompt,
                input=text,
            )
            return resp.output_text
        except Exception:
            if attempt == MAX_RETRIES:
                raise
            time.sleep(RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1)))


def target_path_for(source_path: Path) -> Path:
    return source_path.with_name(source_path.stem + "_en" + source_path.suffix)


def find_ipynb_files(root: Path) -> List[Path]:
    return sorted(p for p in root.glob("*.ipynb") if not p.name.endswith("_en.ipynb"))


def sync_structure_by_ids(src_nb: NotebookNode, tgt_nb: NotebookNode, prune_deleted: bool) -> None:
    src_ids = [c["id"] for c in src_nb.cells]
    tgt_map = {c.get("id"): c for c in tgt_nb.cells if "id" in c}

    new_cells: List[NotebookNode] = []
    seen = set()

    for src_cell in src_nb.cells:
        cid = src_cell["id"]
        if cid in tgt_map:
            new_cells.append(tgt_map[cid])
            seen.add(cid)
        else:
            # Create fresh copy if missing
            if src_cell.cell_type == "markdown":
                new_cell = nbformat.v4.new_markdown_cell(src_cell.source)
            elif src_cell.cell_type == "raw":
                new_cell = nbformat.v4.new_raw_cell(src_cell.source)
            else:
                new_cell = nbformat.v4.new_code_cell(
                    source=src_cell.source,
                    outputs=src_cell.get("outputs", []),
                    execution_count=src_cell.get("execution_count"),
                )
            new_cell.metadata = src_cell.get("metadata", {})
            new_cell["id"] = cid
            new_cells.append(new_cell)
            seen.add(cid)

    if not prune_deleted:
        for cell in tgt_nb.cells:
            cid = cell.get("id")
            if cid and cid not in seen:
                new_cells.append(cell)

    tgt_nb.cells = new_cells


def translate_untagged_or_changed_cells(
    client: Optional[OpenAI],
    src_nb: NotebookNode,
    tgt_nb: NotebookNode,
    model: str,
    tag_translated: str,
    dry_run: bool,
) -> int:
    translated = 0
    tgt_map = {c.get("id"): c for c in tgt_nb.cells if "id" in c}

    for src_cell in src_nb.cells:
        cid = src_cell["id"]
        tgt_cell = tgt_map.get(cid)
        if not tgt_cell:
            continue

        src_text = src_cell.source or ""
        src_hash = hashlib.sha256(src_text.encode("utf-8")).hexdigest()

        md = tgt_cell.setdefault("metadata", {})
        meta = md.setdefault(TRANSLATION_META_KEY, {})
        prev_hash = meta.get("src_hash")
        tags = md.setdefault("tags", [])

        needs_translation = prev_hash != src_hash or tag_translated not in tags
        if not needs_translation:
            continue

        if dry_run:
            translated += 1
            continue

        if src_cell.cell_type == "markdown":
            en_text = translate_text(client, src_text, model, PROMPT_MD)
        elif src_cell.cell_type == "raw":
            en_text = translate_text(client, src_text, model, PROMPT_MD)
        elif src_cell.cell_type == "code":
            en_text = translate_text(client, src_text, model, PROMPT_CODE)
        else:
            continue

        tgt_cell.source = en_text
        if tag_translated not in tags:
            tags.append(tag_translated)
        meta["src_hash"] = src_hash
        meta["lang"] = "de"
        meta["updated_at_iso"] = datetime.now(timezone.utc).isoformat()
        translated += 1

    return translated


def process_notebook(
    client: Optional[OpenAI],
    src: Path,
    model: str,
    tag_translated: str,
    prune_deleted: bool,
    dry_run: bool,
) -> None:
    tgt = target_path_for(src)
    src_nb = nbformat.read(src, as_version=4)
    ensure_cell_ids(src_nb)

    if not tgt.exists():
        if dry_run:
            print(f"[DRY-RUN] Would copy {src} -> {tgt}")
        else:
            tgt.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, tgt)

    tgt_nb = nbformat.read(tgt if tgt.exists() else src, as_version=4)
    ensure_cell_ids(tgt_nb)

    sync_structure_by_ids(src_nb, tgt_nb, prune_deleted=prune_deleted)
    changed = translate_untagged_or_changed_cells(client, src_nb, tgt_nb, model, tag_translated, dry_run)

    if dry_run:
        print(f"[DRY-RUN] {src.name} -> {tgt.name}: would translate {changed} cell(s)")
    elif changed > 0 or not tgt.exists():
        nbformat.write(tgt_nb, tgt)


def main():
    parser = argparse.ArgumentParser(description="Incrementally translate .ipynb (DE->EN), including code cells.")
    parser.add_argument("folder", type=str, help="Folder to scan for .ipynb files")
    parser.add_argument("--model", type=str, default=MODEL_DEFAULT)
    parser.add_argument("--tag", type=str, default=TRANSLATION_TAG_DEFAULT)
    parser.add_argument("--prune-deleted", action="store_true", help="Remove target cells no longer in source")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing/translating")
    args = parser.parse_args()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.is_dir():
        print(f"Error: {folder} is not a directory", file=sys.stderr)
        sys.exit(1)

    if not args.dry_run and not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    client = None if args.dry_run else OpenAI()

    files = find_ipynb_files(folder)
    if not files:
        print("No .ipynb files found.")
        return

    for src in tqdm(files, desc="Processing notebooks"):
        try:
            process_notebook(client, src, args.model, args.tag, args.prune_deleted, args.dry_run)
        except Exception as e:
            print(f"Failed to process {src}: {e}", file=sys.stderr)

    print("Done.")


if __name__ == "__main__":
    main()