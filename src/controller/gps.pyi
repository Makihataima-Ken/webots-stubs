from typing import Final

from .sensor import Sensor

class GPS(Sensor):
    """A global positioning sensor giving the absolute position and speed of the device.

    Positions are Cartesian coordinates [m] in the frame of Webots or latitude, longitude and altitude,
    depending on the `gpsCoordinateSystem` field of the WorldInfo node. Enable the device with
    `enable()` before reading it.

    Reference: https://cyberbotics.com/doc/reference/gps?tab-language=python
    """

    LOCAL: Final = 0
    """Coordinate system of a `gpsCoordinateSystem` set to "local" (see `getCoordinateSystem()`)."""
    WGS84: Final = 1
    """Coordinate system of a `gpsCoordinateSystem` set to "WGS84" (see `getCoordinateSystem()`)."""

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getCoordinateSystem(self) -> int:
        """Return the coordinate system of the measurements: `GPS.LOCAL` or `GPS.WGS84`.

        Reference: https://cyberbotics.com/doc/reference/gps?tab-language=python#wb_gps_get_coordinate_system
        """

    @property
    def coordinate_system(self) -> int:
        """The coordinate system of the measurements, `GPS.LOCAL` or `GPS.WGS84` (same as `getCoordinateSystem()`)."""

    @staticmethod
    def convertToDegreesMinutesSeconds(decimalDegrees: float) -> str:
        """Convert a coordinate in decimal degrees to a "degrees minutes seconds" string.

        The string contains the symbols for degrees, minutes and seconds, so the console must support UTF-8.
        Upstream bug: only the degrees are reliable, the minutes are always 0 and the seconds are wrong
        (a multiple of 60), so do not rely on the result for anything but the whole degrees.

        Reference: https://cyberbotics.com/doc/reference/gps?tab-language=python#wb_gps_convert_to_degrees_minutes_seconds
        """

    def getSpeed(self) -> float:
        """Return the current speed of the device [m/s].

        Reference: https://cyberbotics.com/doc/reference/gps?tab-language=python#wb_gps_get_speed
        """

    @property
    def speed(self) -> float:
        """The current speed of the device [m/s] (same as `getSpeed()`)."""

    def getSpeedVector(self) -> list[float]:
        """Return the current velocity of the device as `[x, y, z]` [m/s].

        Reference: https://cyberbotics.com/doc/reference/gps?tab-language=python#wb_gps_get_speed_vector
        """

    @property
    def speed_vector(self) -> list[float]:
        """The current velocity `[x, y, z]` of the device [m/s] (same as `getSpeedVector()`)."""

    def getValues(self) -> list[float]:
        """Return the current position as `[x, y, z]` [m], or `[latitude, longitude, altitude]` with `GPS.WGS84`.

        Latitude and longitude are in degrees [deg], the altitude in meters [m].

        Reference: https://cyberbotics.com/doc/reference/gps?tab-language=python#wb_gps_get_values
        """

    @property
    def value(self) -> list[float]:
        """The current position of the device, 3 numbers (same as `getValues()`)."""
