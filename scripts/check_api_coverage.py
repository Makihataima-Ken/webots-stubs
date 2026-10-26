"""Check that the stubs cover the upstream API and that every public stub item is documented.

Unlike stubtest, this check only parses source code, so it also works on an upstream
branch whose native library would not match (e.g. to spot API drift on ``master``).
It reports:

* public classes, functions, methods, properties, constants and instance attributes of
  the upstream ``controller`` and ``vehicle`` packages that the stubs do not declare;
* public stub items without a docstring (see "Docstrings" in CONTRIBUTING.md).

Usage::

    python scripts/check_api_coverage.py [--tag TAG]
"""

from __future__ import annotations

import argparse
import ast
import sys
from collections.abc import Iterator
from pathlib import Path

from _upstream import ROOT, upstream_dir, webots_tag

PACKAGES = ("controller", "vehicle")
# Bodies that may stay undocumented: users never call these directly.
UNDOCUMENTED_METHODS = {"__init__", "__del__"}


def _is_public(name: str) -> bool:
    return not name.startswith("_")


def _decorator_names(node: ast.FunctionDef) -> set[str]:
    names: set[str] = set()
    for decorator in node.decorator_list:
        target = decorator.func if isinstance(decorator, ast.Call) else decorator
        if isinstance(target, ast.Attribute):
            names.add(target.attr)
        elif isinstance(target, ast.Name):
            names.add(target.id)
    return names


def _flatten(body: list[ast.stmt]) -> Iterator[ast.stmt]:
    """Yield the statements of ``body``, descending into ``if`` blocks (platform checks)."""
    for statement in body:
        if isinstance(statement, ast.If):
            yield from _flatten(statement.body)
            yield from _flatten(statement.orelse)
        else:
            yield statement


def _assigned_names(statement: ast.stmt) -> list[str]:
    if isinstance(statement, ast.Assign):
        return [target.id for target in statement.targets if isinstance(target, ast.Name)]
    if isinstance(statement, ast.AnnAssign) and isinstance(statement.target, ast.Name):
        return [statement.target.id]
    return []


def runtime_api(path: Path) -> set[str]:
    """Return the public names defined by an upstream module, as ``Class.member`` or ``name``."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: set[str] = set()
    for statement in _flatten(tree.body):
        if isinstance(statement, ast.ClassDef) and _is_public(statement.name):
            names.add(statement.name)
            for member in _flatten(statement.body):
                if isinstance(member, ast.FunctionDef):
                    if _is_public(member.name):
                        names.add(f"{statement.name}.{member.name}")
                    if member.name == "__init__":
                        for node in ast.walk(member):
                            if (
                                isinstance(node, ast.Attribute)
                                and isinstance(node.ctx, ast.Store)
                                and isinstance(node.value, ast.Name)
                                and node.value.id == "self"
                                and _is_public(node.attr)
                            ):
                                names.add(f"{statement.name}.{node.attr}")
                names.update(f"{statement.name}.{name}" for name in _assigned_names(member) if _is_public(name))
        elif isinstance(statement, ast.FunctionDef) and _is_public(statement.name):
            names.add(statement.name)
        elif isinstance(statement, ast.Assign):
            for target in statement.targets:
                # Constants attached after the class body: ``Node.NO_NODE = constant(...)``.
                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name):
                    names.add(f"{target.value.id}.{target.attr}")
                elif isinstance(target, ast.Name) and _is_public(target.id) and target.id != "__all__":
                    names.add(target.id)
    return names


def _has_docstring(body: list[ast.stmt], index: int) -> bool:
    """Whether the statement at ``index`` is followed by a string expression (attribute docstring)."""
    if index + 1 >= len(body):
        return False
    following = body[index + 1]
    return (
        isinstance(following, ast.Expr)
        and isinstance(following.value, ast.Constant)
        and isinstance(following.value.value, str)
    )


def stub_api(path: Path) -> tuple[set[str], list[str]]:
    """Return the names declared by a stub and the ``line: name`` of its undocumented items."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: set[str] = set()
    undocumented: list[str] = []

    def visit(body: list[ast.stmt], prefix: str) -> None:
        documented_overloads: dict[str, bool] = {}
        for index, statement in enumerate(body):
            if isinstance(statement, ast.If):
                visit(statement.body, prefix)
                visit(statement.orelse, prefix)
            elif isinstance(statement, ast.ClassDef):
                names.add(prefix + statement.name)
                if _is_public(statement.name) and ast.get_docstring(statement) is None:
                    undocumented.append(f"{statement.lineno}: class {prefix}{statement.name}")
                visit(statement.body, f"{prefix}{statement.name}.")
            elif isinstance(statement, ast.FunctionDef):
                name = prefix + statement.name
                names.add(name)
                decorators = _decorator_names(statement)
                documented = ast.get_docstring(statement) is not None
                if "setter" in decorators or statement.name in UNDOCUMENTED_METHODS:
                    continue
                if "overload" in decorators:
                    documented_overloads[name] = documented_overloads.get(name, False) or documented
                elif _is_public(statement.name) and not documented:
                    undocumented.append(f"{statement.lineno}: def {name}")
            else:
                for target in _assigned_names(statement):
                    names.add(prefix + target)
                    if _is_public(target) and not _has_docstring(body, index):
                        undocumented.append(f"{statement.lineno}: {prefix}{target}")
        undocumented.extend(f"overloads of {name}" for name, ok in documented_overloads.items() if not ok)

    visit(tree.body, "")
    return names, undocumented


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tag", default=webots_tag(), help="fetched upstream tag (default: %(default)s)")
    args = parser.parse_args()
    python_dir = upstream_dir(args.tag) / "lib" / "controller" / "python"

    problems = 0
    for package in PACKAGES:
        stubs = {path.stem: stub_api(path) for path in sorted((ROOT / "src" / package).glob("*.pyi"))}
        # Upstream sometimes attaches members to a class defined in another module
        # (``Field.getSFNode = getSFNode`` in node.py): those are looked up package-wide.
        declared_anywhere = set().union(*(declared for declared, _ in stubs.values()))
        for runtime_path in sorted((python_dir / package).glob("*.py")):
            module = f"{package}.{runtime_path.stem}"
            if runtime_path.stem not in stubs:
                print(f"{module}: no stub file")
                problems += 1
                continue
            declared, _ = stubs[runtime_path.stem]
            for name in sorted(runtime_api(runtime_path) - declared):
                owner = name.partition(".")[0]
                if owner not in declared and name in declared_anywhere:
                    continue
                print(f"{module}: {name} is missing from the stub")
                problems += 1
        for stem, (_, undocumented) in stubs.items():
            for item in undocumented:
                print(f"src/{package}/{stem}.pyi:{item} has no docstring")
                problems += 1

    print(f"{problems} problem(s) found" if problems else "API coverage and docstrings: OK")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
