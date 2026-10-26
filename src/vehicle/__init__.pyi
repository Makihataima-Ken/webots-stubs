"""Python API of the Webots automobile library, used by controllers of vehicles.

`Driver` drives a car like a human would (steering, throttle, brakes, gears, lights);
`Car` adds the information and functions a human driver does not have access to.
Webots adds this package to the path of the controllers it starts; it is not
installed from PyPI. These stubs only describe it for type checkers and IDEs.

Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python
"""

from .car import Car as Car
from .driver import Driver as Driver
