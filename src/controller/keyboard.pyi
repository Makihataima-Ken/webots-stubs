from .constants import constant as constant
from .wb import wb as wb
from _typeshed import Incomplete

class Keyboard:
    END: Incomplete
    HOME: Incomplete
    LEFT: Incomplete
    UP: Incomplete
    RIGHT: Incomplete
    DOWN: Incomplete
    PAGEUP: Incomplete
    PAGEDOWN: Incomplete
    NUMPAD_HOME: Incomplete
    NUMPAD_LEFT: Incomplete
    NUMPAD_UP: Incomplete
    NUMPAD_RIGHT: Incomplete
    NUMPAD_DOWN: Incomplete
    NUMPAD_END: Incomplete
    KEY: Incomplete
    SHIFT: Incomplete
    CONTROL: Incomplete
    ALT: Incomplete
    def __init__(self, sampling_period: int | None = None) -> None: ...
    def enable(self, p: int): ...
    def disable(self) -> None: ...
    def getSamplingPeriod(self) -> int: ...
    @property
    def sampling_period(self) -> int: ...
    @sampling_period.setter
    def sampling_period(self, p: int | None): ...
    def getKeyCode(self) -> int: ...
    def getKey(self) -> int: ...
    def get_key(self) -> str: ...
