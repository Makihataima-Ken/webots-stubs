from typing import Final

from typing_extensions import Never

from .device import Device
from .motor import Motor
from .position_sensor import PositionSensor

class Brake(Device):
    """A brake that adds friction to a joint (Brake node in the `device` field of a joint or track).

    Reference: https://cyberbotics.com/doc/reference/brake?tab-language=python
    """

    ROTATIONAL: Final[int]
    """Brake type of a brake on a rotational joint (see `getType()`)."""
    LINEAR: Final[int]
    """Brake type of a brake on a linear joint or a track (see `getType()`)."""

    def __init__(self, name: str | int) -> None: ...
    def setDampingConstant(self, c: float) -> None:
        """Set the damping constant of the joint [N⋅s/m or N⋅m⋅s].

        It adds up to any damping constant set in the joint's `JointParameters`.

        Reference: https://cyberbotics.com/doc/reference/brake?tab-language=python#wb_brake_set_damping_constant
        """

    def getType(self) -> int:
        """Return the brake type: `Brake.ROTATIONAL` or `Brake.LINEAR`.

        Reference: https://cyberbotics.com/doc/reference/brake?tab-language=python#wb_brake_get_type
        """

    def getMotor(self) -> Motor | None:
        """Return the Motor device of the same joint, or `None` if the joint has none.

        Reference: https://cyberbotics.com/doc/reference/brake?tab-language=python#wb_brake_get_motor
        """

    def getPositionSensor(self) -> PositionSensor | None:
        """Return the PositionSensor device of the same joint, or `None` if the joint has none.

        Reference: https://cyberbotics.com/doc/reference/brake?tab-language=python#wb_brake_get_position_sensor
        """

    @property
    def dampingConstant(self) -> Never:
        """Write-only: setting it sets the damping constant of the joint (same as `setDampingConstant()`)."""

    @dampingConstant.setter
    def dampingConstant(self, c: float) -> None: ...
    @property
    def motor(self) -> Motor | None:
        """The Motor device of the same joint, if any (same as `getMotor()`)."""

    @property
    def position_sensor(self) -> PositionSensor | None:
        """The PositionSensor device of the same joint, if any (same as `getPositionSensor()`)."""

    @property
    def type(self) -> int:
        """The brake type, `Brake.ROTATIONAL` or `Brake.LINEAR` (same as `getType()`)."""
