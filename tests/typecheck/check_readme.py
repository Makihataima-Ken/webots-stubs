"""The code snippets of README.md, kept here so that they stay valid (type-checked, never run)."""

from controller import Camera, DistanceSensor, Lidar, Motor, Robot, Supervisor


def introduction() -> None:
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())

    sensor: DistanceSensor = robot.getDevice("ps0")
    sensor.enable(timestep)
    motor: Motor = robot.getDevice("left wheel motor")
    motor.setPosition(float("inf"))

    while robot.step(timestep) != -1:
        motor.setVelocity(6.28 if sensor.getValue() < 80 else -6.28)


def devices(robot: Robot, i: int) -> None:
    camera: Camera = robot.getDevice("camera")
    camera.enable(32)

    device = robot.getDeviceByIndex(i)
    if isinstance(device, Lidar):
        device.enablePointCloud()


def lookups(supervisor: Supervisor) -> None:
    robot_node = supervisor.getFromDef("ROBOT")
    if robot_node is None:
        raise LookupError("no node with DEF name ROBOT")
    translation = robot_node.getField("translation")
    if translation is not None:
        translation.setSFVec3f([0.0, 0.0, 0.0])
