from .radar_target import RadarTarget
from .sensor import Sensor

class Radar(Sensor):
    """A radar that detects targets within its field of view.

    Reference: https://cyberbotics.com/doc/reference/radar?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getMaxRange(self) -> float:
        """Return the maximum range of the radar [m].

        Reference: https://cyberbotics.com/doc/reference/radar?tab-language=python#wb_radar_get_max_range
        """

    def getMinRange(self) -> float:
        """Return the minimum range of the radar [m].

        Reference: https://cyberbotics.com/doc/reference/radar?tab-language=python#wb_radar_get_min_range
        """

    def getHorizontalFov(self) -> float:
        """Return the horizontal field of view of the radar [rad].

        Reference: https://cyberbotics.com/doc/reference/radar?tab-language=python#wb_radar_get_horizontal_fov
        """

    def getVerticalFov(self) -> float:
        """Return the vertical field of view of the radar [rad].

        Reference: https://cyberbotics.com/doc/reference/radar?tab-language=python#wb_radar_get_vertical_fov
        """

    def getNumberOfTargets(self) -> int:
        """Return the number of targets currently seen by the radar.

        Reference: https://cyberbotics.com/doc/reference/radar?tab-language=python#wb_radar_get_number_of_targets
        """

    def getTargets(self) -> list[RadarTarget]:
        """Return the targets currently seen by the radar, as new `RadarTarget` objects.

        Reference: https://cyberbotics.com/doc/reference/radar?tab-language=python#wb_radar_get_targets
        """

    @property
    def max_range(self) -> float:
        """The maximum range of the radar [m] (same as `getMaxRange()`)."""

    @property
    def min_range(self) -> float:
        """The minimum range of the radar [m] (same as `getMinRange()`)."""

    @property
    def horizontal_fov(self) -> float:
        """The horizontal field of view of the radar [rad] (same as `getHorizontalFov()`)."""

    @property
    def vertical_fov(self) -> float:
        """The vertical field of view of the radar [rad] (same as `getVerticalFov()`)."""

    @property
    def number_of_targets(self) -> int:
        """The number of targets currently seen by the radar (same as `getNumberOfTargets()`)."""
