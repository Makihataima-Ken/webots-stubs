class MouseState:
    """A snapshot of the computer mouse, as returned by `Mouse.getState()`.

    Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python#wbmousestate
    """

    u: float
    """Horizontal position of the pointer in the 3D window, 0 (left border) to 1 (right border), `NaN` if outside."""
    v: float
    """Vertical position of the pointer in the 3D window, 0 (top border) to 1 (bottom border), `NaN` if outside."""
    x: float
    """X coordinate [m] of the 3D point under the pointer, `NaN` unless the 3D position is enabled."""
    y: float
    """Y coordinate [m] of the 3D point under the pointer, `NaN` unless the 3D position is enabled."""
    z: float
    """Z coordinate [m] of the 3D point under the pointer, `NaN` unless the 3D position is enabled."""
    left: bool
    """Whether the left button is pressed."""
    middle: bool
    """Whether the middle button is pressed."""
    right: bool
    """Whether the right button is pressed."""

    def __init__(
        self, u: float, v: float, x: float, y: float, z: float, left: bool, middle: bool, right: bool
    ) -> None: ...

class Mouse:
    """The computer mouse, read while the simulation is running.

    Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python
    """

    def __init__(self, sampling_period: int | None = None) -> None:
        """Enable the mouse with `sampling_period` milliseconds, or else the world's basic time step.

        Pass 0 to leave the mouse disabled.
        """

    def enable(self, p: int) -> None:
        """Enable mouse input, with a new state every `p` milliseconds of simulated time.

        The first state is available after the first sampling period.

        Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python#wb_mouse_enable
        """

    def disable(self) -> None:
        """Stop reading the mouse.

        Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python#wb_mouse_disable
        """

    def getSamplingPeriod(self) -> int:
        """Return the sampling period given to `enable()` [ms], or 0 if the mouse is disabled.

        Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python#wb_mouse_get_sampling_period
        """

    def getState(self) -> MouseState:
        """Return the current state of the mouse: pointer position, 3D position and buttons.

        Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python#wb_mouse_get_state
        """

    def enable3dPosition(self) -> None:
        """Enable the computation of the 3D point under the pointer (`x`, `y`, `z` of the state).

        It can slow down the simulation noticeably in complex scenes.

        Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python#wb_mouse_enable_3d_position
        """

    def disable3dPosition(self) -> None:
        """Disable the computation of the 3D point under the pointer.

        Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python#wb_mouse_disable_3d_position
        """

    def is3dPositionEnabled(self) -> bool:
        """Return whether the 3D position of the pointer is being computed.

        Reference: https://cyberbotics.com/doc/reference/mouse?tab-language=python#wb_mouse_is_3d_position_enabled
        """

    @property
    def sampling_period(self) -> int:
        """Sampling period of the mouse [ms], 0 when disabled. Setting it enables the mouse; `None` disables it."""

    @sampling_period.setter
    def sampling_period(self, p: int | None) -> None: ...
