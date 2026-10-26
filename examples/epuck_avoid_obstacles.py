"""Obstacle avoidance for the e-puck robot: a fully typed Webots controller.

Use it as the controller of an e-puck in any world (e.g. projects/robots/gctronic/e-puck).
"""

from controller import DistanceSensor, Motor, Robot

MAX_SPEED = 6.28  # [rad/s]
OBSTACLE_THRESHOLD = 80.0  # raw proximity sensor value


def main() -> None:
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())

    sensors: list[DistanceSensor] = []
    for index in range(8):
        sensor: DistanceSensor = robot.getDevice(f"ps{index}")
        sensor.enable(timestep)
        sensors.append(sensor)

    left_motor: Motor = robot.getDevice("left wheel motor")
    right_motor: Motor = robot.getDevice("right wheel motor")
    for motor in (left_motor, right_motor):
        motor.setPosition(float("inf"))  # velocity control
        motor.setVelocity(0.0)

    while robot.step(timestep) != -1:
        values = [sensor.getValue() for sensor in sensors]
        obstacle_right = any(value > OBSTACLE_THRESHOLD for value in values[0:3])
        obstacle_left = any(value > OBSTACLE_THRESHOLD for value in values[5:8])

        left_speed = right_speed = 0.5 * MAX_SPEED
        if obstacle_left:
            left_speed, right_speed = 0.5 * MAX_SPEED, -0.5 * MAX_SPEED
        elif obstacle_right:
            left_speed, right_speed = -0.5 * MAX_SPEED, 0.5 * MAX_SPEED
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)


if __name__ == "__main__":
    main()
