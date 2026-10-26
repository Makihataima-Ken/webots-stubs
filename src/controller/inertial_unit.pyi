from .sensor import Sensor

class InertialUnit(Sensor):
    """An inertial unit measuring its orientation with respect to the world's reference frame.

    Angles are in radians [rad]. Enable the device with `enable()` before reading it.

    Reference: https://cyberbotics.com/doc/reference/inertialunit?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getRollPitchYaw(self) -> list[float]:
        """Return the latest orientation as `[roll, pitch, yaw]` [rad].

        Angles of axes disabled with the `xAxis`, `yAxis` and `zAxis` fields are `NaN`. Use
        `getQuaternion()` to avoid gimbal lock.

        Reference: https://cyberbotics.com/doc/reference/inertialunit?tab-language=python#wb_inertial_unit_get_roll_pitch_yaw
        """

    def getQuaternion(self) -> list[float]:
        """Return the latest orientation as a quaternion `[x, y, z, w]`.

        Reference: https://cyberbotics.com/doc/reference/inertialunit?tab-language=python#wb_inertial_unit_get_quaternion
        """

    def getNoise(self) -> float:
        """Return the value of the `noise` field of the device.

        Reference: https://cyberbotics.com/doc/reference/inertialunit?tab-language=python#wb_inertial_unit_get_noise
        """

    @property
    def roll_pitch_yaw(self) -> list[float]:
        """The latest orientation `[roll, pitch, yaw]` [rad] (same as `getRollPitchYaw()`)."""

    @property
    def quaternion(self) -> list[float]:
        """The latest orientation as a quaternion `[x, y, z, w]` (same as `getQuaternion()`)."""

    @property
    def noise(self) -> float:
        """The value of the `noise` field of the device (same as `getNoise()`)."""
