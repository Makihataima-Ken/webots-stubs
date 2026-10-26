from typing import Final

from .node import Node
from .robot import Robot

class Supervisor(Robot):
    """A `Robot` with supervisor powers over the scene tree and the simulation.

    A supervisor can inspect and modify the scene tree, control the simulation and record
    movies and animations. The `supervisor` field of the robot must be TRUE. Only one
    `Robot` or `Supervisor` instance can be created.

    Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python
    """

    SIMULATION_MODE_PAUSE: Final = 0
    """Simulation mode: the simulation is paused."""
    SIMULATION_MODE_REAL_TIME: Final = 1
    """Simulation mode: the simulation runs as close as possible to real time."""
    SIMULATION_MODE_FAST: Final = 2
    """Simulation mode: the simulation runs as fast as possible, without graphical rendering."""

    def __init__(self) -> None:
        """Initialize the controller and connect it to Webots. Only one instance may be created."""

    def getRoot(self) -> Node:
        """Return the root node of the scene tree (the parent of all the world's top-level nodes).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_root
        """

    def getSelf(self) -> Node:
        """Return the node of the robot running this controller.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_self
        """

    def getFromDef(self, d: str) -> Node | None:
        """Return the node with the DEF name `d`, or `None` if there is none.

        Dots scope the search along a node path (e.g. `"ROBOT.JOINT"`). Internal nodes of a PROTO are not found:
        use `Node.getFromProtoDef()` for those.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_from_def
        """

    def getFromId(self, id: int) -> Node | None:
        """Return the node with the unique identifier `id` (see `Node.getId()`), or `None` if there is none.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_from_id
        """

    def getFromDevice(self, tag: int) -> Node | None:
        """Return the node of the device with the given `tag`, or `None` if it cannot be found.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_from_device
        """

    def getSelected(self) -> Node | None:
        """Return the node currently selected in the Webots scene tree, or `None` if nothing is selected.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_node_get_selected
        """

    def setLabel(
        self,
        id: int,
        label: str,
        x: float,
        y: float,
        size: float,
        color: int,
        transparency: float = 0,
        font: str = "Arial",
    ) -> None:
        """Overlay a text label on the 3D view.

        `id` (0 to 65534) identifies the label so it can be updated later. `x`, `y` and `size` are fractions (0 to 1)
        of the 3D window, `color` is 0xRRGGBB, `transparency` goes from 0 (opaque) to 1 (invisible).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_set_label
        """

    def simulationQuit(self, status: int) -> None:
        """Terminate the simulation and Webots, with `status` as the exit code.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_simulation_quit
        """

    def simulationSetMode(self, mode: int) -> None:
        """Set the simulation mode (`SIMULATION_MODE_PAUSE`, `SIMULATION_MODE_REAL_TIME` or `SIMULATION_MODE_FAST`).

        Same as setting `simulation_mode`.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_simulation_set_mode
        """

    def simulationGetMode(self) -> int:
        """Return the simulation mode, updated at the last call of `step()` (same as `simulation_mode`).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_simulation_get_mode
        """

    def simulationReset(self) -> None:
        """Reset the simulation to its initial state and restart the controllers.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_simulation_reset
        """

    def simulationResetPhysics(self) -> None:
        """Stop the inertial movement of all solids, without changing their positions.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_simulation_reset_physics
        """

    def worldLoad(self, filename: str) -> None:
        """Load the world file `filename`; all controllers are terminated and restarted.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_world_load
        """

    def worldSave(self, filename: str | None = None) -> int:
        """Save the current world to `filename` (a `.wbt` path), or to its current file if omitted.

        Return a non-zero value on success. Existing files are overwritten silently.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_world_save
        """

    def worldReload(self) -> None:
        """Reload the current world; all controllers are terminated and restarted.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_world_reload
        """

    def exportImage(self, filename: str, quality: int) -> None:
        """Save the current image of the 3D view to the JPEG file `filename`.

        `quality` is the JPEG quality (1 to 100). An existing file is overwritten silently.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_export_image
        """

    def movieStartRecording(
        self,
        filename: str,
        width: int,
        height: int,
        codec: int,
        quality: int,
        acceleration: int,
        caption: bool,
    ) -> None:
        """Start recording the simulation to the MP4 movie `filename`.

        The `.mp4` extension is added if missing. `codec` is ignored (MPEG-4/AVC only). `quality` is the compression
        factor (1 to 100) and `acceleration` the speed-up relative to simulated time (1 for none). `caption` prints
        the acceleration on the movie.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_movie_start_recording
        """

    def movieStopRecording(self) -> None:
        """Stop the movie recording and finish encoding the file.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_movie_stop_recording
        """

    def movieIsReady(self) -> bool:
        """Return whether no recording or encoding is in progress (also `True` after a failure).

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_movie_is_ready
        """

    def movieFailed(self) -> bool:
        """Return whether the last movie recording failed.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_movie_failed
        """

    def animationStartRecording(self, filename: str) -> int:
        """Start recording an HTML5 animation to `filename` (a `.html` path).

        Return a non-zero value on success.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_animation_start_recording
        """

    def animationStopRecording(self) -> int:
        """Stop the animation recording. Return a non-zero value on success.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_animation_stop_recording
        """

    def virtualRealityHeadsetIsUsed(self) -> bool:
        """Return whether a virtual reality headset is currently used to view the simulation.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_virtual_reality_headset_is_used
        """

    def virtualRealityHeadsetGetPosition(self) -> list[float]:
        """Return the position [x, y, z] of the virtual reality headset [m].

        Values are NaN if the position is not tracked or no headset is used.

        Note: in R2025a this call returns a NULL ctypes pointer instead of a list (field.py rebinds the C function),
        so indexing the result raises `ValueError`.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_virtual_reality_headset_get_position
        """

    def virtualRealityHeadsetGetOrientation(self) -> list[float]:
        """Return the orientation of the virtual reality headset as a 3x3 rotation matrix (9 values, row-major).

        Values are NaN if the orientation is not tracked or no headset is used.

        Note: in R2025a this call returns a NULL ctypes pointer instead of a list (field.py rebinds the C function),
        so indexing the result raises `ValueError`.

        Reference: https://cyberbotics.com/doc/reference/supervisor?tab-language=python#wb_supervisor_virtual_reality_headset_get_orientation
        """

    @property
    def simulation_mode(self) -> int:
        """The simulation mode (same as `simulationGetMode()` / `simulationSetMode()`)."""

    @simulation_mode.setter
    def simulation_mode(self, mode: int) -> None: ...
