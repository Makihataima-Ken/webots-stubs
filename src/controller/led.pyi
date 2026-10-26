from .device import Device

class LED(Device):
    """A light-emitting diode that can be switched on and off, with its color or intensity.

    Reference: https://cyberbotics.com/doc/reference/led?tab-language=python
    """

    def __init__(self, name: str | int) -> None: ...
    def set(self, v: int) -> None:
        """Set the LED value: 0 is off. A bool is accepted and counts as 0 or 1.

        For a non-gradual LED, 1, 2, ... selects the first, second, ... color of the `color` field.
        For a monochromatic gradual LED, the value is the intensity from 0 to 255.
        For an RGB gradual LED, the value is a color from 0 to 0xFFFFFF in R8G8B8 format.

        Reference: https://cyberbotics.com/doc/reference/led?tab-language=python#wb_led_set
        """

    def get(self) -> int:
        """Return the value given to the last `set()` call.

        Reference: https://cyberbotics.com/doc/reference/led?tab-language=python#wb_led_get
        """

    @property
    def value(self) -> int:
        """The LED value (same as `get()` / `set()`)."""

    @value.setter
    def value(self, v: int) -> None: ...
