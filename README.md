# webots-stubs

[![PyPI](https://img.shields.io/pypi/v/webots-stubs)](https://pypi.org/project/webots-stubs/)
[![Python versions](https://img.shields.io/pypi/pyversions/webots-stubs)](https://pypi.org/project/webots-stubs/)
[![License](https://img.shields.io/pypi/l/webots-stubs)](LICENSE)

Type stubs for the Python API of the [Webots](https://cyberbotics.com) robot simulator.

Webots runs Python controllers with its own `controller` and `vehicle` packages, which
live inside the Webots installation rather than on PyPI. Editors and type checkers
therefore cannot see them, so there is no autocompletion and no type checking. This
package fixes that. It gives VS Code (Pylance), PyCharm, mypy and pyright:

- **full autocompletion** for every class, method, property and constant of the
  `controller` and `vehicle` packages;
- **hover documentation** for every item, with units (`[rad]`, `[m/s]`, `[ms]`, ...) and a
  link to the matching section of the Webots reference manual;
- **precise types** taken from the code Webots actually runs: methods that can return
  `None` say so, raw ctypes buffers are not passed off as lists, overloads follow arguments
  such as `data_type`, and constants are `Final`;
- **deprecation warnings** for deprecated API such as `Robot.getMotor()`;
- **notes on runtime quirks** of the Webots release where its behavior differs from the
  manual.

```python
from controller import DistanceSensor, Motor, Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

sensor: DistanceSensor = robot.getDevice("ps0")
sensor.enable(timestep)
motor: Motor = robot.getDevice("left wheel motor")
motor.setPosition(float("inf"))

while robot.step(timestep) != -1:
    motor.setVelocity(6.28 if sensor.getValue() < 80 else -6.28)
```

## Installation

Install the stubs into the Python environment that your editor or type checker uses:

```sh
pip install webots-stubs
```

Then pick the stubs version that matches your Webots release:

| Webots | webots-stubs |
| ------ | ------------ |
| R2025a | 2025.1.*     |

The package contains type information only (PEP 561 `controller-stubs` and
`vehicle-stubs`). At run time your controllers keep using the modules that Webots
provides, and nothing changes in how Webots starts them.

## Editor and type checker setup

**VS Code (Pylance)**: select the interpreter where you installed the stubs
(*Python: Select Interpreter*). If your settings add the Webots controller directory to
`python.analysis.extraPaths`, remove it: code on the extra paths takes precedence over
stub packages, so the Webots sources would hide the stubs. Because the runtime modules
are then not visible to the editor, Pylance shows the warning *Import "controller" could
not be resolved from source* on the import line. It is harmless; to silence it, add this
to your `settings.json`:

```json
"python.analysis.diagnosticSeverityOverrides": { "reportMissingModuleSource": "none" }
```

**PyCharm**: select the interpreter where you installed the stubs. If you added
`$WEBOTS_HOME/lib/controller/python` to the interpreter paths and completion does not
pick up the stubs, remove that path.

**pyright**: nothing to configure; set `reportMissingModuleSource = "none"` to silence the
warning described above. Like Pylance, pyright prefers code listed in `extraPaths` over
the stubs.

**mypy**: nothing to configure. Do not put the Webots controller directory on `MYPYPATH`,
for the same reason.

The stubs themselves are checked with mypy and pyright in strict mode.

## Working with the types

**Devices.** `Robot.getDevice()` returns `Any`, because the device class depends on the
robot. Annotate the variable to get completion and type checking for the device:

```python
camera: Camera = robot.getDevice("camera")
```

`Robot.getDeviceByIndex()` returns a `Device`. Narrow it with `isinstance`, which works
because Webots creates instances of the concrete classes:

```python
device = robot.getDeviceByIndex(i)
if isinstance(device, Lidar):
    device.enablePointCloud()
```

**Lookups that can fail** return `X | None`, as they do at run time:
`Supervisor.getFromDef()`, `Node.getField()`, `Motor.getPositionSensor()` and others. Check
the result before using it:

```python
robot_node = supervisor.getFromDef("ROBOT")
if robot_node is None:
    raise LookupError("no node with DEF name ROBOT")
translation = robot_node.getField("translation")
```

**Importing device classes.** Import them from `controller` as usual. A few classes that the
`controller` package does not export at run time, such as `Device` and `Pen`, must be
imported from their module: `from controller.pen import Pen`.

The [`examples`](examples) directory contains complete typed controllers.

## How the stubs are checked

- [stubtest](https://mypy.readthedocs.io/en/stable/stubtest.html) imports the real
  `controller` and `vehicle` packages of the targeted Webots release and compares every
  class, signature and constant with the stubs.
- The Python sample controllers shipped with Webots are type-checked against the stubs.
  Every error they produce is reviewed, which catches stubs that are too strict.
- mypy and pyright check the stubs, the type-checking tests in
  [`tests/typecheck`](tests/typecheck) and the examples in strict mode.
- A coverage check makes sure no public name is missing and every item is documented.

## Contributing

Bug reports and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the
development setup and the conventions the stubs follow.

## Prior work

Type annotations for the Webots Python API have been discussed upstream in
[cyberbotics/webots#2385](https://github.com/cyberbotics/webots/issues/2385) and
[#2959](https://github.com/cyberbotics/webots/issues/2959). A stubs package was prototyped
in [cyberbotics/webots#5472](https://github.com/cyberbotics/webots/pull/5472). This project
takes the idea further as a standalone package, so that it costs the Webots maintainers
nothing.

## License

Apache License 2.0, the same as Webots. The stubs and their docstrings are derived from
the Webots source code and reference manual (Copyright Cyberbotics Ltd.); see
[NOTICE](NOTICE). Webots is a trademark of Cyberbotics Ltd. This project is not affiliated
with or endorsed by Cyberbotics Ltd.
