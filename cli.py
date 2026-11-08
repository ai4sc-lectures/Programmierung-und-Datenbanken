"""uv entry points: thin wrappers around the invoke tasks in tasks.py.

Usage: `uv run build`, `uv run build --all`, `uv run serve`,
`uv run render 02b --to all`, `uv run preview 06a`, ...
Extra CLI arguments are passed through to the invoke task.

The .venv is shared between the main checkout and the git worktrees, and the editable
install of this project points at whichever checkout installed it last. So this module
must not import `tasks` itself: invoke loads `tasks.py` from the current directory
(searching upwards), which is always the checkout the command is run in.
"""

import sys

from invoke import Program


def _run(task: str) -> None:
    Program(version="0.1.0").run(["invoke", task, *sys.argv[1:]])


def build() -> None:
    _run("build")


def serve() -> None:
    _run("serve")


def publish() -> None:
    _run("publish")


def update() -> None:
    _run("update")


def render() -> None:
    _run("render")


def preview() -> None:
    _run("preview")
