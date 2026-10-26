from .device import Device

class VacuumGripper(Device):
    """A suction pump that creates a physical link with the solid object it touches while on.

    Reference: https://cyberbotics.com/doc/reference/vacuumgripper?tab-language=python
    """

    def __init__(self, name: str | int) -> None: ...
    def enablePresence(self, sampling_period: int) -> None:
        """Start querying the presence of a linked object, every `sampling_period` milliseconds.

        The first measurement is available after the first sampling period has elapsed.

        Reference: https://cyberbotics.com/doc/reference/vacuumgripper?tab-language=python#wb_vacuum_gripper_enable_presence
        """

    def disablePresence(self) -> None:
        """Stop querying the presence of a linked object.

        Reference: https://cyberbotics.com/doc/reference/vacuumgripper?tab-language=python#wb_vacuum_gripper_disable_presence
        """

    def getPresenceSamplingPeriod(self) -> int:
        """Return the sampling period of the presence sensor [ms], or 0 if it is disabled.

        Reference: https://cyberbotics.com/doc/reference/vacuumgripper?tab-language=python#wb_vacuum_gripper_get_presence_sampling_period
        """

    def getPresence(self) -> bool:
        """Return whether a solid object is linked to the gripper.

        Reference: https://cyberbotics.com/doc/reference/vacuumgripper?tab-language=python#wb_vacuum_gripper_get_presence
        """

    def isOn(self) -> bool:
        """Return whether the suction pump is on (the `isOn` field).

        Reference: https://cyberbotics.com/doc/reference/vacuumgripper?tab-language=python#wb_vacuum_gripper_is_on
        """

    def turnOn(self) -> None:
        """Turn the suction pump on: a dynamic solid colliding with the gripper gets linked to it.

        Reference: https://cyberbotics.com/doc/reference/vacuumgripper?tab-language=python#wb_vacuum_gripper_turn_on
        """

    def turnOff(self) -> None:
        """Turn the suction pump off, destroying the current physical link if there is one.

        Reference: https://cyberbotics.com/doc/reference/vacuumgripper?tab-language=python#wb_vacuum_gripper_turn_off
        """

    @property
    def on(self) -> bool:
        """Whether the suction pump is on (same as `isOn()`)."""

    @property
    def presence(self) -> bool:
        """Whether a solid object is linked to the gripper (same as `getPresence()`)."""

    @property
    def presence_sampling_period(self) -> int:
        """Sampling period of the presence sensor [ms], 0 when disabled (same as `getPresenceSamplingPeriod()`)."""
