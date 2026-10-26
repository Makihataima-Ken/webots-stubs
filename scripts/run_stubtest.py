"""Compare the stubs with the real Webots Python modules using mypy's stubtest.

stubtest imports the runtime ``controller`` and ``vehicle`` packages and checks every
class, method, signature and constant against the stubs. Importing those packages
normally loads Webots' libController shared library, so by default this script
substitutes an inert stand-in for the library: the module source is the genuine
upstream code, only the native calls are faked. That keeps the check runnable
anywhere, without a Webots installation.

Pass ``--webots-home`` (or set ``WEBOTS_HOME`` and pass ``--real``) to run against a
real Webots installation instead.

Usage::

    python scripts/fetch_upstream.py
    python scripts/run_stubtest.py [MODULE ...] [--tag TAG] [--real | --webots-home DIR] [-- stubtest args]

MODULE defaults to the ``controller`` and ``vehicle`` packages; naming modules such as
``controller.motor`` restricts the check to them.
"""

from __future__ import annotations

import argparse
import ctypes
import os
import sys
from pathlib import Path
from typing import Any

from _upstream import ROOT, upstream_dir, webots_tag

STUBTEST_DIR = ROOT / "tests" / "stubtest"
PACKAGES = ["controller", "vehicle"]


class _FakeFunction:
    """Stands in for a foreign function: accepts restype/argtypes, returns 0 when called."""

    restype: Any = None
    argtypes: Any = None

    def __call__(self, *args: object) -> int:
        return 0


class _FakeLibrary(ctypes.CDLL):
    """A CDLL that resolves every symbol to a ``_FakeFunction`` instead of loading a library."""

    def __init__(self, name: str, *args: object, **kwargs: object) -> None:
        self._name = name
        self._handle = 0
        self._functions: dict[str, _FakeFunction] = {}

    def __getattr__(self, name: str) -> _FakeFunction:  # type: ignore[override]
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)
        return self._functions.setdefault(name, _FakeFunction())

    def __getitem__(self, name: str) -> _FakeFunction:  # type: ignore[override]
        return self.__getattr__(name)


def _install_fake_libcontroller() -> None:
    os.environ.setdefault("WEBOTS_HOME", str(ROOT / ".upstream" / "fake-webots-home"))
    ctypes.cdll.LoadLibrary = _FakeLibrary  # type: ignore[method-assign]

    def in_dll(cls: type[Any], library: object, name: str) -> Any:
        # Exported constants of the C library (e.g. wb_ROTATIONAL) read as 0 or "".
        return cls(b"") if cls is ctypes.c_char_p else cls(0)

    ctypes.c_int.in_dll = classmethod(in_dll)  # type: ignore[assignment,method-assign]
    ctypes.c_char_p.in_dll = classmethod(in_dll)  # type: ignore[assignment,method-assign]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("modules", nargs="*", default=PACKAGES, help="modules to check (default: all)")
    parser.add_argument("--tag", default=webots_tag(), help="fetched upstream tag (default: %(default)s)")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--real", action="store_true", help="use the Webots installation in WEBOTS_HOME")
    mode.add_argument("--webots-home", type=Path, help="use the Webots installation in this directory")
    own_args, stubtest_args = sys.argv[1:], []
    if "--" in own_args:
        split = own_args.index("--")
        own_args, stubtest_args = own_args[:split], own_args[split + 1 :]
    args = parser.parse_args(own_args)

    if args.webots_home is not None or args.real:
        home = args.webots_home or Path(os.environ["WEBOTS_HOME"])
        os.environ["WEBOTS_HOME"] = str(home)
        python_dir = home / ("Contents" if sys.platform == "darwin" else "") / "lib" / "controller" / "python"
    else:
        python_dir = upstream_dir(args.tag) / "lib" / "controller" / "python"
        _install_fake_libcontroller()
    sys.path.insert(0, str(python_dir))

    from mypy import stubtest

    allowlists = [STUBTEST_DIR / "allowlist.txt", STUBTEST_DIR / f"allowlist_{sys.platform}.txt"]
    argv = [*args.modules, "--mypy-config-file", str(STUBTEST_DIR / "mypy.ini")]
    if sorted(args.modules) != PACKAGES:
        # Entries about modules outside a partial run are expected to be unused.
        argv.append("--ignore-unused-allowlist")
    for allowlist in allowlists:
        if allowlist.is_file():
            argv += ["--allowlist", str(allowlist)]
    return stubtest.test_stubs(stubtest.parse_options([*argv, *stubtest_args]))


if __name__ == "__main__":
    sys.exit(main())
