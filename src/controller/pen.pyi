from .device import Device

class Pen(Device):
    """A pen that draws ink on the objects below it while it is writing.

    Reference: https://cyberbotics.com/doc/reference/pen?tab-language=python
    """

    def __init__(self, name: str | int) -> None: ...
    def write(self, write: bool) -> None:
        """Switch writing on (`True`) or off (`False`).

        Reference: https://cyberbotics.com/doc/reference/pen?tab-language=python#wb_pen_write
        """

    def setInkColor(self, color: int, density: float) -> None:
        """Set the ink `color` (0xRRGGBB) and `density`, from 0.0 (transparent) to 1.0 (opaque).

        Reference: https://cyberbotics.com/doc/reference/pen?tab-language=python#wb_pen_set_ink_color
        """
