from typing import Final

from .brake import Brake
from .motor import Motor
from .sensor import Sensor

class PositionSensor(Sensor):
    """A sensor measuring the position of a joint, in radians [rad] or meters [m].

    Reference: https://cyberbotics.com/doc/reference/positionsensor?tab-language=python
    """

    ROTATIONAL: Final[int]
    """Sensor type of a sensor on a rotational joint (see `getType()`)."""
    LINEAR: Final[int]
    """Sensor type of a sensor on a linear joint or a track (see `getType()`)."""

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getValue(self) -> float:
        """Return the most recent position measured [rad or m].

        Reference: https://cyberbotics.com/doc/reference/positionsensor?tab-language=python#wb_position_sensor_get_value
        """

    def getType(self) -> int:
        """Return the sensor type: `PositionSensor.ROTATIONAL` or `PositionSensor.LINEAR`.

        Reference: https://cyberbotics.com/doc/reference/positionsensor?tab-language=python#wb_position_sensor_get_type
        """

    def getBrake(self) -> Brake | None:
        """Return the Brake device of the same joint, or `None` if the joint has none.

        Reference: https://cyberbotics.com/doc/reference/positionsensor?tab-language=python#wb_position_sensor_get_brake
        """

    def getMotor(self) -> Motor | None:
        """Return the Motor device of the same joint, or `None` if the joint has none.

        Note: in R2025a the Python implementation resolves it with `wb_brake_get_motor`, which may return
        the wrong result for a position sensor.

        Reference: https://cyberbotics.com/doc/reference/positionsensor?tab-language=python#wb_position_sensor_get_motor
        """

    @property
    def brake(self) -> Brake | None:
        """The Brake device of the same joint, if any (same as `getBrake()`)."""

    @property
    def motor(self) -> Motor | None:
        """The Motor device of the same joint, if any (same as `getMotor()`, see the note there)."""

    @property
    def value(self) -> float:
        """The most recent position measured [rad or m] (same as `getValue()`)."""

    @property
    def type(self) -> int:
        """The sensor type, `PositionSensor.ROTATIONAL` or `PositionSensor.LINEAR` (same as `getType()`)."""
