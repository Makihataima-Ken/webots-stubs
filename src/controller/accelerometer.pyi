from .sensor import Sensor

class Accelerometer(Sensor):
    """An accelerometer measuring acceleration, including gravity induced reaction forces, along 1 to 3 axes.

    Values are in meters per second squared [m/s²]. The parent node should have a Physics node
    for the measurements to be meaningful. Enable the device with `enable()` before reading it.

    Reference: https://cyberbotics.com/doc/reference/accelerometer?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getValues(self) -> list[float]:
        """Return the latest measurement as `[x, y, z]` [m/s²].

        Axes disabled with the `xAxis`, `yAxis` and `zAxis` fields are `NaN`.

        Reference: https://cyberbotics.com/doc/reference/accelerometer?tab-language=python#wb_accelerometer_get_values
        """

    def getLookupTable(self) -> list[float]:
        """Return the lookup table of the device as a flat list of N * 3 numbers (N rows of 3 values).

        Reference: https://cyberbotics.com/doc/reference/accelerometer?tab-language=python#wb_accelerometer_get_lookup_table
        """

    @property
    def lookup_table(self) -> list[float]:
        """The lookup table as a flat list of N * 3 numbers (same as `getLookupTable()`)."""

    @property
    def value(self) -> list[float]:
        """The latest measurement `[x, y, z]` [m/s²] (same as `getValues()`)."""
