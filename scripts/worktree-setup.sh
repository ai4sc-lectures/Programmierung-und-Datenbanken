#!/usr/bin/env bash
# Set up (or rebuild) this git worktree: own venv, shared caches via orca.yaml.
# Idempotent: rerun it to rebuild instead of plain `uv sync`.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
# Main checkout: Orca passes ORCA_ROOT_PATH; the git fallback works with the renamed .git.nosync.
MAIN="${ORCA_ROOT_PATH:-$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")}"

# --- Python (uv), OWN venv: cli/tasks are installed editable, so a shared venv would
# import another checkout's code. Keep it out of iCloud like the main checkout.
if [ ! -e .venv ]; then
    mkdir -p .venv.nosync
    ln -s .venv.nosync .venv
fi
uv sync
# .pyc files into the venv (.venv.nosync/pycache) instead of __pycache__ folders iCloud syncs;
# same .pth file as uvinit writes.
echo 'import sys, os; sys.pycache_prefix = os.path.join(sys.prefix, "pycache")' \
    > "$(.venv/bin/python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/zz_pycache_prefix.pth"

# --- links to the *.nosync folders. Shared ones come from orca.yaml (Orca only shares
# directories, not the NAME -> NAME.nosync links); per-worktree ones are created here.
ln -sfn _freeze.nosync lectures/_freeze                 # shared
ln -sfn .jupyter_cache.nosync lectures/.jupyter_cache   # shared
ln -sfn node_modules.nosync .opencode/node_modules      # shared
mkdir -p lectures/.quarto.nosync _build.nosync          # per-render state, per worktree
[ -e lectures/.quarto ] || ln -s .quarto.nosync lectures/.quarto
[ -e _build ] || ln -s _build.nosync _build

# --- single gitignored file: can't be a shared directory, link it
if [ "$ROOT" != "$MAIN" ] && [ -e "$MAIN/lectures/CLAUDE.md" ]; then
    ln -sfn "$MAIN/lectures/CLAUDE.md" lectures/CLAUDE.md
fi

# --- shared dirs from orca.yaml should exist ---
for d in lectures/_freeze.nosync lectures/_extensions .claude/skills; do
    [ -e "$d" ] || echo "warning: $d is missing; is it gitignored and present in the main checkout?" >&2
done
