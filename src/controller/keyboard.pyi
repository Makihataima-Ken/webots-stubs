from typing import Final

class Keyboard:
    """The computer keyboard, read while the 3D window of Webots is selected and the simulation is running.

    Key codes are the ASCII codes of the keys or one of the special values below, possibly
    combined with a modifier (`SHIFT`, `CONTROL`, `ALT`) using a binary OR.

    Reference: https://cyberbotics.com/doc/reference/keyboard?tab-language=python
    """

    END: Final[int]
    """Key code of the End key."""
    HOME: Final[int]
    """Key code of the Home key."""
    LEFT: Final[int]
    """Key code of the left arrow key."""
    UP: Final[int]
    """Key code of the up arrow key."""
    RIGHT: Final[int]
    """Key code of the right arrow key."""
    DOWN: Final[int]
    """Key code of the down arrow key."""
    PAGEUP: Final[int]
    """Key code of the Page Up key."""
    PAGEDOWN: Final[int]
    """Key code of the Page Down key."""
    NUMPAD_HOME: Final[int]
    """Key code of the Home key of the numeric keypad."""
    NUMPAD_LEFT: Final[int]
    """Key code of the left arrow key of the numeric keypad."""
    NUMPAD_UP: Final[int]
    """Key code of the up arrow key of the numeric keypad."""
    NUMPAD_RIGHT: Final[int]
    """Key code of the right arrow key of the numeric keypad."""
    NUMPAD_DOWN: Final[int]
    """Key code of the down arrow key of the numeric keypad."""
    NUMPAD_END: Final[int]
    """Key code of the End key of the numeric keypad."""
    KEY: Final[int]
    """Mask that extracts the key code from a value that includes modifiers (`getKey() & Keyboard.KEY`)."""
    SHIFT: Final[int]
    """Modifier flag set in the key code while Shift is pressed."""
    CONTROL: Final[int]
    """Modifier flag set in the key code while Control is pressed."""
    ALT: Final[int]
    """Modifier flag set in the key code while Alt is pressed."""

    def __init__(self, sampling_period: int | None = None) -> None:
        """Enable the keyboard with `sampling_period` milliseconds, or else the world's basic time step.

        Pass 0 to leave the keyboard disabled.
        """

    def enable(self, p: int) -> None:
        """Enable keyboard input, with a new reading every `p` milliseconds of simulated time.

        The first key is available after the first sampling period. You may have to click in the 3D window first.

        Reference: https://cyberbotics.com/doc/reference/keyboard?tab-language=python#wb_keyboard_enable
        """

    def disable(self) -> None:
        """Stop reading the keyboard.

        Reference: https://cyberbotics.com/doc/reference/keyboard?tab-language=python#wb_keyboard_disable
        """

    def getSamplingPeriod(self) -> int:
        """Return the sampling period given to `enable()` [ms], or 0 if the keyboard is disabled.

        Reference: https://cyberbotics.com/doc/reference/keyboard?tab-language=python#wb_keyboard_get_sampling_period
        """

    @property
    def sampling_period(self) -> int:
        """Sampling period of the keyboard [ms], 0 when disabled. Setting it enables it; `None` disables it."""

    @sampling_period.setter
    def sampling_period(self, p: int | None) -> None: ...
    def getKeyCode(self) -> int:
        """Return the code of a key currently pressed, or -1 if none is (same as `getKey()`).

        Reference: https://cyberbotics.com/doc/reference/keyboard?tab-language=python#wb_keyboard_get_key
        """

    def getKey(self) -> int:
        """Return the code of a key currently pressed, or -1 if none is.

        With modifiers pressed the code is a binary OR of `SHIFT`, `CONTROL` or `ALT` and the key;
        use `& Keyboard.KEY` to get the key alone. Call it repeatedly until it returns -1 to read
        up to 7 simultaneous keys.

        Reference: https://cyberbotics.com/doc/reference/keyboard?tab-language=python#wb_keyboard_get_key
        """

    def get_key(self) -> str:
        """Return a readable name of the key currently pressed, such as "shift-up" or "a".

        The Alt modifier prefix is spelled "atl-" (upstream typo), e.g. "atl-a".

        Raises `ValueError` when no key is pressed.
        """
