class Device:
    """Base class of all robot devices (sensors and actuators).

    Device objects are normally obtained with `Robot.getDevice()`, which returns an
    instance of the matching subclass (`Motor`, `Camera`, `DistanceSensor`, ...).

    Reference: https://cyberbotics.com/doc/reference/device?tab-language=python
    """

    def __init__(self, name: str | int) -> None:
        """Look up the device called `name` on the robot, or wrap an existing device tag."""

    def getName(self) -> str:
        """Return the value of the device's `name` field.

        Reference: https://cyberbotics.com/doc/reference/device?tab-language=python#wb_device_get_name
        """

    def getModel(self) -> str:
        """Return the value of the device's `model` field, or "" if the device has no such field.

        Reference: https://cyberbotics.com/doc/reference/device?tab-language=python#wb_device_get_model
        """

    def getNodeType(self) -> int:
        """Return the node type of the device, to compare with the `Node` type constants (e.g. `Node.CAMERA`).

        Reference: https://cyberbotics.com/doc/reference/device?tab-language=python#wb_device_get_node_type
        """

    @property
    def name(self) -> str:
        """The value of the device's `name` field (same as `getName()`)."""

    @property
    def model(self) -> str:
        """The value of the device's `model` field (same as `getModel()`)."""

    @property
    def node_type(self) -> int:
        """The node type of the device (same as `getNodeType()`)."""
