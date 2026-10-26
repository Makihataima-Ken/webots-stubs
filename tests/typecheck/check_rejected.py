"""Code the stubs must reject (type-checked, never run).

Each line below carries an ignore comment; mypy (warn_unused_ignores) and pyright
(reportUnnecessaryTypeIgnoreComment) fail if the error it silences stops being reported.
"""

from controller import Display, Motor, Robot, Supervisor

robot = Robot()
robot.step("32")  # type: ignore[arg-type]
robot.getMotor("left wheel motor")  # type: ignore[deprecated]
Robot.EVENT_QUIT = 0  # type: ignore[misc]

supervisor = Supervisor()
supervisor.getFromDef("ROBOT").getField("translation")  # type: ignore[union-attr]

display = Display("display")
display.imageDelete(display.imageLoad("icon.png"))  # type: ignore[arg-type]

motor = Motor("motor")
motor.setPosition("1.57")  # type: ignore[arg-type]
motor.max_velocity = 10.0  # type: ignore[misc]
