from .sensor import Sensor

class Compass(Sensor):
    """A compass indicating the direction of the north in the coordinate system of the device.

    Enable the device with `enable()` before reading it.

    Reference: https://cyberbotics.com/doc/reference/compass?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getValues(self) -> list[float]:
        """Return the latest measurement as `[x, y, z]`, a unit vector pointing to the north.

        Axes disabled with the `xAxis`, `yAxis` and `zAxis` fields are `NaN`.

        Reference: https://cyberbotics.com/doc/reference/compass?tab-language=python#wb_compass_get_values
        """

    def getLookupTable(self) -> list[float]:
        """Return the lookup table of the device as a flat list of N * 3 numbers (N rows of 3 values).

        Reference: https://cyberbotics.com/doc/reference/compass?tab-language=python#wb_compass_get_lookup_table
        """

    @property
    def value(self) -> list[float]:
        """The latest measurement `[x, y, z]` pointing to the north (same as `getValues()`)."""

    @property
    def lookup_table(self) -> list[float]:
        """The lookup table as a flat list of N * 3 numbers (same as `getLookupTable()`)."""
