"""Type-checking tests for the actuator and communication devices (checked by mypy and pyright, never run)."""

from typing import Literal

from typing_extensions import assert_type

from controller import (
    LED,
    Brake,
    Connector,
    Display,
    Emitter,
    Motor,
    PositionSensor,
    Radar,
    RadarTarget,
    Receiver,
    Speaker,
    VacuumGripper,
)
from controller.pen import Pen

# Brake and PositionSensor: the joint's other devices may be missing.
brake = Brake("brake")
assert_type(brake.getType(), int)
assert_type(Brake.ROTATIONAL, int)
assert_type(brake.getMotor(), Motor | None)
assert_type(brake.getPositionSensor(), PositionSensor | None)
assert_type(brake.motor, Motor | None)
assert_type(brake.position_sensor, PositionSensor | None)
brake.setDampingConstant(0.5)
brake.dampingConstant = 0.5

position_sensor = PositionSensor("joint sensor", 32)
assert_type(position_sensor.getValue(), float)
assert_type(position_sensor.value, float)
assert_type(position_sensor.getType(), int)
assert_type(PositionSensor.LINEAR, int)
assert_type(position_sensor.getBrake(), Brake | None)
assert_type(position_sensor.getMotor(), Motor | None)
assert_type(position_sensor.brake, Brake | None)
assert_type(position_sensor.motor, Motor | None)
position_sensor.enable(16)
assert_type(position_sensor.getSamplingPeriod(), int)

# Connector
connector = Connector("connector")
connector.enablePresence(32)
assert_type(connector.getPresence(), int)
assert_type(connector.presence, int)
assert_type(connector.isLocked(), bool)
assert_type(connector.locked, bool)
assert_type(connector.getPresenceSamplingPeriod(), int)
connector.lock()
connector.unlock()

# Display
display = Display("display")
assert_type(display.getWidth(), int)
assert_type(display.height, int)
assert_type(Display.BGRA, Literal[6])
display.setColor(0xFF0000)
display.color = 0x00FF00
display.alpha = 0.5
display.opacity = 1.0
display.setFont("Arial", 16, True)
display.drawText("hello", 0, 0)
display.drawPolygon([0, 10, 5], [0, 0, 10])
display.fillPolygon((0, 10, 5), (0, 0, 10))
display.drawLine(0, 0, 10, 10)
# Clipboard images are None when the file is unreadable or the arguments are invalid.
image = display.imageLoad("icon.png")
assert_type(image, int | None)
assert_type(display.imageNew(b"\x00\x00\x00\xff", Display.BGRA, 1, 1), int | None)
assert_type(display.imageCopy(0, 0, 4, 4), int | None)
if image is not None:
    display.imagePaste(image, 0, 0, False)
    display.imageSave(image, "out.png")
    display.imageDelete(image)
display.imageSave(None, "main.png")

# Emitter and Receiver
emitter = Emitter("emitter")
assert_type(emitter.getBufferSize(), int)
assert_type(emitter.buffer_size, int)
assert_type(emitter.getChannel(), int)
assert_type(emitter.channel, int)
assert_type(emitter.getRange(), float)
assert_type(emitter.range, float)
assert_type(Emitter.CHANNEL_BROADCAST, Literal[-1])
assert_type(emitter.send("hello"), None)
emitter.send(b"\x01\x02", 2)
emitter.send([1.0, 2.0])
emitter.send([1, 2, 3])
emitter.send((1.5, 2.5))
emitter.channel = Emitter.CHANNEL_BROADCAST
emitter.range = 3.0
emitter.setChannel(1)
emitter.setRange(-1)

receiver = Receiver("receiver", 32)
assert_type(receiver.getQueueLength(), int)
assert_type(receiver.getBytes(), bytes)
assert_type(receiver.getString(), str)
assert_type(receiver.getFloats(), tuple[float, ...])
assert_type(receiver.getInts(), tuple[int, ...])
assert_type(receiver.getBools(), tuple[bool, ...])
assert_type(receiver.getDataSize(), int)
assert_type(receiver.getSignalStrength(), float)
assert_type(receiver.getEmitterDirection(), list[float])
assert_type(receiver.emitter_direction, list[float])
assert_type(receiver.signal_strength, float)
assert_type(receiver.string, str)
assert_type(receiver.channel, int)
receiver.channel = 2
receiver.setChannel(Emitter.CHANNEL_BROADCAST)
receiver.nextPacket()
# The deprecated getData() still returns a string (checkers report the deprecation).
assert_type(receiver.getData(), str)  # type: ignore[deprecated]

# LED and Pen
led = LED("led")
led.set(True)
led.set(0xFF00FF)
assert_type(led.get(), int)
assert_type(led.value, int)
led.value = 1

pen = Pen("pen")
pen.write(True)
pen.setInkColor(0xFF0000, 0.9)

# Radar
radar = Radar("radar")
radar.enable(64)
assert_type(radar.getMaxRange(), float)
assert_type(radar.min_range, float)
assert_type(radar.horizontal_fov, float)
assert_type(radar.getVerticalFov(), float)
assert_type(radar.getNumberOfTargets(), int)
assert_type(radar.number_of_targets, int)
targets = radar.getTargets()
assert_type(targets, list[RadarTarget])
for target in targets:
    assert_type(target.distance, float)
    assert_type(target.receiver_power, float)
    assert_type(target.speed, float)
    assert_type(target.azimuth, float)

# Speaker
speaker = Speaker("speaker")
Speaker.playSound(speaker, speaker, "sound.wav", 1.0, 1.0, 0.0, False)
speaker.stop()
speaker.stop("sound.wav")
assert_type(speaker.isSoundPlaying("sound.wav"), bool)
assert_type(speaker.setEngine("pico"), bool)
assert_type(speaker.setLanguage("en-US"), bool)
assert_type(speaker.getEngine(), str)
assert_type(speaker.getLanguage(), str)
assert_type(speaker.isSpeaking(), bool)
speaker.speak("hello", 1.0)

# VacuumGripper
gripper = VacuumGripper("gripper")
gripper.enablePresence(32)
assert_type(gripper.getPresence(), bool)
assert_type(gripper.presence, bool)
assert_type(gripper.isOn(), bool)
assert_type(gripper.on, bool)
assert_type(gripper.getPresenceSamplingPeriod(), int)
gripper.turnOn()
gripper.turnOff()
