from typing import Final

from typing_extensions import Never

from .camera import Camera
from .device import Device

class Display(Device):
    """A 2D drawing surface with a main image and a list of clipboard images.

    Coordinates are in pixels, with the origin at the top left. Colors are integers in 0xRRGGBB format.
    Clipboard images are referred to by an integer handle returned by `imageNew()`, `imageLoad()` or
    `imageCopy()`, to release with `imageDelete()`.

    Reference: https://cyberbotics.com/doc/reference/display?tab-language=python
    """

    RGB: Final = 3
    """Pixel format of image data: red, green, blue (see `imageNew()`)."""
    RGBA: Final = 4
    """Pixel format of image data: red, green, blue, alpha."""
    ARGB: Final = 5
    """Pixel format of image data: alpha, red, green, blue."""
    BGRA: Final = 6
    """Pixel format of image data: blue, green, red, alpha (the format of `Camera.getImage()`)."""
    ABGR: Final = 7
    """Pixel format of image data: alpha, blue, green, red."""

    def __init__(self, name: str | int) -> None: ...
    def attachCamera(self, camera: Camera) -> None:
        """Copy the images of `camera` to the background of the display, e.g. to draw over them.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_attach_camera
        """

    def detachCamera(self) -> None:
        """Detach the camera attached with `attachCamera()`.

        Pixels that were not drawn manually become transparent.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_detach_camera
        """

    def drawLine(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Draw a line from (`x1`, `y1`) to (`x2`, `y2`) [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_draw_line
        """

    def drawOval(self, cx: int, cy: int, a: int, b: int) -> None:
        """Draw the outline of an oval centered on (`cx`, `cy`) with radii `a` and `b` [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_draw_oval
        """

    def drawPixel(self, x: int, y: int) -> None:
        """Draw a pixel at (`x`, `y`).

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_draw_pixel
        """

    def drawPolygon(self, x: list[int], y: list[int]) -> None:
        """Draw the outline of the polygon whose vertices have the coordinates `x` and `y` [pixels].

        The shorter list sets the number of vertices. The loop is closed automatically.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_draw_polygon
        """

    def drawRectangle(self, x: int, y: int, width: int, height: int) -> None:
        """Draw the outline of a rectangle with its top left pixel at (`x`, `y`) [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_draw_rectangle
        """

    def drawText(self, text: str, x: int, y: int) -> None:
        """Draw an ASCII text with its top left corner at (`x`, `y`), using the font set by `setFont()`.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_draw_text
        """

    def fillOval(self, cx: int, cy: int, a: int, b: int) -> None:
        """Draw a filled oval centered on (`cx`, `cy`) with radii `a` and `b` [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_fill_oval
        """

    def fillPolygon(self, x: list[int], y: list[int]) -> None:
        """Draw a filled polygon whose vertices have the coordinates `x` and `y` [pixels].

        The shorter list sets the number of vertices.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_fill_polygon
        """

    def fillRectangle(self, x: int, y: int, width: int, height: int) -> None:
        """Draw a filled rectangle with its top left pixel at (`x`, `y`) [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_fill_rectangle
        """

    def getHeight(self) -> int:
        """Return the `height` field of the display [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_get_height
        """

    def getWidth(self) -> int:
        """Return the `width` field of the display [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_get_width
        """

    def imageCopy(self, x: int, y: int, width: int, height: int) -> int:
        """Copy a sub-image of the main display image to a new clipboard image and return its handle.

        The sub-image has its top left pixel at (`x`, `y`) [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_image_copy
        """

    def imageDelete(self, image: int) -> None:
        """Release the clipboard image `image`, which must not be used afterwards.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_image_delete
        """

    def imageNew(self, data: bytes, format: int, width: int, height: int) -> int:
        """Create a clipboard image from raw pixel `data` and return its handle.

        `format` is one of `Display.RGB`, `RGBA`, `ARGB`, `BGRA` (recommended) or `ABGR`.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_image_new
        """

    def imageLoad(self, filename: str) -> int:
        """Load a PNG or JPEG file (relative to the controller directory) into a new clipboard image.

        Return the handle of the new image.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_image_load
        """

    def imagePaste(self, image: int, x: int, y: int, blend: bool) -> None:
        """Paste the clipboard image `image` onto the main display image, with its top left at (`x`, `y`).

        Blending uses the alpha channels but is much slower than a plain copy.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_image_paste
        """

    def imageSave(self, image: int | None, filename: str) -> None:
        """Save the clipboard image `image` (or the main display image if `None`) to a PNG or JPEG file.

        The format follows the extension of `filename` (".png" or ".jpg").

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_image_save
        """

    def setAlpha(self, alpha: float) -> None:
        """Set the alpha channel of the drawing color, from 0.0 (transparent) to 1.0 (opaque).

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_set_alpha
        """

    def setColor(self, color: int) -> None:
        """Set the drawing color, in 0xRRGGBB format.

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_set_color
        """

    def setFont(self, font: str, size: int, anti_aliasing: bool) -> None:
        """Set the font used by `drawText()`, with its `size` [pixels].

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_set_font
        """

    def setOpacity(self, opacity: float) -> None:
        """Set the opacity of the drawing, from 0.0 (transparent) to 1.0 (opaque).

        Reference: https://cyberbotics.com/doc/reference/display?tab-language=python#wb_display_set_opacity
        """

    @property
    def alpha(self) -> Never:
        """Write-only: setting it sets the alpha channel of the drawing color (same as `setAlpha()`)."""

    @alpha.setter
    def alpha(self, alpha: float) -> None: ...
    @property
    def color(self) -> Never:
        """Write-only: setting it sets the drawing color in 0xRRGGBB format (same as `setColor()`)."""

    @color.setter
    def color(self, color: int) -> None: ...
    @property
    def opacity(self) -> Never:
        """Write-only: setting it sets the opacity of the drawing (same as `setOpacity()`)."""

    @opacity.setter
    def opacity(self, opacity: float) -> None: ...
    @property
    def width(self) -> int:
        """The width of the display [pixels] (same as `getWidth()`)."""

    @property
    def height(self) -> int:
        """The height of the display [pixels] (same as `getHeight()`)."""
