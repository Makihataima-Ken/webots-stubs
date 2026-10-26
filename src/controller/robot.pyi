import sys
from typing import Any, ClassVar, Final

from typing_extensions import deprecated

from .accelerometer import Accelerometer
from .altimeter import Altimeter
from .brake import Brake
from .camera import Camera
from .compass import Compass
from .connector import Connector
from .device import Device
from .display import Display
from .distance_sensor import DistanceSensor
from .emitter import Emitter
from .gps import GPS
from .gyro import Gyro
from .inertial_unit import InertialUnit
from .joystick import Joystick
from .keyboard import Keyboard
from .led import LED
from .lidar import Lidar
from .light_sensor import LightSensor
from .motor import Motor
from .mouse import Mouse
from .pen import Pen
from .position_sensor import PositionSensor
from .radar import Radar
from .range_finder import RangeFinder
from .receiver import Receiver
from .skin import Skin
from .speaker import Speaker
from .touch_sensor import TouchSensor

if sys.platform == "win32":
    class StdStreamRedirect:
        """Forwards Python's stdout or stderr to the Webots console on Windows (internal helper)."""

        def __init__(self, stream: int) -> None: ...
        def __del__(self) -> None: ...

class Robot:
    """The robot running the controller: simulation stepping, device access and robot-wide settings.

    Only one `Robot` (or `Supervisor`) instance can be created per controller process.
    A typical controller looks like this:

        robot = Robot()
        timestep = int(robot.getBasicTimeStep())
        motor: Motor = robot.getDevice("left wheel motor")
        while robot.step(timestep) != -1:
            motor.setVelocity(1.0)

    Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python
    """

    EVENT_QUIT: Final = -1
    """`waitForUserInputEvent()` result: Webots is about to terminate the controller."""
    EVENT_NO_EVENT: Final = 0
    """`waitForUserInputEvent()` event type: no event; waits for the whole timeout."""
    EVENT_MOUSE_CLICK: Final = 1
    """`waitForUserInputEvent()` event type: mouse click in the 3D view."""
    EVENT_MOUSE_MOVE: Final = 2
    """`waitForUserInputEvent()` event type: mouse motion in the 3D view."""
    EVENT_KEYBOARD: Final = 4
    """`waitForUserInputEvent()` event type: keyboard key press or release."""
    EVENT_JOYSTICK_BUTTON: Final = 8
    """`waitForUserInputEvent()` event type: joystick button press or release."""
    EVENT_JOYSTICK_AXIS: Final = 16
    """`waitForUserInputEvent()` event type: joystick axis motion."""
    EVENT_JOYSTICK_POV: Final = 32
    """`waitForUserInputEvent()` event type: joystick point-of-view change."""
    MODE_SIMULATION: Final = 0
    """`getMode()` result: the controller drives the simulated robot."""
    MODE_CROSS_COMPILATION: Final = 1
    """`getMode()` result: the controller is cross-compiled for the real robot."""
    MODE_REMOTE_CONTROL: Final = 2
    """`getMode()` result: the controller drives the real robot through a remote-control plugin."""

    created: ClassVar[Robot | None]
    """The `Robot` instance of this controller process, once created."""
    devices: dict[str, Device]
    """All the devices of the robot, by name."""
    keyboard: Keyboard
    """The keyboard of the computer running Webots (same as `getKeyboard()`)."""
    mouse: Mouse
    """The mouse of the computer running Webots (same as `getMouse()`)."""
    joystick: Joystick
    """The joystick connected to the computer running Webots (same as `getJoystick()`)."""

    def __init__(self) -> None:
        """Initialize the controller and connect it to Webots. Only one instance may be created."""

    def __del__(self) -> None: ...
    @deprecated("Use Robot.getDevice() instead.")
    def getAccelerometer(self, name: str) -> Accelerometer:
        """Return the Accelerometer device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getAltimeter(self, name: str) -> Altimeter:
        """Return the Altimeter device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getBrake(self, name: str) -> Brake:
        """Return the Brake device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getCamera(self, name: str) -> Camera:
        """Return the Camera device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getCompass(self, name: str) -> Compass:
        """Return the Compass device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getConnector(self, name: str) -> Connector:
        """Return the Connector device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getDisplay(self, name: str) -> Display:
        """Return the Display device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getDistanceSensor(self, name: str) -> DistanceSensor:
        """Return the DistanceSensor device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getEmitter(self, name: str) -> Emitter:
        """Return the Emitter device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getGPS(self, name: str) -> GPS:
        """Return the GPS device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getGyro(self, name: str) -> Gyro:
        """Return the Gyro device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getInertialUnit(self, name: str) -> InertialUnit:
        """Return the InertialUnit device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getLED(self, name: str) -> LED:
        """Return the LED device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getLidar(self, name: str) -> Lidar:
        """Return the Lidar device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getLightSensor(self, name: str) -> LightSensor:
        """Return the LightSensor device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getMotor(self, name: str) -> Motor:
        """Return the Motor device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getPen(self, name: str) -> Pen:
        """Return the Pen device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getPositionSensor(self, name: str) -> PositionSensor:
        """Return the PositionSensor device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getRadar(self, name: str) -> Radar:
        """Return the Radar device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getRangeFinder(self, name: str) -> RangeFinder:
        """Return the RangeFinder device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getReceiver(self, name: str) -> Receiver:
        """Return the Receiver device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getSkin(self, name: str) -> Skin:
        """Return the Skin device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getSpeaker(self, name: str) -> Speaker:
        """Return the Speaker device called `name`. Deprecated: use `getDevice()`."""

    @deprecated("Use Robot.getDevice() instead.")
    def getTouchSensor(self, name: str) -> TouchSensor:
        """Return the TouchSensor device called `name`. Deprecated: use `getDevice()`."""

    def getDevice(self, name: str) -> Any:
        """Return the device whose `name` field is `name`, or `None` (with an error message) if there is none.

        The result is an instance of the matching `Device` subclass. It is typed `Any`
        because the class depends on the robot model; annotate the variable to get
        completion and type checking:

            motor: Motor = robot.getDevice("left wheel motor")

        If several devices share the same name, the first one is returned.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_device
        """

    def getKeyboard(self) -> Keyboard:
        """Return the keyboard of the computer running Webots. Enable it before reading keys.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_device
        """

    def getMouse(self) -> Mouse:
        """Return the mouse of the computer running Webots. Enable it before reading its state.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_device
        """

    def getJoystick(self) -> Joystick:
        """Return the joystick connected to the computer running Webots. Enable it before reading it.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_device
        """

    def getDeviceByIndex(self, index: int) -> Device:
        """Return the device at `index` in the robot's device list (scene tree order).

        Valid indices go from 0 to `getNumberOfDevices() - 1`.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_device_by_index
        """

    def getBasicTimeStep(self) -> float:
        """Return the `basicTimeStep` field of the WorldInfo node [ms].

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_basic_time_step
        """

    def getName(self) -> str:
        """Return the `name` field of the robot node.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_name
        """

    def getModel(self) -> str:
        """Return the `model` field of the robot node.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_model
        """

    def getCustomData(self) -> str:
        """Return the `customData` field of the robot node.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_custom_data
        """

    def setCustomData(self, data: str) -> None:
        """Set the `customData` field of the robot node.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_set_custom_data
        """

    def getProjectPath(self) -> str:
        """Return the full path of the current project (the directory containing `worlds` and `controllers`).

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_project_path
        """

    def getWorldPath(self) -> str:
        """Return the full path of the current world file, including the `.wbt` extension.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_world_path
        """

    def getSupervisor(self) -> bool:
        """Return the `supervisor` field of the robot node, i.e. whether the Supervisor API may be used.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_supervisor
        """

    def getSynchronization(self) -> bool:
        """Return the `synchronization` field of the robot node.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_synchronization
        """

    def getNumberOfDevices(self) -> int:
        """Return the number of devices of the robot.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_number_of_devices
        """

    def getTime(self) -> float:
        """Return the current simulation time [s].

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_time
        """

    def getUrdf(self, prefix: str = "") -> str:
        """Export the robot model as URDF, prefixing link and joint names with `prefix`.

        The export is minimal, aimed at tools such as `robot_state_publisher` and RViz.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_urdf
        """

    def wwiSendText(self, text: str) -> None:
        """Send a text message to the JavaScript code of the robot's HTML robot window.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_wwi_send_text
        """

    def wwiReceiveText(self) -> str | None:
        """Return the next text message received from the HTML robot window, or `None` if there is none.

        Call it repeatedly until it returns `None` to read all the messages of the step.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_wwi_receive_text
        """

    def step(self, time_step: int | None = None) -> int:
        """Run the simulation for `time_step` milliseconds (default: the world's basic time step).

        This synchronizes sensor and actuator data with Webots and must be called in
        every controller loop. `time_step` must be a multiple of the basic time step.
        Returns -1 when Webots is about to terminate the controller (leaving one second
        for cleanup), otherwise 0 for a synchronized controller.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_step
        """

    def stepBegin(self, time_step: int | None = None) -> int:
        """Start a simulation step of `time_step` milliseconds that runs in parallel with the controller.

        Code placed between `stepBegin()` and `stepEnd()` runs while Webots simulates
        the step. Returns -1 when Webots is about to terminate the controller.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_step_begin
        """

    def stepEnd(self) -> int:
        """Wait for the step started by `stepBegin()` to finish and fetch the new sensor values.

        Returns -1 when Webots is about to terminate the controller.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_step_end
        """

    def waitForUserInputEvent(self, event_type: int, timeout: int) -> int:
        """Block until one of the `event_type` input events occurs or `timeout` real-time milliseconds pass.

        `event_type` combines `Robot.EVENT_*` flags with `|`; the corresponding input
        devices must be enabled. Returns the event that occurred, `EVENT_NO_EVENT` on
        timeout or `EVENT_QUIT` when the controller is about to terminate.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_wait_for_user_input_event
        """

    def batterySensorEnable(self, sampling_period: int) -> None:
        """Start measuring the battery energy level every `sampling_period` milliseconds.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_battery_sensor_enable
        """

    def batterySensorDisable(self) -> None:
        """Stop the battery energy level measurements.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_battery_sensor_disable
        """

    def batterySensorGetSamplingPeriod(self) -> int:
        """Return the sampling period of the battery sensor [ms], or 0 if it is disabled.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_battery_sensor_get_sampling_period
        """

    def batterySensorGetValue(self) -> float:
        """Return the current energy level of the robot battery [J], or -1 if the `battery` field is empty.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_battery_sensor_get_value
        """

    def getMode(self) -> int:
        """Return the operating mode: `MODE_SIMULATION`, `MODE_CROSS_COMPILATION` or `MODE_REMOTE_CONTROL`.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_get_mode
        """

    def setMode(self, mode: int, arg: str) -> None:
        """Switch between `MODE_SIMULATION` and `MODE_REMOTE_CONTROL`.

        `arg` is passed to the `wbr_start` function of the remote-control plugin.

        Reference: https://cyberbotics.com/doc/reference/robot?tab-language=python#wb_robot_set_mode
        """

    @property
    def basic_time_step(self) -> float:
        """The `basicTimeStep` field of the WorldInfo node [ms] (same as `getBasicTimeStep()`)."""

    @property
    def name(self) -> str:
        """The `name` field of the robot node (same as `getName()`)."""

    @property
    def model(self) -> str:
        """The `model` field of the robot node (same as `getModel()`)."""

    @property
    def custom_data(self) -> str:
        """The `customData` field of the robot node (same as `getCustomData()` / `setCustomData()`)."""

    @custom_data.setter
    def custom_data(self, data: str) -> None: ...
    @property
    def project_path(self) -> str:
        """The full path of the current project (same as `getProjectPath()`)."""

    @property
    def world_path(self) -> str:
        """The full path of the current world file (same as `getWorldPath()`)."""

    @property
    def supervisor(self) -> bool:
        """The `supervisor` field of the robot node (same as `getSupervisor()`)."""

    @property
    def synchronization(self) -> bool:
        """The `synchronization` field of the robot node (same as `getSynchronization()`)."""

    @property
    def time(self) -> float:
        """The current simulation time [s] (same as `getTime()`)."""

    @property
    def number_of_devices(self) -> int:
        """The number of devices of the robot (same as `getNumberOfDevices()`)."""

    @property
    def battery_sensor_sampling_period(self) -> int:
        """Sampling period of the battery sensor [ms], 0 when disabled. Setting it enables the sensor.

        Setting it to `None` enables the sensor with the basic time step.
        """

    @battery_sensor_sampling_period.setter
    def battery_sensor_sampling_period(self, sampling_period: int | None) -> None: ...
    @property
    def mode(self) -> int:
        """The operating mode of the controller (same as `getMode()`)."""
