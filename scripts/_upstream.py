"""Locations shared by the maintenance scripts.

The targeted Webots release is configured once, in ``[tool.webots-stubs]`` of
pyproject.toml, and fetched by fetch_upstream.py into ``.upstream/<tag>``.
"""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def webots_tag() -> str:
    """Return the Webots release tag the stubs target."""
    with (ROOT / "pyproject.toml").open("rb") as file:
        tag: str = tomllib.load(file)["tool"]["webots-stubs"]["webots-tag"]
    return tag


def upstream_dir(tag: str) -> Path:
    """Return the directory holding the fetched sources of ``tag``, exiting if they are missing."""
    directory = ROOT / ".upstream" / tag
    if not directory.is_dir():
        sys.exit(f"{directory} not found; run: python scripts/fetch_upstream.py --tag {tag}")
    return directory
