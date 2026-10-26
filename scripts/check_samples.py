"""Type-check the Python sample controllers shipped with Webots against the stubs.

The Webots repository contains about a hundred Python controllers written against the
real API. Type-checking them with the stubs catches stubs that are too strict or simply
wrong: valid controller code must not produce errors. Errors that are genuine problems in
the samples themselves are recorded, one per line and followed by ``  # <reason>``, in
``tests/samples/known_errors.txt``; any other error fails the check, as does a recorded
error that no longer occurs.

Each controller directory is checked separately (sample controllers reuse module names),
with mypy's ``check_untyped_defs`` so that unannotated functions are checked too.

Usage::

    python scripts/check_samples.py [--tag TAG] [--jobs N] [--update]
"""

from __future__ import annotations

import argparse
import os
import queue
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from _upstream import ROOT, upstream_dir, webots_tag

SAMPLES_DIR = ROOT / "tests" / "samples"
KNOWN_ERRORS = SAMPLES_DIR / "known_errors.txt"
MYPY_CONFIG = SAMPLES_DIR / "mypy.ini"
KNOWN_ERRORS_HEADER = (
    "# Errors reported by scripts/check_samples.py in the Webots sample controllers that are\n"
    "# problems of the samples themselves, not of the stubs. One per line: <error>  # <reason>\n"
)
ERROR_LINE = re.compile(r"^(?P<path>[^:]+\.py):(?P<line>\d+): error: (?P<message>.*)$")


def _controller_dirs(projects: Path) -> list[Path]:
    return sorted({path.parent for path in projects.glob("**/controllers/**/*.py")})


def _check(directory: Path, worker_cache: Path, upstream: Path) -> list[str]:
    env = {**os.environ, "MYPY_CACHE_DIR": str(worker_cache), "MYPYPATH": str(ROOT / "src")}
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--config-file", str(MYPY_CONFIG), "--no-error-summary", "."],
        cwd=directory,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(f"mypy failed on {directory}:\n{result.stdout}{result.stderr}")
    errors = []
    for line in result.stdout.splitlines():
        match = ERROR_LINE.match(line)
        if match:
            path = (directory / match["path"]).resolve().relative_to(upstream).as_posix()
            errors.append(f"{path}:{match['line']}: {match['message']}")
    return errors


def _read_known_errors() -> dict[str, str]:
    """Map each recorded error to the reason it is accepted."""
    known = {}
    if KNOWN_ERRORS.is_file():
        for line in KNOWN_ERRORS.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                error, _, reason = line.partition("  # ")
                known[error] = reason
    return known


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tag", default=webots_tag(), help="fetched upstream tag (default: %(default)s)")
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1, help="parallel mypy processes")
    parser.add_argument("--update", action="store_true", help=f"rewrite {KNOWN_ERRORS.name} with the current errors")
    args = parser.parse_args()
    upstream = upstream_dir(args.tag).resolve()
    projects = upstream / "projects"

    directories = _controller_dirs(projects)
    # One mypy cache per concurrent process: mypy caches must not be shared between running processes.
    caches: queue.Queue[Path] = queue.Queue()
    for index in range(args.jobs):
        caches.put(ROOT / ".mypy_cache" / f"samples-{index}")

    def check(directory: Path) -> list[str]:
        cache = caches.get()
        try:
            return _check(directory, cache, upstream)
        finally:
            caches.put(cache)

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        errors = sorted(error for directory_errors in pool.map(check, directories) for error in directory_errors)

    known = _read_known_errors()
    if args.update:
        lines = [f"{error}  # {known.get(error) or 'TODO: explain'}\n" for error in errors]
        KNOWN_ERRORS.write_text(KNOWN_ERRORS_HEADER + "".join(lines), encoding="utf-8", newline="\n")
        print(f"Recorded {len(errors)} error(s) in {KNOWN_ERRORS.relative_to(ROOT).as_posix()}")
        return 0

    new = [error for error in errors if error not in known]
    fixed = sorted(known.keys() - set(errors))
    for error in new:
        print(f"new error: {error}")
    for error in fixed:
        print(f"no longer reported (remove it from {KNOWN_ERRORS.name}): {error}")
    print(
        f"Checked {len(directories)} controller directories: {len(errors)} error(s), {len(new)} new, {len(fixed)} fixed"
    )
    return 1 if new or fixed else 0


if __name__ == "__main__":
    sys.exit(main())
