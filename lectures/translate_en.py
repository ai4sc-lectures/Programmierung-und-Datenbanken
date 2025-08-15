#!/usr/bin/env python3
"""
Translate Jupyter notebooks (German -> English) cell-by-cell.

- Scans a directory for .ipynb files.
- For each notebook, writes a sibling file with "_en" suffix.
- Only processes a notebook if the source is newer than the target (mtime).
- Translates Markdown and Raw cells; leaves Code cells (and outputs) unchanged.

Usage:
  python translate_notebooks_de_to_en.py /path/to/folder \
      --model gpt-4o-mini \
      --dry-run  # optional
Requires:
  pip install openai nbformat tqdm
Environment:
  OPENAI_API_KEY must be set.
"""

import argparse
import os
import sys
import time
from pathlib import Path
from typing import List

import nbformat
from nbformat import NotebookNode
from tqdm import tqdm

from openai import OpenAI


TRANSLATION_SYSTEM_PROMPT = (
    "You are a precise, conservative translator. "
    "Translate the user's content from German to natural, idiomatic English. "
    "Preserve Markdown structure, headings, lists, code fences, inline code, math, "
    "LaTeX blocks, and links. Do not add explanations. If the text is already "
    "English or code-only, return it unchanged."
)

# You can tune these if needed
MODEL_DEFAULT = "gpt-5-nano"
TEMPERATURE = 0.2
MAX_RETRIES = 5
RETRY_BACKOFF_SECONDS = 2.0


def translate_text(client: OpenAI, text: str, model: str) -> str:
    """Translate a single cell's text using the OpenAI API."""
    if not text.strip():
        return text

    # Responses API (supported path in current SDK)
    # https://github.com/openai/openai-python / https://platform.openai.com/docs/api-reference
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.responses.create(
                model=model,
                temperature=TEMPERATURE,
                instructions=TRANSLATION_SYSTEM_PROMPT,
                input=text,
            )
            return resp.output_text
        except Exception as e:
            if attempt == MAX_RETRIES:
                raise
            # Simple exponential backoff
            sleep_s = RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1))
            time.sleep(sleep_s)


def is_source_newer_than_target(src: Path, tgt: Path) -> bool:
    """Return True if src exists and is newer than tgt (or tgt missing)."""
    if not src.exists():
        return False
    if not tgt.exists():
        return True
    return src.stat().st_mtime > tgt.stat().st_mtime


def translate_notebook(
    client: OpenAI, nb: NotebookNode, model: str, dry_run: bool = False
) -> NotebookNode:
    """Translate Markdown and Raw cells; leave Code cells unchanged."""
    new_nb = nbformat.v4.new_notebook(metadata=nb.metadata)
    new_nb.cells = []

    for cell in nb.cells:
        if cell.cell_type in ("markdown", "raw"):
            original = cell.source
            translated = original if dry_run else translate_text(client, original, model)
            new_cell = nbformat.v4.new_markdown_cell(translated) if cell.cell_type == "markdown" \
                else nbformat.v4.new_raw_cell(translated)
            # Preserve metadata when possible
            new_cell.metadata = cell.get("metadata", {})
            new_nb.cells.append(new_cell)
        else:
            # code cell: copy as-is (including outputs)
            new_nb.cells.append(cell)

    return new_nb



def main():
    parser = argparse.ArgumentParser(description="Translate .ipynb (DE->EN) cell-by-cell.")
    parser.add_argument("folder", type=str, help="Folder to scan for .ipynb files")
    parser.add_argument("--model", type=str, default=MODEL_DEFAULT, help="OpenAI model to use")
    parser.add_argument("--dry-run", action="store_true", help="Do not call the API; just show which files would be processed")
    args = parser.parse_args()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        print(f"Error: folder does not exist or is not a directory: {folder}", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not args.dry_run and not api_key:
        print("Error: OPENAI_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    client = OpenAI() if not args.dry_run else None

    ipynb_files = sorted(p for p in folder.glob("**/*.ipynb") if not p.name.endswith("_en.ipynb"))
    if not ipynb_files:
        print("No .ipynb files found.")
        return

    for src in tqdm(ipynb_files, desc="Processing notebooks"):
        tgt = src.with_name(src.stem + "_en" + src.suffix)
        if not is_source_newer_than_target(src, tgt):
            # Skip if target exists and is up-to-date
            continue

        if args.dry_run:
            print(f"[DRY-RUN] Would translate: {src} -> {tgt}")
            continue

        try:
            nb = nbformat.read(src, as_version=4)
            new_nb = translate_notebook(client, nb, args.model, dry_run=False)

            # Ensure target directory exists
            tgt.parent.mkdir(parents=True, exist_ok=True)
            nbformat.write(new_nb, tgt)
            # Copy mtime from source so future runs compare correctly
            os.utime(tgt, (src.stat().st_atime, src.stat().st_mtime))
            print(f"Translated: {src.name} -> {tgt.name}")
        except Exception as e:
            print(f"Failed to translate {src}: {e}", file=sys.stderr)

    print("Done.")


if __name__ == "__main__":
    main()