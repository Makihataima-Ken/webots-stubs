class RadarTarget:
    """A target detected by a `Radar`, as returned by `Radar.getTargets()`.

    Reference: https://cyberbotics.com/doc/reference/radar?tab-language=python
    """

    distance: float
    """Distance from the radar to the target [m]."""
    receiver_power: float
    """Power of the signal received from the target [dBm]."""
    speed: float
    """Speed of the target relative to the radar, along the line of sight [m/s]."""
    azimuth: float
    """Azimuth angle of the target in the radar's frame [rad]."""

    def __init__(self, distance: float, receiver_power: float, speed: float, azimuth: float) -> None: ...
