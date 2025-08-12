#!/usr/bin/env python3
import argparse
import json
import re
import shutil
from pathlib import Path

IMG_RE = re.compile(r'(?P<path>images/[^\s\)\]\}\'"]+)', re.IGNORECASE)
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".svg", ".webp"}

def extract_image_paths_from_notebook(nb_path: Path):
    try:
        data = json.loads(nb_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[FEHLER] Kann Notebook nicht lesen: {nb_path} ({e})")
        return set()
    paths = set()
    for cell in data.get("cells", []):
        src = cell.get("source", [])
        text = "".join(src) if isinstance(src, list) else str(src)
        for m in IMG_RE.finditer(text):
            paths.add(m.group("path"))
    return paths

def update_notebook_paths(nb_path: Path, old_rel: str, new_rel: str):
    """Ersetzt in allen Zellen den Bildpfad old_rel durch new_rel."""
    try:
        data = json.loads(nb_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[FEHLER] Kann Notebook nicht lesen: {nb_path} ({e})")
        return False

    changed = False
    for cell in data.get("cells", []):
        src = cell.get("source", [])
        if isinstance(src, list):
            new_src = []
            for line in src:
                if old_rel in line:
                    line = line.replace(old_rel, new_rel)
                    changed = True
                new_src.append(line)
            cell["source"] = new_src
        else:
            if old_rel in src:
                src = src.replace(old_rel, new_rel)
                changed = True
            cell["source"] = src

    if changed:
        try:
            nb_path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"[AKTUALISIERT] Notebookpfade in {nb_path}")
        except Exception as e:
            print(f"[FEHLER] Konnte Notebook nicht speichern: {e}")
    return changed

def check_and_offer_move(nb_path: Path, rel_img_path: str):
    nb_dir = nb_path.parent
    nb_stem = nb_path.stem
    src_path = (nb_dir / rel_img_path).resolve()

    if not src_path.exists():
        print(f"[WARNUNG] Bild nicht gefunden: {src_path}")
        return

    target_dir = nb_dir / "images" / nb_stem
    try:
        in_correct_dir = Path(src_path).resolve().is_relative_to(target_dir.resolve())
    except AttributeError:
        try:
            src_path.resolve().relative_to(target_dir.resolve())
            in_correct_dir = True
        except Exception:
            in_correct_dir = False

    if in_correct_dir:
        print(f"[OK] {rel_img_path} liegt bereits unter images/{nb_stem}/")
        return

    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / src_path.name

    if target_path.resolve() == src_path.resolve():
        print(f"[OK] {rel_img_path} ist bereits am Ziel.")
        return

    if target_path.exists():
        print(f"[HINWEIS] Ziel existiert bereits: {target_path}")
        if target_path.stat().st_size == src_path.stat().st_size:
            ans = input(f"Datei gleicher Größe existiert. Quelle entfernen? (y/N) ").strip().lower()
            if ans == "y":
                src_path.unlink()
                print(f"[GELÖSCHT] {src_path}")
        return

    rel_target_display = target_path.relative_to(nb_dir)
    ans = input(f"Verschiebe '{rel_img_path}' nach '{rel_target_display}' und aktualisiere Notebook? (y/N) ").strip().lower()
    if ans == "y":
        try:
            shutil.move(str(src_path), str(target_path))
            print(f"[VERSCHOBEN] {src_path} -> {target_path}")
            update_notebook_paths(nb_path, rel_img_path, str(rel_target_display).replace("\\", "/"))
        except Exception as e:
            print(f"[FEHLER] Konnte nicht verschieben: {e}")
    else:
        print("[ÜBERSPRUNGEN] Keine Aktion durchgeführt.")

def collect_used_images(notebooks, images_root: Path):
    used_absolute = set()
    missing_refs = []
    for nb in notebooks:
        img_paths = extract_image_paths_from_notebook(nb)
        if not img_paths:
            continue
        nb_dir = nb.parent
        for rel_img in img_paths:
            abs_path = (nb_dir / rel_img).resolve()
            if abs_path.exists():
                used_absolute.add(abs_path)
            else:
                missing_refs.append((nb, rel_img))
    return used_absolute, missing_refs

def scan_images_tree(images_root: Path):
    files = set()
    if not images_root.exists():
        return files
    for p in images_root.rglob("*"):
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS:
            files.add(p.resolve())
    return files

def main():
    parser = argparse.ArgumentParser(
        description="Scannt Jupyter-Notebooks (ohne .ipynb_checkpoints, old), verschiebt falsch platzierte Bilder und aktualisiert Pfade im Notebook."
    )
    parser.add_argument("verzeichnis", type=Path, help="Startverzeichnis (wird rekursiv durchsucht)")
    parser.add_argument("--images-root", type=Path, default=None,
                        help="Pfad zum images-Stammordner (Standard: <verzeichnis>/images)")
    parser.add_argument("--no-move", action="store_true",
                        help="Nur prüfen, kein Verschiebe-Dialog")
    args = parser.parse_args()

    root = args.verzeichnis.resolve()
    if not root.exists():
        print(f"[FEHLER] Verzeichnis existiert nicht: {root}")
        return

    images_root = (args.images_root.resolve() if args.images_root else (root / "images").resolve())

    notebooks = sorted(
        nb for nb in root.rglob("*.ipynb")
        if ".ipynb_checkpoints" not in nb.parts and "old" not in nb.parts
    )

    if not notebooks:
        print("[INFO] Keine .ipynb-Dateien gefunden.")
    else:
        for nb in notebooks:
            print(f"\n===== Notebook: {nb} =====")
            img_paths = extract_image_paths_from_notebook(nb)
            if not img_paths:
                print("[INFO] Keine Bildpfade gefunden (images/...).")
            for rel_img in sorted(img_paths):
                if not args.no_move:
                    check_and_offer_move(nb, rel_img)
                else:
                    abs_path = (nb.parent / rel_img).resolve()
                    if not abs_path.exists():
                        print(f"[WARNUNG] Bild nicht gefunden: {abs_path}")

    used_absolute, missing_refs = collect_used_images(notebooks, images_root)
    images_in_tree = scan_images_tree(images_root)
    unused = sorted(p for p in images_in_tree if p not in used_absolute)

    print("\n===== Zusammenfassung =====")
    print(f"Images-Stammordner: {images_root}")
    print(f"Gefundene Notebooks: {len(notebooks)}")
    print(f"Referenzierte, existente Bilder: {len(used_absolute)}")
    print(f"Gesamtbilder unter images/: {len(images_in_tree)}")
    print(f"Nicht verwendete Bilder unter images/: {len(unused)}")

    if missing_refs:
        print("\n[WARNUNG] Nicht gefundene Bild-Referenzen:")
        for nb, relp in missing_refs:
            print(f"  - {nb}: {relp}")

    if unused:
        print("\n[LISTE] Unbenutzte Bilder:")
        for p in unused:
            try:
                rel = p.relative_to(images_root)
            except ValueError:
                rel = p
            print(f"  - {rel}")

if __name__ == "__main__":
    main()