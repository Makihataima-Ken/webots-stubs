"""Type-checking tests for the vehicle package (checked by mypy and pyright, never run)."""

import ctypes
from typing import Literal

from typing_extensions import assert_type

from controller import Supervisor
from vehicle import Car, Driver

driver = Driver()
supervisor: Supervisor = driver

assert_type(driver.step(), int)
assert_type(driver.getCurrentSpeed(), float)
assert_type(driver.current_speed, float)
assert_type(driver.getGear(), int)
assert_type(driver.gear_number, int)
assert_type(driver.getIndicator(), int)
assert_type(driver.getAntifogLights(), bool)
assert_type(driver.dipped_beams, bool)
assert_type(driver.getWiperMode(), int)
assert_type(Driver.isInitialisationPossible(), bool)
assert_type(Driver.loadApi(), None)

# The control mode may be unavailable.
assert_type(driver.getControlMode(), int | None)
assert_type(driver.control_mode, int | None)

assert_type(Driver.INDICATOR_LEFT, Literal[2])
assert_type(Driver.FAST, Literal[3])
assert_type(Driver.api, ctypes.CDLL | None)

driver.setSteeringAngle(0.2)
driver.setCruisingSpeed(30.0)
driver.setThrottle(0.5)
driver.setBrakeIntensity(0.0)
driver.setGear(1)
driver.setIndicator(Driver.INDICATOR_RIGHT)
driver.setWiperMode(Driver.NORMAL)

driver.steering_angle = 0.1
driver.target_cruising_speed = 50.0
driver.throttle = 1.0
driver.brake_intensity = 0.3
driver.gear = -1
driver.antifog_lights = True
driver.hazard_flashers = False
driver.wiper_mode = Driver.SLOW

car = Car()
base: Driver = car
assert_type(car.api, ctypes.CDLL)
assert_type(car.getType(), int)
assert_type(car.getEngineType(), int)
assert_type(car.getTrackFront(), float)
assert_type(car.wheelbase, float)
assert_type(car.getWheelEncoder(Car.WHEEL_FRONT_LEFT), float)
assert_type(car.getWheelSpeed(Car.WHEEL_REAR_RIGHT), float)
assert_type(car.getIndicatorPeriod(), float)
assert_type(car.backwards_lights, bool)
assert_type(Car.TRACTION, Literal[0])
assert_type(Car.ELECTRIC_ENGINE, Literal[1])

car.setIndicatorPeriod(0.5)
car.setLeftSteeringAngle(0.1)
car.setRightSteeringAngle(0.1)
car.enableLimitedSlipDifferential(False)
car.enableIndicatorAutoDisabling(True)
car.indicator_period = 0.4
car.left_steering_angle = 0.2
car.right_steering_angle = 0.2
