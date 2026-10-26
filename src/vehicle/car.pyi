import ctypes
from typing import Final

from .driver import Driver

class Car(Driver):
    """A Driver with the extra information and functions of the car library.

    It gives access to what a human driver cannot see or change: the blinking period of the
    indicators, the wheel encoders and speeds, the car dimensions and the steering of each
    front wheel. Distances are in meters [m], angles in radians [rad].

    Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python
    """

    TRACTION: Final = 0
    """Transmission type TRACTION, a value of the car `type` (see `getType()`)."""
    PROPULSION: Final = 1
    """Transmission type PROPULSION, a value of the car `type` (see `getType()`)."""
    FOUR_BY_FOUR: Final = 2
    """Transmission type FOUR_BY_FOUR, a value of the car `type` (see `getType()`)."""
    COMBUSTION_ENGINE: Final = 0
    """Engine type: combustion engine (see `getEngineType()`)."""
    ELECTRIC_ENGINE: Final = 1
    """Engine type: electric engine (see `getEngineType()`)."""
    PARALLEL_HYBRID_ENGINE: Final = 2
    """Engine type: parallel hybrid engine (see `getEngineType()`)."""
    POWER_SPLIT_HYBRID_ENGINE: Final = 3
    """Engine type: power-split hybrid engine (see `getEngineType()`)."""
    WHEEL_FRONT_RIGHT: Final = 0
    """Wheel index of the front right wheel (see `getWheelEncoder()`)."""
    WHEEL_FRONT_LEFT: Final = 1
    """Wheel index of the front left wheel (see `getWheelEncoder()`)."""
    WHEEL_REAR_RIGHT: Final = 2
    """Wheel index of the rear right wheel (see `getWheelEncoder()`)."""
    WHEEL_REAR_LEFT: Final = 3
    """Wheel index of the rear left wheel (see `getWheelEncoder()`)."""

    api: ctypes.CDLL  # pyright: ignore[reportIncompatibleVariableOverride]
    """The loaded car library (`libcar`) of this instance.

    Unlike `Driver.api`, which is a class attribute shared by all instances and `None` until
    loaded, it is always set once the constructor has run.
    """

    def __init__(self) -> None:
        """Initialize the driver library and the car library. Only one instance may be created."""

    def __del__(self) -> None: ...
    def enableIndicatorAutoDisabling(self, enable: bool) -> None:
        """Enable or disable switching the indicator off when steering the other way (default: enabled).

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_enable_indicator_auto_disabling
        """

    def enableLimitedSlipDifferential(self, enable: bool) -> None:
        """Enable or disable the limited slip differential, which evens out wheel speeds (default: enabled).

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_enable_limited_slip_differential
        """

    def getBackwardsLights(self) -> bool:
        """Return whether the backwards lights are on (switched automatically by the library).

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_backwards_lights
        """

    def getBrakeLights(self) -> bool:
        """Return whether the brake lights are on (switched automatically by the library).

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_brake_lights
        """

    def getEngineType(self) -> int:
        """Return the engine type: `Car.COMBUSTION_ENGINE`, `ELECTRIC_ENGINE`,
        `PARALLEL_HYBRID_ENGINE` or `POWER_SPLIT_HYBRID_ENGINE`.

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_engine_type
        """

    def getFrontWheelRadius(self) -> float:
        """Return the radius of the front wheels [m].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_front_wheel_radius
        """

    def getIndicatorPeriod(self) -> float:
        """Return the blinking period of the indicators [s].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_indicator_period
        """

    def getLeftSteeringAngle(self) -> float:
        """Return the steering angle of the left wheel [rad], however it was set.

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_left_steering_angle
        """

    def getRearWheelRadius(self) -> float:
        """Return the radius of the rear wheels [m].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_rear_wheel_radius
        """

    def getRightSteeringAngle(self) -> float:
        """Return the steering angle of the right wheel [rad], however it was set.

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_right_steering_angle
        """

    def getTrackFront(self) -> float:
        """Return the distance between the front wheels [m].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_track_front
        """

    def getTrackRear(self) -> float:
        """Return the distance between the rear wheels [m].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_track_rear
        """

    def getType(self) -> int:
        """Return the transmission type: `Car.TRACTION`, `PROPULSION` or `FOUR_BY_FOUR`.

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_type
        """

    def getWheelbase(self) -> float:
        """Return the distance between the front and rear axles [m].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_wheelbase
        """

    def getWheelEncoder(self, wheel_index: int) -> float:
        """Return the encoder of a wheel [rad]; `wheel_index` is one of the `Car.WHEEL_*` constants.

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_wheel_encoder
        """

    def getWheelSpeed(self, wheel_index: int) -> float:
        """Return the rotation speed of a wheel [rad/s]; `wheel_index` is one of the `Car.WHEEL_*` constants.

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_get_wheel_speed
        """

    def setIndicatorPeriod(self, period: float) -> None:
        """Set the blinking period of the indicators [s].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_set_indicator_period
        """

    def setLeftSteeringAngle(self, angle: float) -> None:
        """Set the steering angle of the left wheel directly, without Ackermann geometry [rad].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_set_left_steering_angle
        """

    def setRightSteeringAngle(self, angle: float) -> None:
        """Set the steering angle of the right wheel directly, without Ackermann geometry [rad].

        Reference: https://cyberbotics.com/doc/automobile/car-library?tab-language=python#wbu_car_set_right_steering_angle
        """

    @property
    def backwards_lights(self) -> bool:
        """Whether the backwards lights are on (same as `getBackwardsLights()`)."""

    @property
    def brake_lights(self) -> bool:
        """Whether the brake lights are on (same as `getBrakeLights()`)."""

    @property
    def engine_type(self) -> int:
        """The engine type (same as `getEngineType()`)."""

    @property
    def front_wheel_radius(self) -> float:
        """The radius of the front wheels [m] (same as `getFrontWheelRadius()`)."""

    @property
    def indicator_period(self) -> float:
        """The blinking period of the indicators [s] (same as `getIndicatorPeriod()` / `setIndicatorPeriod()`)."""

    @indicator_period.setter
    def indicator_period(self, period: float) -> None: ...
    @property
    def left_steering_angle(self) -> float:
        """The steering angle of the left wheel [rad] (same as `getLeftSteeringAngle()` / `setLeftSteeringAngle()`)."""

    @left_steering_angle.setter
    def left_steering_angle(self, angle: float) -> None: ...
    @property
    def rear_wheel_radius(self) -> float:
        """The radius of the rear wheels [m] (same as `getRearWheelRadius()`)."""

    @property
    def right_steering_angle(self) -> float:
        """The right wheel steering angle [rad] (same as `getRightSteeringAngle()` / `setRightSteeringAngle()`)."""

    @right_steering_angle.setter
    def right_steering_angle(self, angle: float) -> None: ...
    @property
    def track_front(self) -> float:
        """The distance between the front wheels [m] (same as `getTrackFront()`)."""

    @property
    def track_rear(self) -> float:
        """The distance between the rear wheels [m] (same as `getTrackRear()`)."""

    @property
    def type(self) -> int:
        """The transmission type (same as `getType()`)."""

    @property
    def wheelbase(self) -> float:
        """The distance between the front and rear axles [m] (same as `getWheelbase()`)."""
