"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Spinbox(Control):

    def __init__(self, min_value, max_value):
        """
        Creates a new spinbox.

        :param min_value: the minimum value (int)
        :param max_value: the maximum value (int)
        """
        super().__init__()
        self.control = libui.uiNewSpinbox(min_value, max_value)

        def handler(window, data):
            self.onChanged(data)
            return 0

        self.changedHandler = libui.uiSpinboxOnChanged(self.control, handler,
                                                       None)

    def setValue(self, value):
        """
        Sets the value of the spinbox.

        :param value: the value of the spinbox (int)
        :return: None
        """
        libui.uiSpinboxSetValue(self.control, value)

    def getValue(self):
        """
        Returns the value of the spinbox.

        :return: int
        """
        return libui.uiSpinboxValue(self.control)

    def onChanged(self, data):
        """
        Executes when spinbox's value change.

        :param data: data
        :return: None
        """
        pass
