"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class DateTimePicker(Control):

    def __init__(self):
        """
        Creates a new date/time picker.

        """
        super().__init__()
        self.control = libui.uiNewDateTimePicker()


class DatePicker(Control):

    def __init__(self):
        """
        Creates a new date picker.

        """
        super().__init__()
        self.control = libui.uiNewDatePicker()


class TimePicker(Control):

    def __init__(self):
        """
        Creates a new time picker.

        """
        super().__init__()
        self.control = libui.uiNewTimePicker()
