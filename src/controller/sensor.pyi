from .device import Device

class Sensor(Device):
    """Base class of the devices that are enabled with a sampling period before they can be read.

    Constructing a sensor by name (rather than getting it from `Robot.getDevice()`)
    enables it right away, with `sampling_period` or else the world's basic time step.
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def enable(self, p: int) -> None:
        """Enable the sensor, with a new measurement every `p` milliseconds of simulated time.

        The first measurement is available after the first sampling period has elapsed.
        """

    def getSamplingPeriod(self) -> int:
        """Return the sampling period of the sensor [ms], or 0 if it is disabled."""

    def disable(self) -> None:
        """Disable the sensor, stopping its measurements and saving computation time."""

    @property
    def sampling_period(self) -> int:
        """Sampling period of the sensor [ms], 0 when disabled. Setting it enables the sensor; `None` disables it."""

    @sampling_period.setter
    def sampling_period(self, p: int | None) -> None: ...
