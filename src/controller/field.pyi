from typing import Final

from .node import Node

class Field:
    """A field of a node of the scene tree, accessible from a Supervisor controller.

    Fields are obtained with `Node.getField()` and similar methods. The `getSF*`/`setSF*` methods handle single
    fields and the `getMF*`/`setMF*`/`insertMF*`/`removeMF` methods multiple fields, selected by `index` (a negative
    index counts from the end). Vectors are lists of floats: 2 values for a Vec2f, 3 for a Vec3f or a Color,
    4 for a Rotation (axis x, y, z and angle [rad]).

    Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python
    """

    SF_BOOL: Final[int]
    """Type of SFBool fields."""
    SF_INT32: Final[int]
    """Type of SFInt32 fields."""
    SF_FLOAT: Final[int]
    """Type of SFFloat fields."""
    SF_VEC2F: Final[int]
    """Type of SFVec2f fields."""
    SF_VEC3F: Final[int]
    """Type of SFVec3f fields."""
    SF_ROTATION: Final[int]
    """Type of SFRotation fields."""
    SF_COLOR: Final[int]
    """Type of SFColor fields."""
    SF_STRING: Final[int]
    """Type of SFString fields."""
    SF_NODE: Final[int]
    """Type of SFNode fields."""
    MF_BOOL: Final[int]
    """Type of MFBool fields."""
    MF_INT32: Final[int]
    """Type of MFInt32 fields."""
    MF_FLOAT: Final[int]
    """Type of MFFloat fields."""
    MF_VEC2F: Final[int]
    """Type of MFVec2f fields."""
    MF_VEC3F: Final[int]
    """Type of MFVec3f fields."""
    MF_ROTATION: Final[int]
    """Type of MFRotation fields."""
    MF_COLOR: Final[int]
    """Type of MFColor fields."""
    MF_STRING: Final[int]
    """Type of MFString fields."""
    MF_NODE: Final[int]
    """Type of MFNode fields."""

    type: int
    """The type of the field (one of the `SF_*` / `MF_*` constants)."""

    def __init__(self, ref: int | None) -> None:
        """Wrap a raw field handle. Use `Node.getField()` to obtain fields."""

    def getName(self) -> str:
        """Return the name of the field (same as the `name` property).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_name
        """

    def getType(self) -> int:
        """Return the type of the field, to compare with the `SF_*` / `MF_*` constants (same as `type`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_type
        """

    def getTypeName(self) -> str:
        """Return the VRML name of the field type, like "SFFloat" or "MFNode" (same as `type_name`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_type_name
        """

    def getCount(self) -> int:
        """Return the number of items of a multiple field, or -1 for a single field (same as `count`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_count
        """

    def getActualField(self) -> Field | None:
        """Return the modifiable scene tree field associated with this (internal) field, or `None`.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_actual_field
        """

    def enableSFTracking(self, samplingPeriod: int) -> None:
        """Make Webots stream the value of this single field to the controller every `samplingPeriod` [ms].

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_enable_sf_tracking
        """

    def disableSFTracking(self) -> None:
        """Stop the tracking of this single field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_disable_sf_tracking
        """

    def getSFBool(self) -> int:
        """Return the value of a SFBool field as an int (0 or 1), not a bool.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_bool
        """

    def getSFInt32(self) -> int:
        """Return the value of a SFInt32 field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_int32
        """

    def getSFFloat(self) -> float:
        """Return the value of a SFFloat field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_float
        """

    def getSFVec2f(self) -> list[float]:
        """Return the value `[x, y]` of a SFVec2f field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_vec2f
        """

    def getSFVec3f(self) -> list[float]:
        """Return the value `[x, y, z]` of a SFVec3f field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_vec3f
        """

    def getSFRotation(self) -> list[float]:
        """Return the value `[x, y, z, angle]` of a SFRotation field [rad].

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_rotation
        """

    def getSFColor(self) -> list[float]:
        """Return the value `[r, g, b]` of a SFColor field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_color
        """

    def getSFString(self) -> str:
        """Return the value of a SFString field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_string
        """

    def getSFNode(self) -> Node | None:
        """Return the node of a SFNode field, or `None` if the field is empty.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_node
        """

    def getMFBool(self, index: int) -> bool:
        """Return the item at `index` of a MFBool field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_bool
        """

    def getMFInt32(self, index: int) -> int:
        """Return the item at `index` of a MFInt32 field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_int32
        """

    def getMFFloat(self, index: int) -> float:
        """Return the item at `index` of a MFFloat field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_float
        """

    def getMFString(self, index: int) -> str:
        """Return the item at `index` of a MFString field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_string
        """

    def getMFVec2f(self, index: int) -> list[float]:
        """Return the item `[x, y]` at `index` of a MFVec2f field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_vec2f
        """

    def getMFVec3f(self, index: int) -> list[float]:
        """Return the item `[x, y, z]` at `index` of a MFVec3f field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_vec3f
        """

    def getMFRotation(self, index: int) -> list[float]:
        """Return the item `[x, y, z, angle]` at `index` of a MFRotation field [rad].

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_rotation
        """

    def getMFColor(self, index: int) -> list[float]:
        """Return the item `[r, g, b]` at `index` of a MFColor field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_color
        """

    def getMFNode(self, index: int) -> Node | None:
        """Return the node at `index` of a MFNode field, or `None` if there is none.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_node
        """

    def setSFBool(self, value: bool) -> None:
        """Set the value of a SFBool field.

        Pass a real bool; any other type only prints an error message to stderr.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_sf_bool
        """

    def setSFInt32(self, value: int) -> None:
        """Set the value of a SFInt32 field.

        Pass an int; any other type only prints an error message to stderr.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_sf_int32
        """

    def setSFFloat(self, value: float) -> None:
        """Set the value of a SFFloat field.

        Pass a float: an int is rejected (error message on stderr, no effect).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_sf_float
        """

    def setSFVec2f(self, value: list[float]) -> None:
        """Set the value `[x, y]` of a SFVec2f field.

        Pass a list (not a tuple) of the exact length; otherwise only an error message is printed to stderr.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_sf_vec2f
        """

    def setSFVec3f(self, value: list[float]) -> None:
        """Set the value `[x, y, z]` of a SFVec3f field.

        Pass a list (not a tuple) of the exact length; otherwise only an error message is printed to stderr.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_sf_vec3f
        """

    def setSFRotation(self, value: list[float]) -> None:
        """Set the value `[x, y, z, angle]` of a SFRotation field [rad].

        Pass a list (not a tuple) of the exact length; otherwise only an error message is printed to stderr.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_sf_rotation
        """

    def setSFColor(self, value: list[float]) -> None:
        """Set the value `[r, g, b]` of a SFColor field.

        Pass a list (not a tuple) of the exact length; otherwise only an error message is printed to stderr.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_sf_color
        """

    def setSFString(self, value: str) -> None:
        """Set the value of a SFString field.

        Pass a str; any other type only prints an error message to stderr.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_sf_string
        """

    def setMFBool(self, index: int, value: bool) -> None:
        """Set the item at `index` of a MFBool field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_mf_bool
        """

    def setMFInt32(self, index: int, value: int) -> None:
        """Set the item at `index` of a MFInt32 field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_mf_int32
        """

    def setMFFloat(self, index: int, value: float) -> None:
        """Set the item at `index` of a MFFloat field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_mf_float
        """

    def setMFVec2f(self, index: int, value: list[float]) -> None:
        """Set the item at `index` `[x, y]` of a MFVec2f field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_mf_vec2f
        """

    def setMFVec3f(self, index: int, value: list[float]) -> None:
        """Set the item at `index` `[x, y, z]` of a MFVec3f field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_mf_vec3f
        """

    def setMFRotation(self, index: int, value: list[float]) -> None:
        """Set the item at `index` `[x, y, z, angle]` of a MFRotation field [rad].

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_mf_rotation
        """

    def setMFColor(self, index: int, value: list[float]) -> None:
        """Set the item at `index` `[r, g, b]` of a MFColor field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_mf_color
        """

    def setMFString(self, index: int, value: str) -> None:
        """Set the item at `index` of a MFString field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_set_mf_string
        """

    def insertMFBool(self, index: int, value: bool) -> None:
        """Insert an item at `index` (-1 appends) of a MFBool field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_insert_mf_bool
        """

    def insertMFInt32(self, index: int, value: int) -> None:
        """Insert an item at `index` (-1 appends) of a MFInt32 field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_insert_mf_int32
        """

    def insertMFFloat(self, index: int, value: float) -> None:
        """Insert an item at `index` (-1 appends) of a MFFloat field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_insert_mf_float
        """

    def insertMFVec2f(self, index: int, value: list[float]) -> None:
        """Insert an item at `index` (-1 appends) `[x, y]` of a MFVec2f field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_insert_mf_vec2f
        """

    def insertMFVec3f(self, index: int, value: list[float]) -> None:
        """Insert an item at `index` (-1 appends) `[x, y, z]` of a MFVec3f field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_insert_mf_vec3f
        """

    def insertMFRotation(self, index: int, value: list[float]) -> None:
        """Insert an item at `index` (-1 appends) `[x, y, z, angle]` of a MFRotation field [rad].

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_insert_mf_rotation
        """

    def insertMFColor(self, index: int, value: list[float]) -> None:
        """Insert an item at `index` (-1 appends) `[r, g, b]` of a MFColor field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_insert_mf_color
        """

    def insertMFString(self, index: int, value: str) -> None:
        """Insert an item at `index` (-1 appends) of a MFString field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_insert_mf_string
        """

    def removeMF(self, index: int) -> None:
        """Remove the item at `index` of a multiple field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_remove_mf
        """

    def removeSF(self) -> None:
        """Remove the node held by a SFNode field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_remove_sf
        """

    def importMFNodeFromString(self, position: int, nodeString: str) -> None:
        """Import the node described by `nodeString` (world-file syntax) at `position` of a MFNode field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_import_mf_node_from_string
        """

    def importSFNodeFromString(self, nodeString: str) -> None:
        """Import the node described by `nodeString` (world-file syntax) into a SFNode field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_import_sf_node_from_string
        """

    @property
    def name(self) -> str:
        """The name of the field (same as `getName()`)."""

    @property
    def type_name(self) -> str:
        """The VRML name of the field type (same as `getTypeName()`)."""

    @property
    def count(self) -> int:
        """The number of items of a multiple field, or -1 for a single field (same as `getCount()`)."""

    @property
    def value(self) -> bool | int | float | str | list[float] | Node | None:
        """The value of a single field (same as the matching `getSF*()`), or `None` for a multiple field.

        Pass a float for a SFFloat field (an int is rejected), a real bool for SFBool and a list (not a tuple)
        of the exact length for vectors; otherwise only an error message is printed to stderr and nothing is
        set. Node values cannot be assigned.
        """

    @value.setter
    def value(self, value: bool | float | str | list[float]) -> None: ...
