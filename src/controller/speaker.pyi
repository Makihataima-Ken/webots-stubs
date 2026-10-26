from .device import Device

class Speaker(Device):
    """A loudspeaker that plays sound files and performs text-to-speech.

    Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python
    """

    def __init__(self, name: str | int) -> None: ...
    @staticmethod
    def playSound(
        left: Speaker, right: Speaker, sound: str, volume: float, pitch: float, balance: float, loop: bool
    ) -> None:
        """Play the WAV file `sound` on the `left` and `right` channel speakers (they may be the same speaker).

        `volume` is from 0.0 to 1.0, `pitch` is a positive multiplier (1.0 for no change), `balance` is from
        -1.0 (right muted) to 1.0 (left muted) and `loop` repeats the sound. Calling it again with the same
        speakers and `sound` changes the parameters of the sound already playing.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_play_sound
        """

    def stop(self, sound: str | None = None) -> None:
        """Stop the sound `sound` (as given to `playSound()`), or all sounds if `None`.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_stop
        """

    def isSoundPlaying(self, sound: str) -> bool:
        """Return whether the sound `sound` is playing; an empty string checks for any sound.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_is_sound_playing
        """

    def setEngine(self, engine: str) -> bool:
        """Set the text-to-speech engine ("pico", or "microsoft" on Windows); return whether it succeeded.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_set_engine
        """

    def setLanguage(self, language: str) -> bool:
        """Set the language of the text-to-speech engine, e.g. "en-US"; return whether it succeeded.

        Note: in R2025a the Python implementation calls `wb_speaker_set_engine` instead of
        `wb_speaker_set_language`, so it sets the engine, not the language.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_set_language
        """

    def getLanguage(self) -> str:
        """Return the language of the text-to-speech engine.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_get_language
        """

    def getEngine(self) -> str:
        """Return the text-to-speech engine.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_get_engine
        """

    def isSpeaking(self) -> bool:
        """Return whether the speaker is performing text-to-speech.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_is_speaking
        """

    def speak(self, text: str, volume: float) -> None:
        """Speak `text` (plain or SSML) with the current engine and language, at a `volume` from 0.0 to 1.0.

        Reference: https://cyberbotics.com/doc/reference/speaker?tab-language=python#wb_speaker_speak
        """
