from .sensor import Sensor

class Altimeter(Sensor):
    """A sensor measuring its altitude above the zero level of the world, in meters [m].

    Enable the device with `enable()` before reading it.

    Reference: https://cyberbotics.com/doc/reference/altimeter?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getValue(self) -> float:
        """Return the latest altitude measurement [m].

        Reference: https://cyberbotics.com/doc/reference/altimeter?tab-language=python#wb_altimeter_get_value
        """

    @property
    def value(self) -> float:
        """The latest altitude measurement [m] (same as `getValue()`)."""
