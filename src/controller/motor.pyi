from typing import Final

from typing_extensions import Never

from .brake import Brake
from .device import Device
from .position_sensor import PositionSensor

class Motor(Device):
    """A rotational or linear motor that powers a joint (RotationalMotor and LinearMotor nodes).

    Positions are in radians [rad] for rotational motors and meters [m] for linear
    motors; velocities and accelerations use the matching units ([rad/s], [m/s],
    [rad/s²], [m/s²]). Forces are in newtons [N] and torques in newton meters [N⋅m].

    Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python
    """

    ROTATIONAL: Final[int]
    """Motor type of a RotationalMotor node (see `getType()`)."""
    LINEAR: Final[int]
    """Motor type of a LinearMotor node (see `getType()`)."""

    def __init__(self, name: str | int) -> None: ...
    def setPosition(self, position: float) -> None:
        """Set the target position that the motor's PID controller moves the joint to [rad or m].

        The call returns immediately; the motion happens over the next simulation steps,
        using the current velocity, acceleration and available force/torque. Pass
        `float("inf")` for an endless motion, then control the speed with `setVelocity()`.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_position
        """

    def setVelocity(self, velocity: float) -> None:
        """Set the velocity the motor should reach while moving to its target position [rad/s or m/s].

        The value cannot exceed the `maxVelocity` field of the motor.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_velocity
        """

    def setAcceleration(self, acceleration: float) -> None:
        """Set the acceleration used by the PID controller to reach the velocity [rad/s² or m/s²].

        Pass -1 for an infinite acceleration.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_acceleration
        """

    def setAvailableForce(self, force: float) -> None:
        """Set the maximum force available to a linear motor to carry out the motion [N].

        The value cannot exceed the `maxForce` field of the motor.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_available_force
        """

    def setAvailableTorque(self, torque: float) -> None:
        """Set the maximum torque available to a rotational motor to carry out the motion [N⋅m].

        The value cannot exceed the `maxTorque` field of the motor.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_available_torque
        """

    def setControlPID(self, p: float, i: float, d: float) -> None:
        """Set the proportional, integral and derivative gains of the motor's PID controller.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_control_pid
        """

    def getTargetPosition(self) -> float:
        """Return the target position given to the last `setPosition()` call [rad or m].

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_target_position
        """

    def getMinPosition(self) -> float:
        """Return the `minPosition` field of the motor [rad or m].

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_min_position
        """

    def getMaxPosition(self) -> float:
        """Return the `maxPosition` field of the motor [rad or m].

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_max_position
        """

    def getVelocity(self) -> float:
        """Return the velocity given to the last `setVelocity()` call, or else `maxVelocity` [rad/s or m/s].

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_velocity
        """

    def getMaxVelocity(self) -> float:
        """Return the `maxVelocity` field of the motor [rad/s or m/s].

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_max_velocity
        """

    def getAcceleration(self) -> float:
        """Return the acceleration used by the PID controller [rad/s² or m/s²], -1 meaning infinite.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_acceleration
        """

    def getAvailableForce(self) -> float:
        """Return the force available to the motor [N], `maxForce` unless changed by `setAvailableForce()`.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_available_force
        """

    def getMaxForce(self) -> float:
        """Return the `maxForce` field of the motor [N].

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_max_force
        """

    def getAvailableTorque(self) -> float:
        """Return the torque available to the motor [N⋅m], `maxTorque` unless changed by `setAvailableTorque()`.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_available_torque
        """

    def getMaxTorque(self) -> float:
        """Return the `maxTorque` field of the motor [N⋅m].

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_max_torque
        """

    def getMultiplier(self) -> float:
        """Return the `multiplier` field of the motor (used by coupled motors).

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_multiplier
        """

    def enableForceFeedback(self, sampling_period: int) -> None:
        """Start measuring the force used by a linear motor, every `sampling_period` milliseconds.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_enable_force_feedback
        """

    def disableForceFeedback(self) -> None:
        """Stop the force measurements started by `enableForceFeedback()`.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_disable_force_feedback
        """

    def getForceFeedbackSamplingPeriod(self) -> int:
        """Return the sampling period of the force feedback [ms], or 0 if it is disabled.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_force_feedback_sampling_period
        """

    def getForceFeedback(self) -> float:
        """Return the latest measurement of the force used by the motor to move or hold its joint [N].

        Only the motor force along the joint's degree of freedom is measured: spring,
        damping and constraint forces are ignored. Requires a physics-based simulation.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_force_feedback
        """

    def enableTorqueFeedback(self, sampling_period: int) -> None:
        """Start measuring the torque used by a rotational motor, every `sampling_period` milliseconds.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_enable_torque_feedback
        """

    def disableTorqueFeedback(self) -> None:
        """Stop the torque measurements started by `enableTorqueFeedback()`.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_disable_torque_feedback
        """

    def getTorqueFeedbackSamplingPeriod(self) -> int:
        """Return the sampling period of the torque feedback [ms], or 0 if it is disabled.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_torque_feedback_sampling_period
        """

    def getTorqueFeedback(self) -> float:
        """Return the latest measurement of the torque used by the motor to move or hold its joint [N⋅m].

        Only the motor torque around the joint's axis is measured: spring, damping and
        constraint torques are ignored. Requires a physics-based simulation.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_torque_feedback
        """

    def setForce(self, force: float) -> None:
        """Apply a force along the axis of a linear motor directly, bypassing its PID controller [N].

        The value cannot exceed the available force (see `setAvailableForce()`).
        Requires a physics-based simulation.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_force
        """

    def setTorque(self, torque: float) -> None:
        """Apply a torque around the axis of a rotational motor directly, bypassing its PID controller [N⋅m].

        The value cannot exceed the available torque (see `setAvailableTorque()`).
        Requires a physics-based simulation.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_set_torque
        """

    def getType(self) -> int:
        """Return the motor type: `Motor.ROTATIONAL` or `Motor.LINEAR`.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_type
        """

    def getBrake(self) -> Brake | None:
        """Return the Brake device of the same joint, or `None` if the joint has no brake.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_brake
        """

    def getPositionSensor(self) -> PositionSensor | None:
        """Return the PositionSensor device of the same joint, or `None` if the joint has none.

        Reference: https://cyberbotics.com/doc/reference/motor?tab-language=python#wb_motor_get_position_sensor
        """

    @property
    def brake(self) -> Brake | None:
        """The Brake device of the same joint, if any (same as `getBrake()`)."""

    @property
    def position_sensor(self) -> PositionSensor | None:
        """The PositionSensor device of the same joint, if any (same as `getPositionSensor()`)."""

    @property
    def force_feedback_sampling_period(self) -> int:
        """Sampling period of the force feedback [ms], 0 when disabled. Setting it enables the feedback."""

    @force_feedback_sampling_period.setter
    def force_feedback_sampling_period(self, sampling_period: int) -> None: ...
    @property
    def torque_feedback_sampling_period(self) -> int:
        """Sampling period of the torque feedback [ms], 0 when disabled. Setting it enables the feedback."""

    @torque_feedback_sampling_period.setter
    def torque_feedback_sampling_period(self, sampling_period: int) -> None: ...
    @property
    def max_position(self) -> float:
        """The `maxPosition` field of the motor [rad or m] (same as `getMaxPosition()`)."""

    @property
    def min_position(self) -> float:
        """The `minPosition` field of the motor [rad or m] (same as `getMinPosition()`)."""

    @property
    def max_velocity(self) -> float:
        """The `maxVelocity` field of the motor [rad/s or m/s] (same as `getMaxVelocity()`)."""

    @property
    def target_position(self) -> float:
        """The target position [rad or m] (same as `getTargetPosition()` / `setPosition()`)."""

    @target_position.setter
    def target_position(self, position: float) -> None: ...
    @property
    def target_velocity(self) -> float:
        """The target velocity [rad/s or m/s] (same as `getVelocity()` / `setVelocity()`)."""

    @target_velocity.setter
    def target_velocity(self, velocity: float) -> None: ...
    @property
    def available_force(self) -> float:
        """The available force [N] (same as `getAvailableForce()` / `setAvailableForce()`)."""

    @available_force.setter
    def available_force(self, force: float) -> None: ...
    @property
    def max_force(self) -> float:
        """The `maxForce` field of the motor [N] (same as `getMaxForce()`)."""

    @property
    def available_torque(self) -> float:
        """The available torque [N⋅m] (same as `getAvailableTorque()` / `setAvailableTorque()`)."""

    @available_torque.setter
    def available_torque(self, torque: float) -> None: ...
    @property
    def max_torque(self) -> float:
        """The `maxTorque` field of the motor [N⋅m] (same as `getMaxTorque()`)."""

    @property
    def target_acceleration(self) -> float:
        """The acceleration [rad/s² or m/s²] (same as `getAcceleration()` / `setAcceleration()`)."""

    @target_acceleration.setter
    def target_acceleration(self, acceleration: float) -> None: ...
    @property
    def force(self) -> Never:
        """Write-only: setting it applies a force directly [N] (same as `setForce()`)."""

    @force.setter
    def force(self, force: float) -> None: ...
    @property
    def torque(self) -> Never:
        """Write-only: setting it applies a torque directly [N⋅m] (same as `setTorque()`)."""

    @torque.setter
    def torque(self, torque: float) -> None: ...
    @property
    def multiplier(self) -> float:
        """The `multiplier` field of the motor (same as `getMultiplier()`)."""

    @property
    def force_feedback(self) -> float:
        """The latest force feedback measurement [N] (same as `getForceFeedback()`)."""

    @property
    def torque_feedback(self) -> float:
        """The latest torque feedback measurement [N⋅m] (same as `getTorqueFeedback()`)."""

    @property
    def type(self) -> int:
        """The motor type, `Motor.ROTATIONAL` or `Motor.LINEAR` (same as `getType()`)."""
