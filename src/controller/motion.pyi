class Motion:
    """A robot motion loaded from a `.motion` file, played back on the motors of the robot.

    The playback happens in the background as a side effect of `Robot.step()`. Check `isValid()`
    after constructing it.

    Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python
    """

    def __init__(self, filename: str) -> None:
        """Load the motion file `filename`, an absolute path or a path relative to the controller directory.

        The motion is created stopped: call `play()` to start it.

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_new
        """

    def __del__(self) -> None: ...
    def isValid(self) -> bool:
        """Return whether the motion file was loaded.

        Upstream bug: it always returns `True`, so a failed load is not detected.

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_new
        """

    def play(self) -> None:
        """Start (or resume) the playback of the motion.

        Several motions can be played at once, but the behavior is undefined if they share joints.

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_play
        """

    def stop(self) -> None:
        """Interrupt the playback, keeping the current position so that `play()` resumes it.

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_stop
        """

    def setLoop(self, loop: bool) -> None:
        """Set whether the motion repeats when it reaches its end (or its beginning in reverse mode).

        It can be changed while the motion is playing. The default is `False`.

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_set_loop
        """

    def setReverse(self, reverse: bool) -> None:
        """Set whether the motion plays backwards.

        It can be changed while the motion is playing. The default is `False`.

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_set_reverse
        """

    def isOver(self) -> bool:
        """Return whether the playback has reached the end of the motion (its beginning in reverse mode).

        Always `False` in loop mode. The motors may not have reached the last pose yet.

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_is_over
        """

    def getDuration(self) -> int:
        """Return the total duration of the motion [ms].

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_get_duration
        """

    def getTime(self) -> int:
        """Return the current playback position [ms].

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_get_time
        """

    def setTime(self, time: int) -> None:
        """Set the playback position [ms], between 0 and `getDuration()`, whether playing or stopped.

        Reference: https://cyberbotics.com/doc/reference/motion?tab-language=python#wbu_motion_set_time
        """

    @property
    def time(self) -> int:
        """The playback position [ms] (same as `getTime()` / `setTime()`)."""

    @time.setter
    def time(self, time: int) -> None: ...
    @property
    def duration(self) -> int:
        """The total duration of the motion [ms] (same as `getDuration()`)."""
