from ctypes import _Pointer, c_double  # pyright: ignore[reportPrivateUsage]
from typing import Final

from .sensor import Sensor

class DistanceSensor(Sensor):
    """A distance sensor (infra-red, sonar, laser or generic) measuring the distance to obstacles.

    The measurements are mapped through the `lookupTable` field of the node, which therefore
    defines the unit and range of the values. Enable the device with `enable()` before reading it.

    Reference: https://cyberbotics.com/doc/reference/distancesensor?tab-language=python
    """

    GENERIC: Final = 0
    """Sensor type of a `type` field set to "generic" (see `getType()`)."""
    INFRA_RED: Final = 1
    """Sensor type of a `type` field set to "infra-red" (see `getType()`)."""
    SONAR: Final = 2
    """Sensor type of a `type` field set to "sonar" (see `getType()`)."""
    LASER: Final = 3
    """Sensor type of a `type` field set to "laser" (see `getType()`)."""

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getAperture(self) -> float:
        """Return the aperture of the sensor [rad].

        Reference: https://cyberbotics.com/doc/reference/distancesensor?tab-language=python#wb_distance_sensor_get_aperture
        """

    def getLookupTable(self) -> list[float]:
        """Return the lookup table of the sensor as a flat list of N * 3 numbers (N rows of 3 values).

        Reference: https://cyberbotics.com/doc/reference/distancesensor?tab-language=python#wb_distance_sensor_get_lookup_table
        """

    def getMaxValue(self) -> float:
        """Return the largest value the sensor can return (maximum of the second column of the lookup table).

        Reference: https://cyberbotics.com/doc/reference/distancesensor?tab-language=python#wb_distance_sensor_get_max_value
        """

    def getMinValue(self) -> float:
        """Return the smallest value the sensor can return (minimum of the second column of the lookup table).

        Reference: https://cyberbotics.com/doc/reference/distancesensor?tab-language=python#wb_distance_sensor_get_min_value
        """

    def getType(self) -> int:
        """Return the sensor type: `DistanceSensor.GENERIC`, `INFRA_RED`, `SONAR` or `LASER`.

        Reference: https://cyberbotics.com/doc/reference/distancesensor?tab-language=python#wb_distance_sensor_get_type
        """

    def getValue(self) -> float:
        """Return the latest measurement, as mapped by the lookup table of the sensor.

        Reference: https://cyberbotics.com/doc/reference/distancesensor?tab-language=python#wb_distance_sensor_get_value
        """

    @property
    def aperture(self) -> float:
        """The aperture of the sensor [rad] (same as `getAperture()`)."""

    @property
    def lookup_table(self) -> _Pointer[c_double]:
        """The lookup table as a raw ctypes array of N * 3 numbers, N being the number of rows.

        Unlike `getLookupTable()`, this is not a list and its length is not bounded.
        """

    @property
    def max_value(self) -> float:
        """The largest value the sensor can return (same as `getMaxValue()`)."""

    @property
    def min_value(self) -> float:
        """The smallest value the sensor can return (same as `getMinValue()`)."""

    @property
    def type(self) -> int:
        """The sensor type, `DistanceSensor.GENERIC`, `INFRA_RED`, `SONAR` or `LASER` (same as `getType()`)."""

    @property
    def value(self) -> float:
        """The latest measurement, as mapped by the lookup table (same as `getValue()`)."""
