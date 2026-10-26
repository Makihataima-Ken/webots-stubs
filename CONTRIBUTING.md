# Contributing to webots-stubs

Thanks for helping make the Webots Python API pleasant to use in typed code!
This guide explains how the project is laid out, how to check your changes, and
the conventions every stub follows.

## Project layout

```
src/controller/      stubs for the `controller` package (one .pyi per upstream module)
src/vehicle/         stubs for the `vehicle` package (Driver, Car)
tests/typecheck/     code that is type-checked (never run) to pin down the stubs' behavior
tests/stubtest/      stubtest configuration and allowlist
tests/samples/       configuration and known errors of the sample-controller check
scripts/             maintenance scripts (fetching upstream sources, stubtest, checks)
examples/            small typed controllers, type-checked in CI
```

The stub directories use importable names (`controller`, `vehicle`) so that mypy
and pyright read them directly during development. The wheel ships them as the
PEP 561 stub-only packages `controller-stubs` and `vehicle-stubs`.

## Development setup

You need [uv](https://docs.astral.sh/uv/) and git.

```sh
uv sync                                 # create .venv with the development tools
uv run python scripts/fetch_upstream.py # fetch the Webots sources into .upstream/
uv run pre-commit install               # optional: format and lint on every commit
```

The targeted Webots release is set once, by `webots-tag` in the `[tool.webots-stubs]`
table of `pyproject.toml`. For that release, `fetch_upstream.py` downloads the Python API
(`lib/controller/python`), the reference manual (`docs/reference`, `docs/automobile`)
and the sample controllers (`projects/**/controllers`). The stubs are written and
checked against these files.

## Checks

Run them all before opening a pull request; CI runs the same commands.

```sh
uv run ruff format --check .
uv run ruff check .
uv run mypy src tests examples
uv run mypy scripts
uv run pyright
uv run python scripts/run_stubtest.py
uv run python scripts/check_api_coverage.py
uv run python scripts/check_samples.py
```

`run_stubtest.py` runs mypy's [stubtest](https://mypy.readthedocs.io/en/stable/stubtest.html),
which imports the real upstream modules and compares every class, method,
signature and constant with the stubs. It works without a Webots installation
(the native library is replaced by an inert stand-in); pass
`--webots-home /path/to/webots` to run it against a real installation. Pass module
names (e.g. `controller.motor`) to check only those. Intentional differences
between stubs and runtime go in `tests/stubtest/allowlist.txt`, each with a
comment explaining why.

`check_api_coverage.py` parses the upstream sources and the stubs, and reports public
names the stubs miss and stub items without a docstring.

`check_samples.py` type-checks the Python sample controllers shipped with Webots
against the stubs. Errors that are problems of the samples themselves are listed in
`tests/samples/known_errors.txt`, each with a reason; any other error, typically a stub
that is too strict, fails the check. After an intended change, refresh the list with
`--update` and give every new entry a reason.

## Typing conventions

The stubs describe what the upstream code *actually does*. Upstream inline
annotations are a starting point, not the truth: always read the function body.

- **Annotate everything.** Every parameter and return type is annotated; methods
  that return nothing are `-> None`. `Incomplete` and unexplained `Any` are not
  allowed.
- **Match the runtime signature exactly.** Keep upstream parameter names, order,
  kinds and defaults, even when they are unusual (`p`, `d`, `fromNode`). stubtest
  enforces this.
- **`None` results are part of the type.** When a method can return `None` (for
  example `return None if tag == 0 else Brake(tag)`, or a lookup that fails),
  return `X | None`. Two deliberate exceptions keep everyday code ergonomic:
  - `Robot.getDevice()` returns `Any`: the device class depends on the robot,
    so users annotate the variable (`motor: Motor = robot.getDevice("motor")`);
  - the deprecated typed getters (`Robot.getMotor()`, ...) return their class.
- **Optional parameters** are spelled `x: int | None = None`.
- **Constants** are `Final`. Constants written as literals in the upstream source
  keep their value (`EVENT_QUIT: Final = -1`); constants read from the C library
  with `constant()` are `Final[int]` (or `Final[str]`). Constants that upstream
  assigns after the class body (`Node.NO_NODE = constant(...)`) are declared in the
  class body.
- **Properties** keep their getter and setter together; setters return `None`.
  A write-only property (`force = property(fset=setForce)`) gets a getter typed
  `Never` and a docstring starting with "Write-only".
- **Precise containers.** Use `list[float]`, `list[list[int]]`, etc. Where the
  return type depends on an argument (such as `data_type="list"` versus a raw
  ctypes buffer), use `@overload` with `Literal` arguments.
- **Deprecated API** (methods that print a `DEPRECATION` message) is decorated with
  `@deprecated("Use X instead.")` from `typing_extensions`.
- **Imports.** Import within the package relatively (`from .device import Device`).
  Do not re-export implementation details such as `wb` or `constant` from device
  modules. Use `X | Y` and built-in generics; import `Any`, `ClassVar`, `Final`,
  `Literal` and `overload` from `typing`, and `deprecated`, `Never` and `Self` from
  `typing_extensions`.
- **Scope.** Private (`_`-prefixed) names are omitted. Public instance attributes
  assigned in `__init__` are declared in the class body. Dunder methods that exist
  at runtime (`__init__`, `__del__`, `__eq__`, ...) are included. Definitions that
  only exist on some platforms go under `if sys.platform == ...`.

## Docstrings

Stub docstrings are what users see when hovering in their editor, so every public
class, method, function, property and constant has one. Bare `...` bodies are only
used for property setters, `__del__` and constructors users do not call themselves
(device classes are obtained from `Robot.getDevice()`).

- **Classes:** a one-line summary, optionally a short paragraph (units, typical use),
  and a final `Reference:` line linking to the reference manual page with
  `?tab-language=python`.
- **Methods and functions:** an imperative summary line (“Return …”, “Set …”) that
  ends with a period and states units in brackets (`[ms]`, `[rad]`, `[m/s]`,
  `[N⋅m]`). Add up to four lines on behavior users need: valid ranges, when the value
  is available, when `None` is returned, what must be enabled first. End with a
  `Reference:` line pointing at the C function's anchor, e.g.
  `https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_position`.
- **Properties:** a single line describing the value and its unit, and naming the
  equivalent methods: “The target position [rad or m] (same as `getTargetPosition()`
  / `setPosition()`).” No `Reference:` line.
- **Constants:** a one-line docstring right below the declaration.
- Write the text yourself, concisely, from the reference manual. Skip notes that only
  concern C, C++, Java or MATLAB; keep Python-specific ones. Lines stay within 120
  characters (a trailing URL may run over).

## Updating to a new Webots release

The weekly *Upstream drift* workflow compares the stubs with the `master` branch of
Webots and opens an issue when they differ, so most changes are known before a release.

1. Set `webots-tag` in `pyproject.toml` to the new release (e.g. `R2026a`) and fetch it:
   `uv run python scripts/fetch_upstream.py`.
2. Run the checks. stubtest and `check_api_coverage.py` list everything that was added,
   removed or changed; `check_samples.py --update` refreshes the sample errors.
3. Update the stubs and docstrings, then the version in `pyproject.toml`: release
   `R20XXa` maps to `20XX.1.N` and `R20XXb` to `20XX.2.N`, `N` counting stub releases
   for that Webots release.
4. Add a `CHANGELOG.md` entry and the new row of the version table in `README.md`.

To publish a release, push a tag `v<version>` (e.g. `v2025.1.0`): the *Release*
workflow checks that it matches `pyproject.toml`, builds the distribution and
publishes it to PyPI with trusted publishing.

## Pull requests

Keep pull requests focused, describe the user-visible effect, and add a case under
`tests/typecheck/` for any behavior worth pinning down (a return type, an overload,
an `Optional` result).
