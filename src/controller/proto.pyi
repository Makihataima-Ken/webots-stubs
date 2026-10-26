from .field import Field

class Proto:
    """A PROTO definition: its type name, parent PROTO and fields.

    Obtained from `Node.getProto()` or `Proto.getParent()`.

    Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python
    """

    def __init__(self, ref: int) -> None: ...
    def getTypeName(self) -> str:
        """Return the PROTO type name (same as `type_name`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_proto_get_type_name
        """

    def getParent(self) -> Proto | None:
        """Return the PROTO this one derives from, or `None` if it is not derived from another PROTO.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_proto_get_parent
        """

    def getField(self, name: str) -> Field | None:
        """Return the field called `name` of this PROTO, or `None` if there is no such field.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_proto_get_field
        """

    def getFieldByIndex(self, index: int) -> Field | None:
        """Return the field at `index` (0 to `getNumberOfFields() - 1`), or `None` if out of range.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_proto_get_field_by_index
        """

    def getNumberOfFields(self) -> int:
        """Return the number of fields of this PROTO (same as `number_of_fields`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_proto_get_number_of_fields
        """

    def isDerived(self) -> bool:
        """Return whether this PROTO derives from another PROTO (same as `is_derived`).

        Note: in R2025a the C function is called without its `type_name` argument, so the result is unreliable.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_proto_is_derived
        """

    @property
    def type_name(self) -> str:
        """The PROTO type name (same as `getTypeName()`)."""

    @property
    def number_of_fields(self) -> int:
        """The number of fields of this PROTO (same as `getNumberOfFields()`)."""

    @property
    def is_derived(self) -> bool:
        """Whether this PROTO derives from another PROTO (same as `isDerived()`).

        Note: in R2025a the result is unreliable (see `isDerived()`).
        """
