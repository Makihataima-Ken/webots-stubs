# Changelog

Versions follow the Webots release they describe: `2025.1.N` is the `N`-th release of the
stubs for Webots R2025a (`2025.2.N` would be for R2025b). See
[CONTRIBUTING.md](CONTRIBUTING.md#updating-to-a-new-webots-release).

## 2025.1.0 (unreleased)

First release, for Webots R2025a.

- Complete stubs for the `controller` and `vehicle` packages: every class, method,
  property and constant of the Webots R2025a Python API.
- Docstrings for every class, method, property and constant, with units and, for the
  API functions, links to the Webots reference manual.
- Types taken from the code Webots runs: `None` results of lookups that can fail,
  ctypes buffers where the API returns them, overloads for arguments that change the
  return type, `Final` constants and deprecation markers.
- `Robot.getDevice()` returns `Any`: annotate the variable to get a typed device.
- Docstrings note where the R2025a runtime departs from the reference manual.
