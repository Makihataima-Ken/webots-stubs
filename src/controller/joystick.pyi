class Joystick:
    """A joystick, gamepad or racing wheel paired with the controller, with optional force feedback.

    The Webots window must be selected and the simulation running for button presses to be reported.

    Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python
    """

    def __init__(self, sampling_period: int | None = None) -> None:
        """Enable the joystick with `sampling_period` milliseconds, or else the world's basic time step.

        Pass 0 to leave the joystick disabled.
        """

    def enable(self, p: int) -> None:
        """Enable the joystick, with a new reading every `p` milliseconds of simulated time.

        The first free joystick is paired with the controller and becomes active after the first sampling period.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_enable
        """

    def disable(self) -> None:
        """Disable the joystick and release it so that another controller can use it.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_disable
        """

    def getSamplingPeriod(self) -> int:
        """Return the sampling period given to `enable()` [ms], or 0 if the joystick is disabled.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_get_sampling_period
        """

    def isConnected(self) -> bool:
        """Return whether a free joystick has been paired with the controller since it was enabled.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_is_connected
        """

    def getNumberOfAxes(self) -> int:
        """Return the number of axes of the joystick.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_get_number_of_axes
        """

    def getAxisValue(self, axis: int) -> float:
        """Return the current value of the axis with index `axis`.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_get_axis_value
        """

    def getNumberOfPovs(self) -> int:
        """Return the number of points of view (POV, or hats) of the joystick.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_get_number_of_povs
        """

    def getPovValue(self, pov: int) -> int:
        """Return the current value of the point of view with index `pov`.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_get_pov_value
        """

    def getPressedButton(self) -> int:
        """Return the code of a button currently pressed, or -1 if none is.

        Call it repeatedly until it returns -1 to read several buttons pressed at the same time.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_get_pressed_button
        """

    def setConstantForce(self, level: int) -> None:
        """Apply a constant force feedback to the axis selected with `setForceAxis()` (hardware specific unit).

        The joystick must support force feedback. Try a small value first to avoid instabilities.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_set_constant_force
        """

    def setConstantForceDuration(self, duration: float) -> None:
        """Set for how long a force added with `setConstantForce()` is applied [s].

        The default is 1 second.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_set_constant_force_duration
        """

    def setAutoCenteringGain(self, gain: float) -> None:
        """Set the gain of the force feedback effect centering the axis on its zero position (hardware specific unit).

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_set_auto_centering_gain
        """

    def setResistanceGain(self, gain: float) -> None:
        """Set the gain of the force feedback effect that resists the movement of the axis (hardware specific unit).

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_set_resistance_gain
        """

    def setForceAxis(self, axis: int) -> None:
        """Select the axis the force feedback applies to.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_set_force_axis
        """

    @property
    def sampling_period(self) -> int:
        """Sampling period of the joystick [ms], 0 when disabled. Setting it enables it; `None` disables it."""

    @sampling_period.setter
    def sampling_period(self, p: int | None) -> None: ...
    @property
    def is_connected(self) -> bool:
        """Whether a joystick is paired with the controller (same as `isConnected()`)."""

    @property
    def model(self) -> str:
        """The model of the connected joystick, e.g. "Logitech G29 Driving Force Racing Wheel USB".

        Raises `AttributeError` when no joystick is connected.

        Reference: https://cyberbotics.com/doc/reference/joystick?tab-language=python#wb_joystick_get_model
        """

    @property
    def number_of_axes(self) -> int:
        """The number of axes of the joystick (same as `getNumberOfAxes()`)."""

    @property
    def number_of_povs(self) -> int:
        """The number of points of view of the joystick (same as `getNumberOfPovs()`)."""

    @property
    def pressed_button(self) -> int:
        """The code of a button currently pressed, -1 if none (same as `getPressedButton()`)."""
