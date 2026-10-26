import ctypes
from collections.abc import Sequence
from ctypes import _Pointer  # pyright: ignore[reportPrivateUsage]
from typing import Literal, overload

from .sensor import Sensor

class RangeFinder(Sensor):
    """Depth camera: measures the distance [m] from the device to the objects in front of it.

    Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getFov(self) -> float:
        """Return the horizontal field of view of the range-finder [rad].

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_get_fov
        """

    def getWidth(self) -> int:
        """Return the width of the range image [pixels].

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_get_width
        """

    def getHeight(self) -> int:
        """Return the height of the range image [pixels].

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_get_height
        """

    def getMaxRange(self) -> float:
        """Return the maximum range of the range-finder [m].

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_get_max_range
        """

    def getMinRange(self) -> float:
        """Return the minimum range of the range-finder [m].

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_get_min_range
        """

    @overload
    def getRangeImage(self, data_type: Literal["list"] = "list") -> list[float]:
        """Return the last range image as a flat list of `width * height` depths [m], row by row from the top left.

        Depths outside `[minRange, maxRange]` are infinite. With `data_type="buffer"`, the
        function instead returns the native ctypes buffer of floats without copying: faster, but only valid
        until the next step and not bounds-checked.

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_get_range_image
        """

    @overload
    def getRangeImage(self, data_type: Literal["buffer"]) -> _Pointer[ctypes.c_float]:
        """Return the native ctypes buffer of the last range image: `width * height` floats [m], not copied."""

    def getRangeImageArray(self) -> list[list[float]]:
        """Return the last range image as `height` rows of `width` depths [m].

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_get_range_image
        """

    @staticmethod
    def rangeImageGetDepth(image: _Pointer[ctypes.c_float] | Sequence[float], width: int, x: int, y: int) -> float:
        """Return the depth [m] of pixel (`x`, `y`) of a range image obtained from `getRangeImage()`.

        `width` is the image width, from `getWidth()`.

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_image_get_depth
        """

    def saveImage(self, filename: str, quality: int) -> int:
        """Save the last range image to `filename` as PNG, JPEG or HDR, according to its extension.

        `quality` (1 to 100) only applies to JPEG. Return 0 on success, -1 on failure.

        Reference: https://cyberbotics.com/doc/reference/rangefinder?tab-language=python#wb_range_finder_save_image
        """

    @property
    def range_image(self) -> _Pointer[ctypes.c_float]:
        """The native buffer of the last range image, `width * height` floats [m] (like `getRangeImage("buffer")`)."""

    @property
    def fov(self) -> float:
        """The horizontal field of view [rad] (same as `getFov()`)."""

    @property
    def width(self) -> int:
        """The width of the range image [pixels] (same as `getWidth()`)."""

    @property
    def height(self) -> int:
        """The height of the range image [pixels] (same as `getHeight()`)."""

    @property
    def max_range(self) -> float:
        """The maximum range [m] (same as `getMaxRange()`)."""

    @property
    def min_range(self) -> float:
        """The minimum range [m] (same as `getMinRange()`)."""
