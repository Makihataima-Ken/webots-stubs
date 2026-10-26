from ctypes import _Pointer, c_double  # pyright: ignore[reportPrivateUsage]

from .sensor import Sensor

class LightSensor(Sensor):
    """A sensor measuring the irradiance of the light it receives.

    The measurements are mapped through the `lookupTable` field of the node, which therefore
    defines the unit and range of the values. Enable the device with `enable()` before reading it.

    Reference: https://cyberbotics.com/doc/reference/lightsensor?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getLookupTable(self) -> list[float]:
        """Return the lookup table of the sensor as a flat list of N * 3 numbers (N rows of 3 values).

        Reference: https://cyberbotics.com/doc/reference/lightsensor?tab-language=python#wb_light_sensor_get_lookup_table
        """

    def getValue(self) -> float:
        """Return the latest measurement, as mapped by the lookup table of the sensor.

        Reference: https://cyberbotics.com/doc/reference/lightsensor?tab-language=python#wb_light_sensor_get_value
        """

    @property
    def lookup_table(self) -> _Pointer[c_double]:
        """The lookup table as a raw ctypes array of N * 3 numbers, N being the number of rows.

        Unlike `getLookupTable()`, this is not a list and its length is not bounded.
        """

    @property
    def value(self) -> float:
        """The latest measurement, as mapped by the lookup table (same as `getValue()`)."""
