"""
 Python wrapper for separator.

"""

from pylibui import libui
from .control import Control


class HorizontalSeparator(Control):

    def __init__(self):
        """
        Creates a new horizontal separator.

        """
        super().__init__()
        self.control = libui.uiNewHorizontalSeparator()

class VerticalSeparator(Control):

    def __init__(self):
        """
        Creates a new vertical separator.

        """
        super().__init__()
        self.control = libui.uiNewVerticalSeparator()
