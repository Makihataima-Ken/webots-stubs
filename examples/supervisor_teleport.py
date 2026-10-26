"""A supervisor that brings a robot back to its start position when it wanders too far.

The world must contain a robot whose DEF name is ``ROBOT``; this controller runs on a
Robot node whose ``supervisor`` field is TRUE.
"""

import math

from controller import Field, Node, Supervisor

MAX_DISTANCE = 1.0  # [m]


def find_field(node: Node, name: str) -> Field:
    field = node.getField(name)
    if field is None:
        raise LookupError(f"{node.getTypeName()} has no field named {name!r}")
    return field


def main() -> None:
    supervisor = Supervisor()
    timestep = int(supervisor.getBasicTimeStep())

    robot = supervisor.getFromDef("ROBOT")
    if robot is None:
        raise LookupError("no node with DEF name ROBOT in the world")
    translation = find_field(robot, "translation")
    start = translation.getSFVec3f()

    while supervisor.step(timestep) != -1:
        x, y, _ = robot.getPosition()
        if math.hypot(x - start[0], y - start[1]) > MAX_DISTANCE:
            translation.setSFVec3f(start)
            robot.resetPhysics()
            print(f"Robot moved back to its start position at t={supervisor.getTime():.2f} s")


if __name__ == "__main__":
    main()
