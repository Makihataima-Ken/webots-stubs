from typing import Final

class AnsiCodes:
    """ANSI escape codes to format the text printed in the Webots console (colors, bold, underline).

    Print a code before the text to format it and `RESET` after it, e.g.
    `print(AnsiCodes.RED_FOREGROUND + "error" + AnsiCodes.RESET)`.
    """

    RESET: Final[str]
    """Reset all text attributes."""
    BOLD: Final[str]
    """Bold text."""
    UNDERLINE: Final[str]
    """Underlined text."""
    BLACK_BACKGROUND: Final[str]
    """Black background."""
    RED_BACKGROUND: Final[str]
    """Red background."""
    GREEN_BACKGROUND: Final[str]
    """Green background."""
    YELLOW_BACKGROUND: Final[str]
    """Yellow background."""
    BLUE_BACKGROUND: Final[str]
    """Blue background."""
    MAGENTA_BACKGROUND: Final[str]
    """Magenta background."""
    CYAN_BACKGROUND: Final[str]
    """Cyan background."""
    WHITE_BACKGROUND: Final[str]
    """White background."""
    BLACK_FOREGROUND: Final[str]
    """Black text."""
    RED_FOREGROUND: Final[str]
    """Red text."""
    GREEN_FOREGROUND: Final[str]
    """Green text."""
    YELLOW_FOREGROUND: Final[str]
    """Yellow text."""
    BLUE_FOREGROUND: Final[str]
    """Blue text."""
    MAGENTA_FOREGROUND: Final[str]
    """Magenta text."""
    CYAN_FOREGROUND: Final[str]
    """Cyan text."""
    WHITE_FOREGROUND: Final[str]
    """White text."""
    CLEAR_SCREEN: Final[str]
    """Clear the console."""
