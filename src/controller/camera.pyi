import ctypes
from collections.abc import Sequence
from ctypes import _Pointer  # pyright: ignore[reportPrivateUsage]

from .sensor import Sensor

class CameraRecognitionObject(ctypes.Structure):
    """An object recognized by a camera, with its pose and size relative to the camera.

    Instances are only valid until the next simulation step; copy what you need.

    Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#camera-recognition-object
    """

    id: int
    """Id of the recognized node, usable with `Supervisor.getFromId()`."""
    position: ctypes.Array[ctypes.c_double]
    """Position (x, y, z) of the object center relative to the camera [m]."""
    orientation: ctypes.Array[ctypes.c_double]
    """Orientation of the object relative to the camera, as an axis-angle (x, y, z, angle [rad])."""
    size: ctypes.Array[ctypes.c_double]
    """Size (y, z) of the object relative to the camera [m]."""
    position_on_image: ctypes.Array[ctypes.c_int]
    """Position (x, y) of the object center in the camera image [pixels]."""
    size_on_image: ctypes.Array[ctypes.c_int]
    """Size (width, height) of the object bounding box in the camera image [pixels]."""
    number_of_colors: int
    """Number of colors of the object."""
    colors: _Pointer[ctypes.c_double]
    """The colors of the object, as `3 * number_of_colors` doubles (R, G, B for each color)."""

    def getId(self) -> int:
        """Return the id of the recognized node (same as `id`)."""

    def getPosition(self) -> ctypes.Array[ctypes.c_double]:
        """Return the position (x, y, z) of the object relative to the camera [m]."""

    def getOrientation(self) -> ctypes.Array[ctypes.c_double]:
        """Return the orientation of the object relative to the camera, as an axis-angle (x, y, z, angle [rad])."""

    def getSize(self) -> ctypes.Array[ctypes.c_double]:
        """Return the size (y, z) of the object relative to the camera [m]."""

    def getPositionOnImage(self) -> ctypes.Array[ctypes.c_int]:
        """Return the position (x, y) of the object center in the camera image [pixels]."""

    def getSizeOnImage(self) -> ctypes.Array[ctypes.c_int]:
        """Return the size (width, height) of the object bounding box in the camera image [pixels]."""

    def getNumberOfColors(self) -> int:
        """Return the number of colors of the object."""

    def getColors(self) -> _Pointer[ctypes.c_double]:
        """Return the colors of the object, as `3 * getNumberOfColors()` doubles (R, G, B for each color)."""

    def getModel(self) -> str:
        """Return the `model` field of the recognized `Solid` node."""

    @property
    def model(self) -> str:
        """The `model` field of the recognized `Solid` node (same as `getModel()`)."""

class Camera(Sensor):
    """Color camera, optionally with object recognition and segmentation.

    Images are in BGRA order, 4 bytes per pixel, row by row from the top left.

    Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getExposure(self) -> float:
        """Return the exposure of the camera.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_exposure
        """

    def getFocalDistance(self) -> float:
        """Return the current focal distance [m], or 0 if the camera has no `Focus` node.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_focal_distance
        """

    def getFocalLength(self) -> float:
        """Return the focal length [m], or 0 if the camera has no `Focus` node.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_focal_length
        """

    def getFov(self) -> float:
        """Return the current horizontal field of view [rad].

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_fov
        """

    def getHeight(self) -> int:
        """Return the height of the camera image [pixels].

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_height
        """

    def getImage(self) -> bytes:
        """Return a copy of the last image as `4 * width * height` bytes in BGRA order.

        Pixels are stored row by row from the top left. Use `imageGetRed()` and friends to read a pixel.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_image
        """

    def getImageArray(self) -> list[list[list[int]]] | None:
        """Return the last image as `width` lists of `height` `[r, g, b]` pixels, or `None` if it is empty.

        In R2025a the lists are filled in order from the row-major buffer, not indexed `[x][y]` as documented: for a
        square image `array[a][b]` is the pixel at x=b, y=a (the image is transposed, i.e. indexed `[y][x]`), and
        for other shapes the pixels are scrambled. For reliable access, use `getImage()` with `imageGetRed()`,
        `imageGetGreen()` and `imageGetBlue()`.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_image
        """

    @staticmethod
    def imageGetRed(image: Sequence[int], width: int, x: int, y: int) -> int:
        """Return the red level (0 to 255) of pixel (`x`, `y`) of an image obtained from `getImage()`.

        `width` is the image width, from `getWidth()`.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_image_get_red
        """

    @staticmethod
    def imageGetGreen(image: Sequence[int], width: int, x: int, y: int) -> int:
        """Return the green level (0 to 255) of pixel (`x`, `y`) of an image obtained from `getImage()`.

        `width` is the image width, from `getWidth()`.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_image_get_green
        """

    @staticmethod
    def imageGetBlue(image: Sequence[int], width: int, x: int, y: int) -> int:
        """Return the blue level (0 to 255) of pixel (`x`, `y`) of an image obtained from `getImage()`.

        `width` is the image width, from `getWidth()`.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_image_get_blue
        """

    @staticmethod
    def imageGetGray(image: Sequence[int], width: int, x: int, y: int) -> float:
        """Return the gray level (mean of red, green and blue, 0 to 255) of pixel (`x`, `y`) of an image.

        `width` is the image width, from `getWidth()`.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_image_get_gray
        """

    def getMaxFocalDistance(self) -> float:
        """Return the maximum focal distance [m], or 0 if the camera has no `Focus` node.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_max_focal_distance
        """

    def getMaxFov(self) -> float:
        """Return the maximum field of view [rad]; without a `Zoom` node, the current field of view.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_max_fov
        """

    def getMinFocalDistance(self) -> float:
        """Return the minimum focal distance [m], or 0 if the camera has no `Focus` node.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_min_focal_distance
        """

    def getMinFov(self) -> float:
        """Return the minimum field of view [rad]; without a `Zoom` node, the current field of view.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_min_fov
        """

    def getNear(self) -> float:
        """Return the near clipping distance of the camera [m].

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_near
        """

    def getWidth(self) -> int:
        """Return the width of the camera image [pixels].

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_get_width
        """

    def saveImage(self, filename: str, quality: int) -> int:
        """Save the last image to `filename` as PNG or JPEG, according to its extension.

        `quality` (1 to 100) only applies to JPEG. Return 0 on success, -1 on failure.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_save_image
        """

    def setExposure(self, exposure: float) -> None:
        """Set the exposure of the camera.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_set_exposure
        """

    def setFocalDistance(self, d: float) -> None:
        """Set the focal distance [m]. The camera needs a `Focus` node.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_set_focal_distance
        """

    def setFov(self, f: float) -> None:
        """Set the horizontal field of view [rad]. The camera needs a `Zoom` node.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_set_fov
        """

    @property
    def image(self) -> bytes:
        """A copy of the last image, `4 * width * height` bytes in BGRA order (same as `getImage()`)."""

    @property
    def segmentation_image(self) -> bytes:
        """A copy of the last segmentation image, as `image` (same as `getRecognitionSegmentationImage()`)."""

    @property
    def exposure(self) -> float:
        """The exposure of the camera (same as `getExposure()` / `setExposure()`)."""

    @exposure.setter
    def exposure(self, exposure: float) -> None: ...
    @property
    def focal_distance(self) -> float:
        """The focal distance [m] (same as `getFocalDistance()` / `setFocalDistance()`)."""

    @focal_distance.setter
    def focal_distance(self, focal_distance: float) -> None: ...
    @property
    def focal_length(self) -> float:
        """The focal length [m] (same as `getFocalLength()`)."""

    @property
    def max_focal_distance(self) -> float:
        """The maximum focal distance [m] (same as `getMaxFocalDistance()`)."""

    @property
    def min_focal_distance(self) -> float:
        """The minimum focal distance [m] (same as `getMinFocalDistance()`)."""

    @property
    def fov(self) -> float:
        """The horizontal field of view [rad] (same as `getFov()` / `setFov()`)."""

    @fov.setter
    def fov(self, fov: float) -> None: ...
    @property
    def height(self) -> int:
        """The height of the camera image [pixels] (same as `getHeight()`)."""

    @property
    def min_fov(self) -> float:
        """The minimum field of view [rad] (same as `getMinFov()`)."""

    @property
    def max_fov(self) -> float:
        """The maximum field of view [rad] (same as `getMaxFov()`)."""

    @property
    def near(self) -> float:
        """The near clipping distance [m] (same as `getNear()`)."""

    @property
    def width(self) -> int:
        """The width of the camera image [pixels] (same as `getWidth()`)."""

    def getRecognitionNumberOfObjects(self) -> int:
        """Return the number of objects recognized in the last image.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_get_number_of_objects
        """

    def getRecognitionObjects(self) -> list[CameraRecognitionObject]:
        """Return the objects recognized in the last image.

        The objects are only valid until the next step; copy their data if you need it later.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_get_objects
        """

    def getRecognitionSamplingPeriod(self) -> int:
        """Return the recognition sampling period [ms], or 0 if recognition is disabled.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_get_sampling_period
        """

    def hasRecognition(self) -> bool:
        """Return whether the camera has a `Recognition` node.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_has_recognition
        """

    def recognitionDisable(self) -> None:
        """Disable object recognition, saving computation time.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_disable
        """

    def recognitionEnable(self, sampling_period: int) -> None:
        """Enable object recognition, with a new result every `sampling_period` milliseconds.

        The camera itself does not need to be enabled.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_enable
        """

    def disableRecognitionSegmentation(self) -> None:
        """Disable the generation of the segmentation image.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_disable_segmentation
        """

    def enableRecognitionSegmentation(self) -> None:
        """Enable the generation of the segmentation image. Recognition must be enabled first.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_enable_segmentation
        """

    def hasRecognitionSegmentation(self) -> bool:
        """Return whether the `Recognition` node has its `segmentation` field set to TRUE.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_has_segmentation
        """

    def isRecognitionSegmentationEnabled(self) -> bool:
        """Return whether the segmentation image is being generated.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python
        """

    def getRecognitionSegmentationImage(self) -> bytes:
        """Return a copy of the last segmentation image, in the same format as `getImage()`.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_get_segmentation_image
        """

    def getRecognitionSegmentationImageArray(self) -> list[list[list[int]]] | None:
        """Return the last segmentation image as `width` lists of `height` `[r, g, b]` pixels, or `None`.

        As with `getImageArray()`, R2025a fills the lists in order from the row-major buffer: a square image is
        transposed (indexed `[y][x]`) and other shapes are scrambled. For reliable access, use
        `getRecognitionSegmentationImage()` with `imageGetRed()`, `imageGetGreen()` and `imageGetBlue()`.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_get_segmentation_image
        """

    def saveRecognitionSegmentationImage(self, filename: str, quality: int) -> int:
        """Save the last segmentation image to `filename` as PNG or JPEG. Return 0 on success, -1 on failure.

        Reference: https://cyberbotics.com/doc/reference/camera?tab-language=python#wb_camera_recognition_save_segmentation_image
        """
