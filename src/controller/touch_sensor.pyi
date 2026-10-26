from ctypes import _Pointer, c_double  # pyright: ignore[reportPrivateUsage]
from typing import Final

from .sensor import Sensor

class TouchSensor(Sensor):
    """A sensor measuring contact: a bumper (0 or 1), a force [N] or a 3D force vector [N].

    Enable the device with `enable()` before reading it. Use `getValue()` for "bumper" and "force"
    sensors, `getValues()` for "force-3d" ones.

    Reference: https://cyberbotics.com/doc/reference/touchsensor?tab-language=python
    """

    BUMPER: Final = 0
    """Sensor type of a `type` field set to "bumper" (see `getType()`)."""
    FORCE: Final = 1
    """Sensor type of a `type` field set to "force" (see `getType()`)."""
    FORCE3D: Final = 2
    """Sensor type of a `type` field set to "force-3d" (see `getType()`)."""

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getValue(self) -> float:
        """Return the latest measurement of a "bumper" (0.0 or 1.0) or "force" [N] sensor.

        Reference: https://cyberbotics.com/doc/reference/touchsensor?tab-language=python#wb_touch_sensor_get_value
        """

    def getValues(self) -> _Pointer[c_double]:
        """Return the latest force vector `[x, y, z]` [N] measured by a "force-3d" sensor.

        The result is a raw ctypes array, not a list: only the indices 0, 1 and 2 are valid.

        Reference: https://cyberbotics.com/doc/reference/touchsensor?tab-language=python#wb_touch_sensor_get_values
        """

    def getLookupTable(self) -> list[float]:
        """Return the lookup table of the sensor as a flat list of N * 3 numbers (N rows of 3 values).

        Reference: https://cyberbotics.com/doc/reference/touchsensor?tab-language=python#wb_touch_sensor_get_lookup_table
        """

    def getType(self) -> int:
        """Return the sensor type: `TouchSensor.BUMPER`, `FORCE` or `FORCE3D`.

        Reference: https://cyberbotics.com/doc/reference/touchsensor?tab-language=python#wb_touch_sensor_get_type
        """

    @property
    def value(self) -> float:
        """The latest "bumper" (0.0 or 1.0) or "force" [N] measurement (same as `getValue()`)."""

    @property
    def values(self) -> _Pointer[c_double]:
        """The latest "force-3d" force vector `[x, y, z]` [N], a raw ctypes array (same as `getValues()`)."""

    @property
    def lookup_table(self) -> list[float]:
        """The lookup table as a flat list of N * 3 numbers (same as `getLookupTable()`)."""

    @property
    def type(self) -> int:
        """The sensor type, `TouchSensor.BUMPER`, `FORCE` or `FORCE3D` (same as `getType()`)."""
