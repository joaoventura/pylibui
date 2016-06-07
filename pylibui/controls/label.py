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

    def setText(self, text):
        """
        Sets the text of the label.

        :param text: the text of the label
        :return: None
        """
        libui.uiLabelSetText(self.control, text)

    def getText(self):
        """
        Returns the text of the label

        :return: string
        """
        return libui.uiLabelText(self.control)
