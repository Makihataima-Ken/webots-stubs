"""Type-checking tests for controller.supervisor and controller.proto (checked by mypy and pyright, never run)."""

from typing import Literal

from typing_extensions import assert_type

from controller import Field, Node, Proto, Robot, Supervisor

supervisor = Supervisor()
assert_type(supervisor, Supervisor)
robot: Robot = supervisor

# Robot members are inherited.
assert_type(supervisor.step(32), int)
assert_type(supervisor.getBasicTimeStep(), float)

assert_type(supervisor.getRoot(), Node)
assert_type(supervisor.getSelf(), Node)

# Lookups can fail.
assert_type(supervisor.getFromDef("BALL"), Node | None)
assert_type(supervisor.getFromId(12), Node | None)
assert_type(supervisor.getFromDevice(1), Node | None)
assert_type(supervisor.getSelected(), Node | None)

ball = supervisor.getFromDef("BALL")
if ball is not None:
    assert_type(ball.getPosition(), list[float])

supervisor.setLabel(0, "hello", 0.0, 0.0, 0.1, 0xFF0000)
supervisor.setLabel(1, "hello", 0, 0.1, 0.1, 0x00FF00, 0.5, "Impact")
assert_type(supervisor.setLabel(2, "text", 0, 0, 0.1, 0), None)

assert_type(Supervisor.SIMULATION_MODE_PAUSE, Literal[0])
assert_type(Supervisor.SIMULATION_MODE_REAL_TIME, Literal[1])
assert_type(Supervisor.SIMULATION_MODE_FAST, Literal[2])
supervisor.simulationSetMode(Supervisor.SIMULATION_MODE_FAST)
assert_type(supervisor.simulationGetMode(), int)
assert_type(supervisor.simulation_mode, int)
supervisor.simulation_mode = Supervisor.SIMULATION_MODE_PAUSE

supervisor.simulationQuit(0)
supervisor.simulationReset()
supervisor.simulationResetPhysics()
supervisor.worldLoad("worlds/other.wbt")
supervisor.worldReload()
assert_type(supervisor.worldSave(), int)
assert_type(supervisor.worldSave("worlds/copy.wbt"), int)
assert_type(supervisor.worldSave(None), int)

supervisor.exportImage("snapshot.jpg", 90)
supervisor.movieStartRecording("movie.mp4", 1280, 720, 0, 90, 1, False)
supervisor.movieStopRecording()
assert_type(supervisor.movieIsReady(), bool)
assert_type(supervisor.movieFailed(), bool)
assert_type(supervisor.animationStartRecording("animation.html"), int)
assert_type(supervisor.animationStopRecording(), int)

assert_type(supervisor.virtualRealityHeadsetIsUsed(), bool)
assert_type(supervisor.virtualRealityHeadsetGetPosition(), list[float])
assert_type(supervisor.virtualRealityHeadsetGetOrientation(), list[float])

# Proto
proto = Proto(0)
assert_type(proto.getTypeName(), str)
assert_type(proto.type_name, str)
assert_type(proto.getParent(), Proto | None)
assert_type(proto.getField("name"), Field | None)
assert_type(proto.getFieldByIndex(0), Field | None)
assert_type(proto.getNumberOfFields(), int)
assert_type(proto.number_of_fields, int)
assert_type(proto.isDerived(), bool)
assert_type(proto.is_derived, bool)

parent = proto.getParent()
if parent is not None:
    assert_type(parent.getTypeName(), str)
