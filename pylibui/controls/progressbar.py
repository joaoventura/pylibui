"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class ProgressBar(Control):

    def __init__(self):
        """
        Creates a new progress bar.

        """
        super().__init__()
        self.control = libui.uiNewProgressBar()

    def setValue(self, value):
        """
        Sets the value of the progress bar.

        :param value: the value of the progress bar (int between 0 and 100)
        """
        libui.uiProgressBarSetValue(self.control, value)

    def getValue(self):
        """
        Returns the value of the progress bar.

        :return: int
        """

        return libui.uiProgressBarValue(self.control)
