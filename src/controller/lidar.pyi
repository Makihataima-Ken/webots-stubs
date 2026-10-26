import ctypes
from ctypes import _Pointer  # pyright: ignore[reportPrivateUsage]

from .lidar_point import LidarPoint
from .sensor import Sensor

class Lidar(Sensor):
    """Laser range scanner with one or more layers, delivering a range image and optionally a point cloud.

    Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getFov(self) -> float:
        """Return the horizontal field of view of the lidar [rad].

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_fov
        """

    def getVerticalFov(self) -> float:
        """Return the vertical field of view of the lidar [rad].

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_vertical_fov
        """

    def getMaxFrequency(self) -> float:
        """Return the maximum rotating frequency of the lidar head [Hz] (rotating lidars).

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_max_frequency
        """

    def getMinFrequency(self) -> float:
        """Return the minimum rotating frequency of the lidar head [Hz] (rotating lidars).

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_min_frequency
        """

    def getMaxRange(self) -> float:
        """Return the maximum range of the lidar [m].

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_max_range
        """

    def getMinRange(self) -> float:
        """Return the minimum range of the lidar [m].

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_min_range
        """

    def getHorizontalResolution(self) -> int:
        """Return the number of points per layer.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_horizontal_resolution
        """

    def getNumberOfLayers(self) -> int:
        """Return the number of layers (lasers).

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_number_of_layers
        """

    def getFrequency(self) -> float:
        """Return the current rotating frequency of the lidar head [Hz] (rotating lidars).

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_frequency
        """

    def setFrequency(self, frequency: float) -> None:
        """Set the rotating frequency of the lidar head [Hz], within `[minFrequency, maxFrequency]`.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_set_frequency
        """

    def getNumberOfPoints(self) -> int:
        """Return the total number of points of the point cloud, all layers included.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_number_of_points
        """

    def getRangeImage(self) -> list[float]:
        """Return the last range image as a flat list of depths [m], layer after layer.

        Depths outside `[minRange, maxRange]` are infinite. Do not call it if the point cloud was
        enabled during the last step.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_range_image
        """

    def getRangeImageArray(self) -> list[list[float]]:
        """Return the last range image as one list of depths [m] per layer.

        In R2025a this repeats layer 0 for every row, because `getLayerRangeImage()` ignores its argument.
        To get each layer, slice `getRangeImage()` by `horizontal_resolution` instead.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_range_image
        """

    def getLayerRangeImage(self, layer: int) -> list[float]:
        """Return the depths [m] of layer 0 of the range image, as a list of `getHorizontalResolution()` values.

        In R2025a the `layer` argument is ignored and layer 0 is always returned. To get another layer, slice
        `getRangeImage()`: `[layer * horizontal_resolution:(layer + 1) * horizontal_resolution]`.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_layer_range_image
        """

    @property
    def range_image(self) -> _Pointer[ctypes.c_float]:
        """The native buffer of the last range image, `horizontal_resolution * number_of_layers` floats [m]."""

    @property
    def fov(self) -> float:
        """The horizontal field of view [rad] (same as `getFov()`)."""

    @property
    def vertical_fov(self) -> float:
        """The vertical field of view [rad] (same as `getVerticalFov()`)."""

    @property
    def max_frequency(self) -> float:
        """The maximum rotating frequency [Hz] (same as `getMaxFrequency()`)."""

    @property
    def min_frequency(self) -> float:
        """The minimum rotating frequency [Hz] (same as `getMinFrequency()`)."""

    @property
    def max_range(self) -> float:
        """The maximum range [m] (same as `getMaxRange()`)."""

    @property
    def min_range(self) -> float:
        """The minimum range [m] (same as `getMinRange()`)."""

    @property
    def horizontal_resolution(self) -> int:
        """The number of points per layer (same as `getHorizontalResolution()`)."""

    @property
    def number_of_layers(self) -> int:
        """The number of layers (same as `getNumberOfLayers()`)."""

    @property
    def frequency(self) -> float:
        """The rotating frequency of the head [Hz] (same as `getFrequency()` / `setFrequency()`)."""

    @frequency.setter
    def frequency(self, frequency: float) -> None: ...
    @property
    def number_of_points(self) -> int:
        """The total number of points of the point cloud (same as `getNumberOfPoints()`)."""

    def disablePointCloud(self) -> None:
        """Disable the point cloud update.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_disable_point_cloud
        """

    def enablePointCloud(self) -> None:
        """Enable the point cloud update, with the sampling period of the range image.

        The lidar itself must also be enabled with `enable()`.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_enable_point_cloud
        """

    def isPointCloudEnabled(self) -> bool:
        """Return whether the point cloud update is enabled.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_is_point_cloud_enabled
        """

    def getPointCloud(self) -> list[LidarPoint]:
        """Return the points of the last point cloud, all layers included.

        Only valid if the point cloud was enabled during the last step.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_point_cloud
        """

    def getLayerPointCloud(self, layer: int) -> list[LidarPoint]:
        """Return the points of one layer of the last point cloud.

        Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wb_lidar_get_layer_point_cloud
        """
