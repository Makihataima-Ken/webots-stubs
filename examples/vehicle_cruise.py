"""Drive a car straight at a constant speed, braking when the lidar sees an obstacle ahead.

Use it as the controller of a car (e.g. a BmwX5 or TeslaModel3 PROTO) equipped with a Lidar
called ``Sick LMS 291``.
"""

from controller import Lidar
from vehicle import Driver

CRUISING_SPEED = 30.0  # [km/h]
SAFETY_DISTANCE = 10.0  # [m]


def main() -> None:
    driver = Driver()
    timestep = int(driver.getBasicTimeStep())

    lidar: Lidar = driver.getDevice("Sick LMS 291")
    lidar.enable(timestep)

    driver.setSteeringAngle(0.0)
    driver.setCruisingSpeed(CRUISING_SPEED)

    while driver.step() != -1:
        ranges = lidar.getRangeImage()
        center = ranges[len(ranges) // 2 - 5 : len(ranges) // 2 + 5]
        if center and min(center) < SAFETY_DISTANCE:
            driver.setCruisingSpeed(0.0)
            driver.setBrakeIntensity(1.0)
        else:
            driver.setBrakeIntensity(0.0)
            driver.setCruisingSpeed(CRUISING_SPEED)


if __name__ == "__main__":
    main()
