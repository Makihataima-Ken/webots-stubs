"""Type-checking tests for controller.node and controller.field (checked by mypy and pyright, never run)."""

from typing import Final

from typing_extensions import assert_type

from controller import Field, Node, Proto
from controller.node import ContactPoint

node = Node(DEF="ROBOT")
root = Node()
assert_type(Node(selected=True), Node)
assert_type(Node(id=3), Node)
assert_type(Node(tag=0), Node)

assert_type(node.getDef(), str)
assert_type(node.DEF, str)
assert_type(node.getId(), int)
assert_type(node.id, int)
assert_type(node.getType(), int)
assert_type(node.type, int)
assert_type(node.getTypeName(), str)
assert_type(node.type_name, str)
assert_type(node.getBaseTypeName(), str)
assert_type(node.base_type_name, str)
assert_type(node.getNumberOfFields(), int)
assert_type(node.number_of_fields, int)
assert_type(node.getNumberOfBaseNodeFields(), int)
assert_type(node.number_of_base_node_fields, int)
assert_type(node.isProto(), bool)
assert_type(node.exportString(), str)

# Lookups that can fail return None.
assert_type(node.getParentNode(), Node | None)
assert_type(node.getProto(), Proto | None)
assert_type(node.getFromProtoDef("BODY"), Node | None)
assert_type(node.getField("translation"), Field | None)
assert_type(node.getFieldByIndex(0), Field | None)
assert_type(node.getBaseNodeField("translation"), Field | None)
assert_type(node.getBaseNodeFieldByIndex(0), Field | None)

assert_type(node.getPosition(), list[float])
assert_type(node.getOrientation(), list[float])
assert_type(node.getPose(), list[float])
assert_type(node.getPose(root), list[float])
assert_type(node.getCenterOfMass(), list[float])
assert_type(node.getVelocity(), list[float])
assert_type(node.getStaticBalance(), bool)
node.enablePoseTracking(32)
node.enablePoseTracking(32, fromNode=root)
node.disablePoseTracking()
node.setVelocity([0.0, 0.0, 1.0, 0.0, 0.0, 0.0])
node.setVelocity((0.0, 0.0, 1.0, 0.0, 0.0, 0.0))
node.setJointPosition(0.5)
node.setJointPosition(0.5, 2)
node.setVisibility(root, False)
node.addForce([0.0, 0.0, 10.0], True)
node.addForce((0, 0, 10), True)
node.addForceWithOffset([0.0, 0.0, 10.0], [0.1, 0.0, 0.0], False)
node.addForceWithOffset((0.0, 0.0, 10.0), (0.1, 0.0, 0.0), False)
node.addTorque([0.0, 1.0, 0.0], False)
node.addTorque((0.0, 1.0, 0.0), False)
node.saveState("start")
node.loadState("start")
node.resetPhysics()
node.remove()

contacts = node.getContactPoints()
assert_type(contacts, list[ContactPoint])
node.enableContactPointsTracking(32, True)
node.disableContactPointsTracking()
for contact in contacts:
    assert_type(contact.getPoint(), tuple[float, float, float])
    assert_type(contact.point, tuple[float, float, float])
    assert_type(contact.getNodeId(), int)
    assert_type(contact.node_id, int)

# Node type constants.
assert_type(Node.ROBOT, int)
assert_type(Node.NO_NODE, int)
assert_type(Node.RADIO, int)
is_camera: bool = node.getType() == Node.CAMERA

parent = node.getParentNode()
if parent is not None:
    assert_type(parent.getDef(), str)

# Fields.
field = node.getField("translation")
assert field is not None
assert_type(field.getName(), str)
assert_type(field.name, str)
assert_type(field.getTypeName(), str)
assert_type(field.type_name, str)
assert_type(field.getType(), int)
assert_type(field.type, int)
assert_type(field.getCount(), int)
assert_type(field.count, int)
assert_type(field.getActualField(), Field | None)
assert_type(Field.SF_VEC3F, int)
assert_type(Field.MF_NODE, int)
is_sf_vec3f: bool = field.getType() == Field.SF_VEC3F
field.enableSFTracking(16)
field.disableSFTracking()

assert_type(field.getSFBool(), int)
assert_type(field.getSFInt32(), int)
assert_type(field.getSFFloat(), float)
assert_type(field.getSFVec2f(), list[float])
assert_type(field.getSFVec3f(), list[float])
assert_type(field.getSFRotation(), list[float])
assert_type(field.getSFColor(), list[float])
assert_type(field.getSFString(), str)
assert_type(field.getSFNode(), Node | None)

assert_type(field.getMFBool(0), bool)
assert_type(field.getMFInt32(0), int)
assert_type(field.getMFFloat(0), float)
assert_type(field.getMFString(0), str)
assert_type(field.getMFVec2f(0), list[float])
assert_type(field.getMFVec3f(0), list[float])
assert_type(field.getMFRotation(0), list[float])
assert_type(field.getMFColor(-1), list[float])
assert_type(field.getMFNode(0), Node | None)

field.setSFBool(True)
field.setSFInt32(1)
field.setSFFloat(0.5)
field.setSFVec2f([0.0, 1.0])
field.setSFVec3f([0.0, 1.0, 2.0])
field.setSFRotation([0.0, 0.0, 1.0, 1.57])
field.setSFColor([1.0, 0.0, 0.0])
field.setSFString("text")

field.setMFBool(0, True)
field.setMFInt32(0, 1)
field.setMFFloat(0, 0.5)
field.setMFVec2f(0, [0.0, 1.0])
field.setMFVec3f(0, [0.0, 1.0, 2.0])
field.setMFRotation(0, [0.0, 0.0, 1.0, 1.57])
field.setMFColor(0, [1.0, 0.0, 0.0])
field.setMFString(0, "text")
field.insertMFBool(-1, True)
field.insertMFInt32(-1, 1)
field.insertMFFloat(-1, 0.5)
field.insertMFVec2f(-1, [0.0, 1.0])
field.insertMFVec3f(-1, [0.0, 1.0, 2.0])
field.insertMFRotation(-1, [0.0, 0.0, 1.0, 1.57])
field.insertMFColor(-1, [1.0, 0.0, 0.0])
# The MF vector setters unpack their value, so any sequence works (the SF setters need a list).
field.setMFVec2f(0, (0.0, 1.0))
field.setMFVec3f(0, (0, 1, 2))
field.setMFRotation(0, (0.0, 0.0, 1.0, 1.57))
field.setMFColor(0, (1.0, 0.0, 0.0))
field.insertMFVec2f(-1, (0.0, 1.0))
field.insertMFVec3f(-1, (0.0, 1.0, 2.0))
field.insertMFRotation(-1, (0.0, 0.0, 1.0, 1.57))
field.insertMFColor(-1, (1.0, 0.0, 0.0))
field.insertMFString(-1, "text")
field.removeMF(0)
field.removeSF()
field.importMFNodeFromString(-1, "Solid {}")
field.importSFNodeFromString("Solid {}")

# The generic value property depends on the field type: narrow it before use.
value = field.value
assert_type(value, bool | int | float | str | list[float] | Node | None)
field.value = [0.0, 1.0, 2.0]
field.value = 1.5
field.value = "text"

limit: Final = field.getSFVec3f()[2]
assert_type(limit, float)
