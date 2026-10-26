class LidarPoint:
    """A point of a lidar point cloud, in coordinates relative to the `Lidar` node origin.

    Reference: https://cyberbotics.com/doc/reference/lidar?tab-language=python#wblidarpoint
    """

    x: float
    """X coordinate [m]."""
    y: float
    """Y coordinate [m]."""
    z: float
    """Z coordinate [m]."""
    layer: int
    """Layer the point belongs to, from 0 to `numberOfLayers` - 1."""
    time: float
    """Time at which the point was acquired [s]."""

    def __init__(self, data: bytes, offset: int) -> None:
        """Decode the `offset`-th point of a raw point cloud buffer (20 bytes per point)."""
