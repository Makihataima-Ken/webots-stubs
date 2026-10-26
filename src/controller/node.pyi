from collections.abc import Sequence
from typing import Final

from .field import Field
from .proto import Proto

class ContactPoint:
    """A contact point of a solid, in world coordinates, as returned by `Node.getContactPoints()`.

    Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_contact_points
    """

    point: tuple[float, float, float]
    """The position of the contact point [m]."""
    node_id: int
    """The id of the node the contact point belongs to (same as `Node.getId()`)."""

    def __init__(self, point: tuple[float, float, float, int]) -> None:
        """Build a contact point from the `(x, y, z, node_id)` tuple returned by the C library."""

    def getPoint(self) -> tuple[float, float, float]:
        """Return the position of the contact point in world coordinates [m]."""

    def getNodeId(self) -> int:
        """Return the id of the node the contact point belongs to."""

class Node:
    """A node of the simulated scene tree, accessible from a Supervisor controller.

    Nodes are obtained with the `Supervisor` methods (`getRoot()`, `getFromDef()`, `getSelf()`, ...) or built
    directly: `Node()` is the root node, `Node(DEF="name")` a node from its DEF name, `Node(tag=...)` the node of
    a device, `Node(id=...)` a node from its id and `Node(selected=True)` the selected node. When the node
    does not exist, the constructor still returns an object, whose methods have no effect.

    Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python
    """

    def __init__(
        self,
        DEF: str | None = None,
        tag: int | None = None,
        id: int | None = None,
        selected: bool | None = None,
        ref: int | None = None,
    ) -> None:
        """Wrap a node of the scene tree, looked up by DEF name, device tag, id or selection, or the root node.

        Only one of the arguments is used, in the order `ref`, `id`, `tag` (0 for the robot itself), `DEF`,
        `selected`. `ref` is a raw node handle used internally.
        """

    def getDef(self) -> str:
        """Return the DEF name of the node, or "" if it has none (same as the `DEF` property).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_def
        """

    def getId(self) -> int:
        """Return the unique identifier of the node (same as the `id` property).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_id
        """

    def getParentNode(self) -> Node | None:
        """Return the direct parent of the node, or `None` if it has none (e.g. the root node).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_parent_node
        """

    def isProto(self) -> bool:
        """Return `True` if the node is a PROTO node.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_is_proto
        """

    def getProto(self) -> Proto | None:
        """Return the PROTO instance corresponding to the node, or `None` if the node is not a PROTO.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_proto
        """

    def getFromProtoDef(self, DEF: str) -> Node | None:
        """Return the node defined with the given DEF name in the body of this PROTO node, or `None`.

        Only works on PROTO nodes.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_from_proto_def
        """

    def getType(self) -> int:
        """Return the type of the node, to compare with the `Node` type constants (same as `type`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_type
        """

    def getTypeName(self) -> str:
        """Return the name of the node: the PROTO name for a PROTO node, else the base type name.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_type_name
        """

    def getBaseTypeName(self) -> str:
        """Return the base (Webots) type name of the node, like "Robot" or "Appearance".

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_base_type_name
        """

    def remove(self) -> None:
        """Remove the node from the scene tree.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_remove
        """

    def exportString(self) -> str:
        """Return the world-file text from which the node can be built again.

        Use it with `Field.importMFNodeFromString()` to duplicate the node.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_export_string
        """

    def getField(self, fieldName: str) -> Field | None:
        """Return the field called `fieldName` of the node, or `None` if there is no such field.

        Hidden fields are also returned.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_field
        """

    def getFieldByIndex(self, index: int) -> Field | None:
        """Return the field at `index` (from 0 to `getNumberOfFields() - 1`), or `None` if it is out of range.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_field_by_index
        """

    def getNumberOfFields(self) -> int:
        """Return the number of fields of the node (same as `number_of_fields`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_number_of_fields
        """

    def getBaseNodeField(self, fieldName: str) -> Field | None:
        """Return the field of the base (Webots) node called `fieldName`, or `None`.

        Gives access to the internal fields of a PROTO. These fields are read-only.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_base_node_field
        """

    def getBaseNodeFieldByIndex(self, index: int) -> Field | None:
        """Return the base node field at `index`, or `None` if it is out of range. These fields are read-only.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_base_node_field_by_index
        """

    def getNumberOfBaseNodeFields(self) -> int:
        """Return the number of fields of the base node (same as `number_of_base_node_fields`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_number_of_base_node_fields
        """

    def getPosition(self) -> list[float]:
        """Return the position `[x, y, z]` of the node in world coordinates [m].

        The node must be a Pose-derived node (otherwise the values are NaN).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_position
        """

    def getOrientation(self) -> list[float]:
        """Return the 3x3 rotation matrix of the node in world coordinates, as 9 values in row-major order.

        The node must be a Pose-derived node (otherwise the values are NaN).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_orientation
        """

    def getPose(self, fromNode: Node | None = None) -> list[float]:
        """Return the 4x4 homogeneous pose matrix of the node as 16 values in row-major order.

        The pose is expressed in world coordinates, or relative to `fromNode` if given. The translation is in [m].
        The node must be a Pose-derived node (otherwise the values are NaN).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_pose
        """

    def enablePoseTracking(self, samplingPeriod: int, fromNode: Node | None = None) -> None:
        """Make Webots stream the pose of the node to the controller every `samplingPeriod` [ms].

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_enable_pose_tracking
        """

    def disablePoseTracking(self, fromNode: Node | None = None) -> None:
        """Stop the pose tracking started with the same `fromNode` by `enablePoseTracking()`.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_disable_pose_tracking
        """

    def getCenterOfMass(self) -> list[float]:
        """Return the center of mass `[x, y, z]` of a Solid node and its descendants in world coordinates [m].

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_center_of_mass
        """

    def getContactPoints(self, includeDescendants: bool = False) -> list[ContactPoint]:
        """Return the contact points of a Solid node, in world coordinates.

        The node must have no Solid parent. With `includeDescendants`, the descendant solids are included.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_contact_points
        """

    def enableContactPointsTracking(self, samplingPeriod: int, includeDescendants: bool = False) -> None:
        """Make Webots stream the contact points of the node to the controller every `samplingPeriod` [ms].

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_enable_contact_points_tracking
        """

    def disableContactPointsTracking(self, includeDescendants: bool = False) -> None:
        """Stop the contact points tracking. `includeDescendants` is ignored, kept for backward compatibility.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_disable_contact_points_tracking
        """

    def getStaticBalance(self) -> bool:
        """Return the result of the static balance test of a Solid, based on its support polygon.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_static_balance
        """

    def getVelocity(self) -> list[float]:
        """Return the absolute velocity `[vx, vy, vz, wx, wy, wz]` of the node [m/s, rad/s].

        The node must be a Solid.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_velocity
        """

    def setVelocity(self, velocity: Sequence[float]) -> None:
        """Set the absolute velocity `[vx, vy, vz, wx, wy, wz]` of the node [m/s, rad/s].

        The node must be a Solid.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_set_velocity
        """

    def saveState(self, stateName: str) -> None:
        """Save the state of the node and its descendants under the name `stateName`.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_save_state
        """

    def loadState(self, stateName: str) -> None:
        """Restore the state saved under `stateName` (or the initial state with "__init__").

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_load_state
        """

    def resetPhysics(self) -> None:
        """Stop the inertia of the node and its descendants.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_reset_physics
        """

    def setJointPosition(self, position: float, index: int = 1) -> None:
        """Set the position of the joint axis `index` of a joint node [rad or m].

        Valid indices are 1 for hinge and slider joints, 1 or 2 for Hinge2Joint, 1 to 3 for BallJoint.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_set_joint_position
        """

    def restartController(self) -> None:
        """Restart the controller of the Robot node.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_restart_controller
        """

    def moveViewpoint(self) -> None:
        """Move the Viewpoint to the node.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_move_viewpoint
        """

    def setVisibility(self, fromNode: Node, visible: bool) -> None:
        """Show or hide the node (and its children) as seen from the Camera, Lidar, RangeFinder or Viewpoint `fromNode`.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_set_visibility
        """

    def addForce(self, force: Sequence[float], relative: bool) -> None:
        """Add a force `[fx, fy, fz]` [N] to a Solid node at its center of mass.

        The force is in the node's coordinate system if `relative` is `True`, else in world coordinates.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_add_force
        """

    def addForceWithOffset(self, force: Sequence[float], offset: Sequence[float], relative: bool) -> None:
        """Add a force `[fx, fy, fz]` [N] to a Solid node at `offset` `[x, y, z]` in the node's coordinate system [m].

        Note: in R2025a the Python controller library calls `wb_supervisor_node_add_force` with the offset in
        the `relative` slot, so the offset is ignored and a plain force is applied; `relative` is not honoured
        either, as the offset pointer lands in the bool slot.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_add_force_with_offset
        """

    def addTorque(self, torque: Sequence[float], relative: bool) -> None:
        """Add a torque `[tx, ty, tz]` [N⋅m] to a Solid node.

        Note: in R2025a the Python controller library calls `wb_supervisor_node_add_force`, so a force is applied
        instead of a torque.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_add_torque
        """

    @property
    def DEF(self) -> str:
        """The DEF name of the node, or "" if it has none (same as `getDef()`)."""

    @property
    def id(self) -> int:
        """The unique identifier of the node (same as `getId()`)."""

    @property
    def type(self) -> int:
        """The type of the node (same as `getType()`)."""

    @property
    def type_name(self) -> str:
        """The name of the node (same as `getTypeName()`)."""

    @property
    def base_type_name(self) -> str:
        """The base type name of the node (same as `getBaseTypeName()`)."""

    @property
    def number_of_fields(self) -> int:
        """The number of fields of the node (same as `getNumberOfFields()`)."""

    @property
    def number_of_base_node_fields(self) -> int:
        """The number of fields of the base node (same as `getNumberOfBaseNodeFields()`)."""

    NO_NODE: Final[int]
    """Type returned for an invalid or missing node (no node)."""
    APPEARANCE: Final[int]
    """Type of Appearance nodes."""
    BACKGROUND: Final[int]
    """Type of Background nodes."""
    BILLBOARD: Final[int]
    """Type of Billboard nodes."""
    BOX: Final[int]
    """Type of Box nodes."""
    CAD_SHAPE: Final[int]
    """Type of CadShape nodes."""
    CAPSULE: Final[int]
    """Type of Capsule nodes."""
    COLOR: Final[int]
    """Type of Color nodes."""
    CONE: Final[int]
    """Type of Cone nodes."""
    COORDINATE: Final[int]
    """Type of Coordinate nodes."""
    CYLINDER: Final[int]
    """Type of Cylinder nodes."""
    DIRECTIONAL_LIGHT: Final[int]
    """Type of DirectionalLight nodes."""
    ELEVATION_GRID: Final[int]
    """Type of ElevationGrid nodes."""
    FOG: Final[int]
    """Type of Fog nodes."""
    GROUP: Final[int]
    """Type of Group nodes."""
    IMAGE_TEXTURE: Final[int]
    """Type of ImageTexture nodes."""
    INDEXED_FACE_SET: Final[int]
    """Type of IndexedFaceSet nodes."""
    INDEXED_LINE_SET: Final[int]
    """Type of IndexedLineSet nodes."""
    MATERIAL: Final[int]
    """Type of Material nodes."""
    MESH: Final[int]
    """Type of Mesh nodes."""
    MUSCLE: Final[int]
    """Type of Muscle nodes."""
    NORMAL: Final[int]
    """Type of Normal nodes."""
    PBR_APPEARANCE: Final[int]
    """Type of PBRAppearance nodes."""
    PLANE: Final[int]
    """Type of Plane nodes."""
    POINT_LIGHT: Final[int]
    """Type of PointLight nodes."""
    POINT_SET: Final[int]
    """Type of PointSet nodes."""
    SHAPE: Final[int]
    """Type of Shape nodes."""
    SPHERE: Final[int]
    """Type of Sphere nodes."""
    SPOT_LIGHT: Final[int]
    """Type of SpotLight nodes."""
    TEXTURE_COORDINATE: Final[int]
    """Type of TextureCoordinate nodes."""
    TEXTURE_TRANSFORM: Final[int]
    """Type of TextureTransform nodes."""
    TRANSFORM: Final[int]
    """Type of Transform nodes."""
    VIEWPOINT: Final[int]
    """Type of Viewpoint nodes."""
    ROBOT: Final[int]
    """Type of Robot nodes."""
    ACCELEROMETER: Final[int]
    """Type of Accelerometer nodes."""
    ALTIMETER: Final[int]
    """Type of Altimeter nodes."""
    BRAKE: Final[int]
    """Type of Brake nodes."""
    CAMERA: Final[int]
    """Type of Camera nodes."""
    COMPASS: Final[int]
    """Type of Compass nodes."""
    CONNECTOR: Final[int]
    """Type of Connector nodes."""
    DISPLAY: Final[int]
    """Type of Display nodes."""
    DISTANCE_SENSOR: Final[int]
    """Type of DistanceSensor nodes."""
    EMITTER: Final[int]
    """Type of Emitter nodes."""
    GPS: Final[int]
    """Type of GPS nodes."""
    GYRO: Final[int]
    """Type of Gyro nodes."""
    INERTIAL_UNIT: Final[int]
    """Type of InertialUnit nodes."""
    LED: Final[int]
    """Type of LED nodes."""
    LIDAR: Final[int]
    """Type of Lidar nodes."""
    LIGHT_SENSOR: Final[int]
    """Type of LightSensor nodes."""
    LINEAR_MOTOR: Final[int]
    """Type of LinearMotor nodes."""
    PEN: Final[int]
    """Type of Pen nodes."""
    POSITION_SENSOR: Final[int]
    """Type of PositionSensor nodes."""
    RADAR: Final[int]
    """Type of Radar nodes."""
    RANGE_FINDER: Final[int]
    """Type of RangeFinder nodes."""
    RECEIVER: Final[int]
    """Type of Receiver nodes."""
    ROTATIONAL_MOTOR: Final[int]
    """Type of RotationalMotor nodes."""
    SKIN: Final[int]
    """Type of Skin nodes."""
    SPEAKER: Final[int]
    """Type of Speaker nodes."""
    TOUCH_SENSOR: Final[int]
    """Type of TouchSensor nodes."""
    VACUUM_GRIPPER: Final[int]
    """Type of VacuumGripper nodes."""
    BALL_JOINT: Final[int]
    """Type of BallJoint nodes."""
    BALL_JOINT_PARAMETERS: Final[int]
    """Type of BallJointParameters nodes."""
    CHARGER: Final[int]
    """Type of Charger nodes."""
    CONTACT_PROPERTIES: Final[int]
    """Type of ContactProperties nodes."""
    DAMPING: Final[int]
    """Type of Damping nodes."""
    FLUID: Final[int]
    """Type of Fluid nodes."""
    FOCUS: Final[int]
    """Type of Focus nodes."""
    HINGE_JOINT: Final[int]
    """Type of HingeJoint nodes."""
    HINGE_JOINT_PARAMETERS: Final[int]
    """Type of HingeJointParameters nodes."""
    HINGE_2_JOINT: Final[int]
    """Type of Hinge2Joint nodes."""
    IMMERSION_PROPERTIES: Final[int]
    """Type of ImmersionProperties nodes."""
    JOINT_PARAMETERS: Final[int]
    """Type of JointParameters nodes."""
    LENS: Final[int]
    """Type of Lens nodes."""
    LENS_FLARE: Final[int]
    """Type of LensFlare nodes."""
    PHYSICS: Final[int]
    """Type of Physics nodes."""
    RECOGNITION: Final[int]
    """Type of Recognition nodes."""
    SLIDER_JOINT: Final[int]
    """Type of SliderJoint nodes."""
    SLOT: Final[int]
    """Type of Slot nodes."""
    SOLID: Final[int]
    """Type of Solid nodes."""
    SOLID_REFERENCE: Final[int]
    """Type of SolidReference nodes."""
    TRACK: Final[int]
    """Type of Track nodes."""
    TRACK_WHEEL: Final[int]
    """Type of TrackWheel nodes."""
    WORLD_INFO: Final[int]
    """Type of WorldInfo nodes."""
    ZOOM: Final[int]
    """Type of Zoom nodes."""
    MICROPHONE: Final[int]
    """Type of Microphone nodes."""
    RADIO: Final[int]
    """Type of Radio nodes."""

def getSFNode(self: Field) -> Node | None:
    """Return the node of a SFNode field, or `None` if the field is empty (installed as `Field.getSFNode`).

    Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_sf_node
    """

def getMFNode(self: Field, index: int) -> Node | None:
    """Return the node at `index` of a MFNode field, or `None` (installed as `Field.getMFNode`).

    Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_field_get_mf_node
    """
