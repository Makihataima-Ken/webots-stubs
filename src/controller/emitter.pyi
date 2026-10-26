from typing import Final

from .device import Device

class Emitter(Device):
    """A radio, infrared or serial emitter that sends data packets to the receivers within its range.

    Reference: https://cyberbotics.com/doc/reference/emitter?tab-language=python
    """

    CHANNEL_BROADCAST: Final = -1
    """Channel value that broadcasts to all channels (see `setChannel()`)."""

    def __init__(self, name: str | int) -> None: ...
    def getBufferSize(self) -> int:
        """Return the size of the transmission buffer [bytes], -1 meaning unlimited.

        Reference: https://cyberbotics.com/doc/reference/emitter?tab-language=python#wb_emitter_get_buffer_size
        """

    def send(
        self, message: str | bytes | list[float] | list[int] | tuple[float, ...], length: int | None = None
    ) -> None:
        """Queue a data packet for the receivers within range.

        A `str` is sent as its characters, but only `len(message)` bytes of its encoding, so pass `bytes`
        for non-ASCII text; `bytes` as they are (`length` defaults to their size and is
        ignored for other types), and a non-empty list or tuple is packed as C doubles if its first item
        is a float, else as C ints. For other formats, pack the data with the `struct` module.
        An empty list or unsupported type prints a message to stderr and sends nothing.
        The packet is dropped if the queue is full.

        Reference: https://cyberbotics.com/doc/reference/emitter?tab-language=python#wb_emitter_send
        """

    def getChannel(self) -> int:
        """Return the current transmission channel.

        Reference: https://cyberbotics.com/doc/reference/emitter?tab-language=python#wb_emitter_get_channel
        """

    def setChannel(self, channel: int) -> None:
        """Set the transmission channel, or `Emitter.CHANNEL_BROADCAST` to reach all channels.

        Only receivers on the same channel get the data. The channel must be in `allowedChannels`
        unless that field is empty.

        Reference: https://cyberbotics.com/doc/reference/emitter?tab-language=python#wb_emitter_set_channel
        """

    @property
    def channel(self) -> int:
        """The transmission channel (same as `getChannel()` / `setChannel()`)."""

    @channel.setter
    def channel(self, c: int) -> None: ...
    def getRange(self) -> float:
        """Return the transmission range [m], -1 meaning infinite.

        Reference: https://cyberbotics.com/doc/reference/emitter?tab-language=python#wb_emitter_get_range
        """

    def setRange(self, range: float) -> None:
        """Set the transmission range [m], -1 meaning infinite.

        A value above the `maxRange` field is clamped to it.

        Reference: https://cyberbotics.com/doc/reference/emitter?tab-language=python#wb_emitter_set_range
        """

    @property
    def range(self) -> float:
        """The transmission range [m] (same as `getRange()` / `setRange()`)."""

    @range.setter
    def range(self, range: float) -> None: ...
    @property
    def buffer_size(self) -> int:
        """The size of the transmission buffer [bytes] (same as `getBufferSize()`)."""
