import ctypes
from typing import Final

from controller import Supervisor

class Driver(Supervisor):
    """A Supervisor that controls a car the way a human driver does.

    Speeds are in kilometers per hour [km/h] and angles in radians [rad]. The main loop
    calls `Driver.step()`, which takes no time step argument.

    Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python
    """

    INDICATOR_OFF: Final = 0
    """Indicator state: both indicators off (see `setIndicator()`)."""
    INDICATOR_RIGHT: Final = 1
    """Indicator state: right indicator blinking (see `setIndicator()`)."""
    INDICATOR_LEFT: Final = 2
    """Indicator state: left indicator blinking (see `setIndicator()`)."""
    SPEED: Final = 0
    """Control mode: the car is controlled in speed (see `getControlMode()`)."""
    TORQUE: Final = 1
    """Control mode: the car is controlled in torque (see `getControlMode()`)."""
    DOWN: Final = 0
    """Wiper mode: wipers down (see `setWiperMode()`)."""
    SLOW: Final = 1
    """Wiper mode: wipers activated once every few seconds (see `setWiperMode()`)."""
    NORMAL: Final = 2
    """Wiper mode: wipers at normal speed (see `setWiperMode()`)."""
    FAST: Final = 3
    """Wiper mode: wipers at fast speed (see `setWiperMode()`)."""

    api: ctypes.CDLL | None
    """The loaded driver library (`libdriver`), stored on the class and shared by all instances.

    It is `None` until `loadApi()` runs, which the constructor does. `Car` shadows it with an
    instance attribute holding the car library.
    """

    @staticmethod
    def loadApi() -> None:
        """Load the car and driver libraries from `$WEBOTS_HOME/lib/controller` and set `Driver.api`."""

    def __init__(self) -> None:
        """Initialize the Robot controller and the driver library. Only one instance may be created."""

    def __del__(self) -> None: ...
    def getAntifogLights(self) -> bool:
        """Return whether the anti-fog lights are on.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_antifog_lights
        """

    def getBrakeIntensity(self) -> float:
        """Return the brake intensity in [0, 1] given to the last `setBrakeIntensity()` call.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_brake_intensity
        """

    def getControlMode(self) -> int | None:
        """Return the control mode, `Driver.SPEED` or `Driver.TORQUE`, or `None` if it is unavailable.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_control_mode
        """

    def getCurrentSpeed(self) -> float:
        """Return the current speed of the car, estimated from the wheels [km/h].

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_current_speed
        """

    def getDippedBeams(self) -> bool:
        """Return whether the dipped beams are on.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_dipped_beams
        """

    def getGear(self) -> int:
        """Return the engaged gear: -1 for reverse, 0 for neutral, otherwise 1 or more.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_gear
        """

    def getGearNumber(self) -> int:
        """Return the number of available gears, including the reverse gear.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_gear_number
        """

    def getHazardFlashers(self) -> bool:
        """Return whether the hazard flashers (both indicators) are on.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_hazard_flashers
        """

    def getIndicator(self) -> int:
        """Return the indicator state: `Driver.INDICATOR_OFF`, `INDICATOR_RIGHT` or `INDICATOR_LEFT`.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_indicator
        """

    def getRpm(self) -> float:
        """Return the estimated rotation speed of the engine [rpm].

        Not available (an error in Webots) while the car is controlled in cruising speed.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_rpm
        """

    def getSteeringAngle(self) -> float:
        """Return the current steering angle [rad].

        It is not updated by `Car.setRightSteeringAngle()` and `Car.setLeftSteeringAngle()`.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_steering_angle
        """

    def getTargetCruisingSpeed(self) -> float:
        """Return the target speed given to the last `setCruisingSpeed()` call [km/h].

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_target_cruising_speed
        """

    def getThrottle(self) -> float:
        """Return the throttle in [0, 1] given to the last `setThrottle()` call.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_throttle
        """

    def getWiperMode(self) -> int:
        """Return the wiper mode: `Driver.DOWN`, `SLOW`, `NORMAL` or `FAST`.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_get_wiper_mode
        """

    def setAntifogLights(self, state: bool) -> bool:
        """Do not use: this does not switch the anti-fog lights, it only returns their current state.

        Use the `antifog_lights` property to switch them on or off.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_antifog_lights
        """

    def setBrakeIntensity(self, brakeIntensity: float) -> None:
        """Set the brake intensity, from 0.0 (no braking) to 1.0 (full braking).

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_brake_intensity
        """

    def setCruisingSpeed(self, cruisingSpeed: float) -> None:
        """Set the target speed of the car and activate the control in cruising speed [km/h].

        The wheel speed is forced without any engine model, so `getRpm()` is unavailable afterwards.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_cruising_speed
        """

    def setDippedBeams(self, state: bool) -> None:
        """Switch the dipped beams on or off.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_dipped_beams
        """

    def setGear(self, gear: int) -> None:
        """Engage a gear: -1 for reverse, 0 to disengage the gearbox, or 1 up to the number of gears.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_gear
        """

    def setHazardFlashers(self, hazardFlasher: bool) -> None:
        """Switch the hazard flashers (indicators on both sides) on or off.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_hazard_flashers
        """

    def setIndicator(self, indicator: int) -> None:
        """Set the indicator state: `Driver.INDICATOR_OFF`, `INDICATOR_RIGHT` or `INDICATOR_LEFT`.

        Fails with an `AttributeError` in Webots R2025a: it calls a library function that does not exist.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_indicator
        """

    def setSteeringAngle(self, steeringAngle: float) -> None:
        """Steer the front wheels according to the Ackermann geometry [rad].

        A positive angle steers right and a negative angle steers left.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_steering_angle
        """

    def setThrottle(self, throttle: float) -> None:
        """Set the throttle, from 0.0 (no engine torque) to 1.0 (full engine torque).

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_throttle
        """

    def setWiperMode(self, mode: int) -> None:
        """Set the wiper mode: `Driver.DOWN`, `SLOW`, `NORMAL` or `FAST`.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_set_wiper_mode
        """

    def step(self) -> int:  # type: ignore[override]
        """Run one simulation step of the default time step of the world; return -1 when Webots ends the controller.

        Unlike `Robot.step()`, it takes no argument.

        Reference: https://cyberbotics.com/doc/automobile/driver-library?tab-language=python#wbu_driver_step
        """

    @property
    def antifog_lights(self) -> bool:
        """Whether the anti-fog lights are on (same as `getAntifogLights()`)."""

    @antifog_lights.setter
    def antifog_lights(self, antifog_lights: bool) -> None: ...
    @property
    def brake_intensity(self) -> float:
        """The brake intensity in [0, 1] (same as `getBrakeIntensity()` / `setBrakeIntensity()`)."""

    @brake_intensity.setter
    def brake_intensity(self, brake_intensity: float) -> None: ...
    @property
    def control_mode(self) -> int | None:
        """The control mode, `Driver.SPEED` or `Driver.TORQUE`, or `None` (same as `getControlMode()`)."""

    @property
    def dipped_beams(self) -> bool:
        """Whether the dipped beams are on (same as `getDippedBeams()` / `setDippedBeams()`)."""

    @dipped_beams.setter
    def dipped_beams(self, dipped_beams: bool) -> None: ...
    @property
    def gear(self) -> int:
        """The engaged gear (same as `getGear()` / `setGear()`)."""

    @gear.setter
    def gear(self, gear: int) -> None: ...
    @property
    def gear_number(self) -> int:
        """The number of available gears (same as `getGearNumber()`)."""

    @property
    def hazard_flashers(self) -> bool:
        """Whether the hazard flashers are on (same as `getHazardFlashers()` / `setHazardFlashers()`)."""

    @hazard_flashers.setter
    def hazard_flashers(self, hazard_flashers: bool) -> None: ...
    @property
    def indicator(self) -> int:
        """The indicator state (same as `getIndicator()` / `setIndicator()`); setting it fails in R2025a."""

    @indicator.setter
    def indicator(self, indicator: int) -> None: ...
    @property
    def rpm(self) -> float:
        """The estimated engine rotation speed [rpm] (same as `getRpm()`)."""

    @property
    def steering_angle(self) -> float:
        """The steering angle [rad] (same as `getSteeringAngle()` / `setSteeringAngle()`)."""

    @steering_angle.setter
    def steering_angle(self, value: float) -> None: ...
    @property
    def current_speed(self) -> float:
        """The current speed of the car [km/h] (same as `getCurrentSpeed()`)."""

    @property
    def target_cruising_speed(self) -> float:
        """The target cruising speed [km/h] (same as `getTargetCruisingSpeed()` / `setCruisingSpeed()`)."""

    @target_cruising_speed.setter
    def target_cruising_speed(self, target_cruising_speed: float) -> None: ...
    @property
    def throttle(self) -> float:
        """The throttle in [0, 1] (same as `getThrottle()` / `setThrottle()`)."""

    @throttle.setter
    def throttle(self, throttle: float) -> None: ...
    @property
    def wiper_mode(self) -> int:
        """The wiper mode (same as `getWiperMode()` / `setWiperMode()`)."""

    @wiper_mode.setter
    def wiper_mode(self, mode: int) -> None: ...
    @staticmethod
    def isInitialisationPossible() -> bool:
        """Return whether the robot can use the driver library (used by webots_ros2); loads the library if needed."""
