from .device import Device

class Connector(Device):
    """A connector that detects a compatible peer connector and can lock to it, creating a physical link.

    Reference: https://cyberbotics.com/doc/reference/connector?tab-language=python
    """

    def __init__(self, name: str | int) -> None: ...
    def enablePresence(self, sampling_period: int) -> None:
        """Start querying the presence sensor, every `sampling_period` milliseconds.

        The first measurement is available after the first sampling period has elapsed.

        Reference: https://cyberbotics.com/doc/reference/connector?tab-language=python#wb_connector_enable_presence
        """

    def disablePresence(self) -> None:
        """Stop querying the presence sensor.

        Reference: https://cyberbotics.com/doc/reference/connector?tab-language=python#wb_connector_disable_presence
        """

    def getPresenceSamplingPeriod(self) -> int:
        """Return the sampling period of the presence sensor [ms], or 0 if it is disabled.

        Reference: https://cyberbotics.com/doc/reference/connector?tab-language=python#wb_connector_get_presence_sampling_period
        """

    def getPresence(self) -> int:
        """Return the presence state: 1 if a compatible peer connector is in position, 0 if not.

        Returns -1 if the connector is of type "passive" (not applicable).

        Reference: https://cyberbotics.com/doc/reference/connector?tab-language=python#wb_connector_get_presence
        """

    def isLocked(self) -> bool:
        """Return whether the connector is locked (the `isLocked` field).

        Reference: https://cyberbotics.com/doc/reference/connector?tab-language=python#wb_connector_is_locked
        """

    def lock(self) -> None:
        """Lock the connector, creating a physical link if a peer connector is present.

        Reference: https://cyberbotics.com/doc/reference/connector?tab-language=python#wb_connector_lock
        """

    def unlock(self) -> None:
        """Unlock the connector, destroying the physical link with its peer if there is one.

        The link stays if `unilateralUnlock` is FALSE and the peer connector is still locked.

        Reference: https://cyberbotics.com/doc/reference/connector?tab-language=python#wb_connector_unlock
        """

    @property
    def locked(self) -> bool:
        """Whether the connector is locked (same as `isLocked()`)."""

    @property
    def presence(self) -> int:
        """The presence state: 1 present, 0 absent, -1 not applicable (same as `getPresence()`)."""

    @property
    def presence_sampling_period(self) -> int:
        """Sampling period of the presence sensor [ms], 0 when disabled (same as `getPresenceSamplingPeriod()`)."""
