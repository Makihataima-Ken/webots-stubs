from collections.abc import Sequence
from ctypes import _Pointer, c_double  # pyright: ignore[reportPrivateUsage]

from .device import Device

class Skin(Device):
    """A skinned 3D model whose skeleton bones can be read and, if the model is not animated, posed.

    Bones are indexed from 0 to `getBoneCount() - 1`.

    Reference: https://cyberbotics.com/doc/reference/skin?tab-language=python
    """

    def __init__(self, name: str | int) -> None: ...
    def getBoneCount(self) -> int:
        """Return the number of bones in the skeleton of the skin.

        Reference: https://cyberbotics.com/doc/reference/skin?tab-language=python#wb_skin_get_bone_count
        """

    def getBoneName(self, index: int) -> str:
        """Return the name of the bone with the given index.

        Reference: https://cyberbotics.com/doc/reference/skin?tab-language=python#wb_skin_get_bone_name
        """

    def getBoneOrientation(self, index: int, absolute: bool) -> _Pointer[c_double]:
        """Return the axis-angle rotation `[x, y, z, angle]` of a bone, a raw ctypes array of 4 numbers [rad].

        It is relative to the skin node if `absolute` is true, to the parent bone otherwise.

        Reference: https://cyberbotics.com/doc/reference/skin?tab-language=python#wb_skin_get_bone_orientation
        """

    def getBonePosition(self, index: int, absolute: bool) -> _Pointer[c_double]:
        """Return the position `[x, y, z]` of a bone, a raw ctypes array of 3 numbers [m].

        It is relative to the skin node if `absolute` is true, to the parent bone otherwise.

        Reference: https://cyberbotics.com/doc/reference/skin?tab-language=python#wb_skin_get_bone_position
        """

    def setBoneOrientation(self, index: int, orientation: Sequence[float], absolute: bool) -> None:
        """Set the axis-angle rotation `[x, y, z, angle]` of a bone [rad].

        It is relative to the skin node if `absolute` is true, to the parent bone otherwise.
        Only available when the `bones` field of the node is empty.

        Reference: https://cyberbotics.com/doc/reference/skin?tab-language=python#wb_skin_set_bone_orientation
        """

    def setBonePosition(self, index: int, position: Sequence[float], absolute: bool) -> None:
        """Set the position `[x, y, z]` of a bone [m].

        It is relative to the skin node if `absolute` is true, to the parent bone otherwise.
        Only available when the `bones` field of the node is empty.

        Reference: https://cyberbotics.com/doc/reference/skin?tab-language=python#wb_skin_set_bone_position
        """

    @property
    def bone_count(self) -> int:
        """The number of bones in the skeleton of the skin (same as `getBoneCount()`)."""
