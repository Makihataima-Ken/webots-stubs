from .sensor import Sensor

class Gyro(Sensor):
    """A gyroscope measuring angular velocities about 1 to 3 axes, in radians per second [rad/s].

    Enable the device with `enable()` before reading it.

    Reference: https://cyberbotics.com/doc/reference/gyro?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getValues(self) -> list[float]:
        """Return the latest measurement as `[x, y, z]` angular velocities about the device's axes [rad/s].

        Axes disabled with the `xAxis`, `yAxis` and `zAxis` fields are `NaN`.

        Reference: https://cyberbotics.com/doc/reference/gyro?tab-language=python#wb_gyro_get_values
        """

    def getLookupTable(self) -> list[float]:
        """Return the lookup table of the device as a flat list of N * 3 numbers (N rows of 3 values).

        Reference: https://cyberbotics.com/doc/reference/gyro?tab-language=python#wb_gyro_get_lookup_table
        """

    @property
    def lookup_table(self) -> list[float]:
        """The lookup table as a flat list of N * 3 numbers (same as `getLookupTable()`)."""

    @property
    def value(self) -> list[float]:
        """The latest measurement `[x, y, z]` [rad/s] (same as `getValues()`)."""
