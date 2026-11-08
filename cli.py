"""uv entry points: thin wrappers around the invoke tasks in tasks.py.

Usage: `uv run build`, `uv run build --all`, `uv run serve`, ...
Extra CLI arguments are passed through to the invoke task.
"""

import sys

from invoke import Collection, Program

import tasks

_program = Program(namespace=Collection.from_module(tasks), version="0.1.0")


def _run(*task_args: str) -> None:
    _program.run(["invoke", *task_args, *sys.argv[1:]])


def build() -> None:
    _run("build")


def serve() -> None:
    _run("serve")


def publish() -> None:
    _run("publish")

def update() -> None:
    _run("update")