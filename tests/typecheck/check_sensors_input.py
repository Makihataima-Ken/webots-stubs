"""Type-checking tests for the simple sensors and user input modules (checked by mypy and pyright, never run)."""

from ctypes import _Pointer, c_double  # pyright: ignore[reportPrivateUsage]
from typing import Literal

from typing_extensions import assert_type

from controller import (
    GPS,
    Accelerometer,
    Altimeter,
    AnsiCodes,
    Compass,
    DistanceSensor,
    Gyro,
    InertialUnit,
    Joystick,
    Keyboard,
    LightSensor,
    Motion,
    Mouse,
    MouseState,
    Skin,
    TouchSensor,
)

# Vector sensors return lists of floats.
accelerometer = Accelerometer("accelerometer")
assert_type(accelerometer.getValues(), list[float])
assert_type(accelerometer.value, list[float])
assert_type(accelerometer.getLookupTable(), list[float])
assert_type(accelerometer.sampling_period, int)

assert_type(Altimeter("altimeter").getValue(), float)
assert_type(Compass("compass").getValues(), list[float])
assert_type(Compass("compass").lookup_table, list[float])
assert_type(Gyro("gyro").value, list[float])

imu = InertialUnit("imu")
assert_type(imu.getRollPitchYaw(), list[float])
assert_type(imu.getQuaternion(), list[float])
assert_type(imu.noise, float)

gps = GPS("gps")
assert_type(gps.getValues(), list[float])
assert_type(gps.getSpeedVector(), list[float])
assert_type(gps.speed, float)
assert_type(gps.getCoordinateSystem(), int)
assert_type(GPS.convertToDegreesMinutesSeconds(48.85), str)
assert_type(GPS.LOCAL, Literal[0])
assert_type(GPS.WGS84, Literal[1])

# Distance, light and touch sensors.
ds = DistanceSensor("ds0")
assert_type(ds.getValue(), float)
assert_type(ds.getAperture(), float)
assert_type(ds.getLookupTable(), list[float])
assert_type(ds.lookup_table, _Pointer[c_double])
assert_type(ds.getType(), int)
assert_type(DistanceSensor.LASER, Literal[3])

ls = LightSensor("ls0")
assert_type(ls.getValue(), float)
assert_type(ls.lookup_table, _Pointer[c_double])

ts = TouchSensor("ts0")
assert_type(ts.getValue(), float)
assert_type(ts.getValues(), _Pointer[c_double])
assert_type(ts.values, _Pointer[c_double])
assert_type(ts.getLookupTable(), list[float])
assert_type(TouchSensor.FORCE3D, Literal[2])

# Joystick.
joystick = Joystick()
joystick.enable(32)
assert_type(joystick.isConnected(), bool)
assert_type(joystick.getAxisValue(0), float)
assert_type(joystick.getPovValue(0), int)
assert_type(joystick.getPressedButton(), int)
assert_type(joystick.model, str)
joystick.sampling_period = 16
joystick.sampling_period = None
joystick.setConstantForce(5)
joystick.setAutoCenteringGain(0.5)

# Keyboard.
keyboard = Keyboard()
assert_type(keyboard.getKey(), int)
assert_type(keyboard.get_key(), str)
assert_type(Keyboard.UP, int)
assert_type(Keyboard.SHIFT, int)
assert_type(keyboard.sampling_period, int)
keyboard.sampling_period = 64
if keyboard.getKey() & Keyboard.KEY == ord("A"):
    pass

# Mouse.
mouse = Mouse()
state = mouse.getState()
assert_type(state, MouseState)
assert_type(state.u, float)
assert_type(state.x, float)
assert_type(state.left, bool)
assert_type(mouse.is3dPositionEnabled(), bool)
mouse.enable3dPosition()

# Motion.
motion = Motion("hand_wave.motion")
assert_type(motion.isValid(), bool)
assert_type(motion.isOver(), bool)
assert_type(motion.getDuration(), int)
assert_type(motion.time, int)
motion.time = 100
motion.setTime(0)
motion.setLoop(True)
motion.play()

# Skin.
skin = Skin("skin")
assert_type(skin.getBoneCount(), int)
assert_type(skin.bone_count, int)
assert_type(skin.getBoneName(0), str)
assert_type(skin.getBonePosition(0, True), _Pointer[c_double])
assert_type(skin.getBoneOrientation(0, False), _Pointer[c_double])
skin.setBonePosition(0, [0.0, 0.1, 0.2], True)
skin.setBoneOrientation(0, [0.0, 0.0, 1.0, 1.57], False)

# ANSI codes.
assert_type(AnsiCodes.RESET, str)
assert_type(AnsiCodes.RED_FOREGROUND, str)
print(AnsiCodes.BOLD + "text" + AnsiCodes.RESET)
