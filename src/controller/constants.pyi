"""Access to the constants exported by the Webots controller library.

This module is an implementation detail of the `controller` package.
"""

from typing import overload

@overload
def constant(name: str, type: type[int] = ...) -> int:
    """Return the value of the integer constant `wb_<name>` exported by the controller library."""

@overload
def constant(name: str, type: type[str]) -> str:
    """Return the value of the string constant `wb_<name>` exported by the controller library."""
