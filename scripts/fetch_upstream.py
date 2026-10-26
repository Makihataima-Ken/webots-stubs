"""Fetch the parts of the Webots source tree that the stubs are written and checked against.

For one Webots release tag this downloads:

* the Python controller API (``lib/controller/python``),
* the reference documentation (``docs/reference/*.md`` and ``docs/automobile/*.md``),
* the Python sample controllers (``projects/**/controllers/**/*.py``),

using a shallow, blob-filtered, sparse clone so that only those files are transferred.

Usage::

    python scripts/fetch_upstream.py [--tag TAG] [--dest .upstream] [--force]

TAG defaults to ``webots-tag`` in the ``[tool.webots-stubs]`` table of pyproject.toml; any
Webots git tag or branch (e.g. ``develop``) works.
"""

from __future__ import annotations

import argparse
import os
import shutil
import stat
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

from _upstream import ROOT, webots_tag

REPO_URL = "https://github.com/cyberbotics/webots.git"
SPARSE_PATTERNS = (
    "/lib/controller/python/",
    "/docs/reference/*.md",
    "/docs/automobile/*.md",
    "/projects/**/controllers/**/*.py",
)


def _git(*args: str, cwd: Path | None = None) -> None:
    subprocess.run(["git", "-c", "advice.detachedHead=false", *args], cwd=cwd, check=True)


def _force_remove(func: Callable[[str], object], path: str, _exc: object) -> None:
    # Git marks pack files read-only, which makes shutil.rmtree fail on Windows.
    os.chmod(path, stat.S_IWRITE)
    func(path)


def fetch(tag: str, dest: Path, *, force: bool = False) -> Path:
    """Fetch ``tag`` into ``dest / tag`` and return that directory."""
    target = dest / tag
    if target.exists():
        if not force:
            print(f"{target} already exists, nothing to do (use --force to fetch again)")
            return target
        if sys.version_info >= (3, 12):
            shutil.rmtree(target, onexc=_force_remove)
        else:
            shutil.rmtree(target, onerror=_force_remove)
    target.parent.mkdir(parents=True, exist_ok=True)
    _git(
        "clone", "--quiet", "--depth=1", f"--branch={tag}", "--filter=blob:none", "--no-checkout", REPO_URL, str(target)
    )
    _git("sparse-checkout", "set", "--no-cone", *SPARSE_PATTERNS, cwd=target)
    _git("checkout", "--quiet", f"{tag}^{{commit}}", cwd=target)
    print(f"Fetched Webots {tag} into {target}")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tag", default=webots_tag(), help="Webots tag or branch (default: %(default)s)")
    parser.add_argument("--dest", type=Path, default=ROOT / ".upstream", help="destination directory")
    parser.add_argument("--force", action="store_true", help="delete and fetch again if already present")
    args = parser.parse_args()
    fetch(args.tag, args.dest, force=args.force)


if __name__ == "__main__":
    main()
