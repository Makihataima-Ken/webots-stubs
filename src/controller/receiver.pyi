import ctypes
from ctypes import _Pointer  # pyright: ignore[reportPrivateUsage]

from typing_extensions import deprecated

from .sensor import Sensor

class Receiver(Sensor):
    """A radio, infrared or serial receiver that queues the data packets sent by emitters in range.

    Enable it, then while `getQueueLength()` is positive read the head packet (`getString()`, `getBytes()`,
    `getFloats()`, ...) and drop it with `nextPacket()`. Reading while the queue is empty is illegal.

    Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python
    """

    def __init__(self, name: str | int, sampling_period: int | None = None) -> None: ...
    def getBytes(self) -> bytes:
        """Return the data of the head packet as bytes.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_data
        """

    @deprecated("Use getString() instead.")
    def getData(self) -> str:
        """Return the data of the head packet as a string.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_data
        """

    def getDataSize(self) -> int:
        """Return the size of the head packet [bytes].

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_data_size
        """

    def getFloats(self) -> tuple[float, ...]:
        """Return the data of the head packet unpacked as C doubles (8 bytes each).

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_data
        """

    def getInts(self) -> tuple[int, ...]:
        """Return the data of the head packet unpacked as C ints (4 bytes each).

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_data
        """

    def getBools(self) -> tuple[bool, ...]:
        """Return the data of the head packet unpacked as booleans (1 byte each).

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_data
        """

    def getQueueLength(self) -> int:
        """Return the number of packets in the reception queue.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_queue_length
        """

    def getString(self) -> str:
        """Return the data of the head packet decoded as a string.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_data
        """

    def nextPacket(self) -> None:
        """Delete the head packet, making the next one (if any) the head of the queue.

        Copy what you need from the head packet first. Illegal if the queue is empty.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_next_packet
        """

    def getSignalStrength(self) -> float:
        """Return the signal strength of the head packet: 1 / r², r being the emitter-receiver distance [m].

        It is +inf for packets sent by a physics plugin.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_signal_strength
        """

    def getEmitterDirection(self) -> list[float]:
        """Return the unit vector [x, y, z] from the receiver to the emitter of the head packet.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_emitter_direction
        """

    def getChannel(self) -> int:
        """Return the reception channel.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_get_channel
        """

    def setChannel(self, channel: int) -> None:
        """Set the reception channel: only packets sent on this channel are received.

        Use `Emitter.CHANNEL_BROADCAST` to receive packets from all channels.

        Reference: https://cyberbotics.com/doc/reference/receiver?tab-language=python#wb_receiver_set_channel
        """

    @property
    def queue_length(self) -> int:
        """The number of packets in the reception queue (same as `getQueueLength()`)."""

    @property
    def data(self) -> _Pointer[ctypes.c_ubyte]:
        """Pointer to the raw data of the head packet, valid until `nextPacket()` is called."""

    @property
    def data_size(self) -> int:
        """The size of the head packet [bytes] (same as `getDataSize()`)."""

    @property
    def string(self) -> str:
        """The data of the head packet decoded as a string (same as `getString()`)."""

    @property
    def signal_strength(self) -> float:
        """The signal strength of the head packet, 1 / r² (same as `getSignalStrength()`)."""

    @property
    def emitter_direction(self) -> list[float]:
        """The unit vector [x, y, z] towards the emitter of the head packet (same as `getEmitterDirection()`)."""

    @property
    def channel(self) -> int:
        """The reception channel (same as `getChannel()` / `setChannel()`)."""

    @channel.setter
    def channel(self, channel: int) -> None: ...
