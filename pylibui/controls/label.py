"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Label(Control):

    def __init__(self, text):
        """
        Creates a new label.

        :param text: the text of the label
        """
        super().__init__()
        self.control = libui.uiNewLabel(text)
