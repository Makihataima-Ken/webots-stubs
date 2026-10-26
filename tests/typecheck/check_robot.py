"""Type-checking tests for controller.robot (checked by mypy and pyright, never run)."""

from typing import Any, Literal

from typing_extensions import assert_type

from controller import GPS, Joystick, Keyboard, Motor, Mouse, Robot
from controller.device import Device

robot = Robot()

assert_type(robot.step(), int)
assert_type(robot.step(32), int)
assert_type(robot.stepBegin(), int)
assert_type(robot.stepEnd(), int)
assert_type(robot.getBasicTimeStep(), float)
assert_type(robot.basic_time_step, float)
assert_type(robot.getTime(), float)
assert_type(robot.getName(), str)
assert_type(robot.getSupervisor(), bool)
assert_type(robot.getUrdf(), str)
assert_type(robot.getUrdf(prefix="r1_"), str)
assert_type(robot.wwiReceiveText(), str | None)
assert_type(robot.batterySensorGetValue(), float)

# getDevice() is deliberately Any: annotating the variable gives a typed device.
assert_type(robot.getDevice("gps"), Any)
gps: GPS = robot.getDevice("gps")
assert_type(gps.getValues(), list[float])
assert_type(robot.getDeviceByIndex(0), Device)
assert_type(robot.devices, dict[str, Device])

assert_type(robot.getKeyboard(), Keyboard)
assert_type(robot.getMouse(), Mouse)
assert_type(robot.getJoystick(), Joystick)

assert_type(Robot.EVENT_QUIT, Literal[-1])
assert_type(Robot.created, Robot | None)
event = robot.waitForUserInputEvent(Robot.EVENT_KEYBOARD | Robot.EVENT_MOUSE_CLICK, 1000)
assert_type(event, int)

robot.custom_data = "configuration"
robot.battery_sensor_sampling_period = None


def control_loop(robot: Robot) -> None:
    timestep = int(robot.getBasicTimeStep())
    left: Motor = robot.getDevice("left wheel motor")
    left.setPosition(float("inf"))
    while robot.step(timestep) != -1:
        left.setVelocity(2.0)
