"""Loader of the Webots controller library (libController), which the whole API calls into.

This module is an implementation detail of the `controller` package.
"""

from ctypes import CDLL

path: str
"""Location of the controller library, relative to `WEBOTS_HOME`."""

wb: CDLL
"""The loaded controller library."""
