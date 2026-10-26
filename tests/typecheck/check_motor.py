"""Type-checking tests for controller.motor (checked by mypy and pyright, never run)."""

from typing_extensions import assert_type

from controller import Brake, Motor, PositionSensor

motor = Motor("joint motor")

assert_type(motor.getTargetPosition(), float)
assert_type(motor.target_position, float)
assert_type(motor.getType(), int)
assert_type(Motor.ROTATIONAL, int)
assert_type(motor.getForceFeedback(), float)

# The joint may have no brake or position sensor.
assert_type(motor.getBrake(), Brake | None)
assert_type(motor.getPositionSensor(), PositionSensor | None)
assert_type(motor.position_sensor, PositionSensor | None)

sensor = motor.getPositionSensor()
if sensor is not None:
    sensor.enable(32)

motor.target_position = 1.57
motor.target_velocity = 2.0
motor.force = 1.0
motor.setControlPID(10.0, 0.0, 0.0)
