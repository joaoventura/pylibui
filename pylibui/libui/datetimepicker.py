"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiDateTimePicker(ctypes.Structure):
    """Wrapper for the uiDateTimePicker C struct."""

    pass


def uiDateTimePickerPointer(obj):
    """
    Casts an object to uiDateTimePicker pointer type.

    :param obj: a generic object
    :return: uiDateTimePicker
    """

    return ctypes.cast(obj, ctypes.POINTER(uiDateTimePicker))


# - uiDateTimePicker *uiNewDateTimePicker(void);
def uiNewDateTimePicker():
    """
    Creates a new date/time picker.

    :return: uiDateTimePicker
    """

    # Set return type
    clibui.uiNewDateTimePicker.restype = ctypes.POINTER(uiDateTimePicker)

    return clibui.uiNewDateTimePicker()


# - uiDateTimePicker *uiNewDatePicker(void);
def uiNewDatePicker():
    """
    Creates a new date picker.

    :return: uiDateTimePicker
    """

    # Set return type
    clibui.uiNewDatePicker.restype = ctypes.POINTER(uiDateTimePicker)

    return clibui.uiNewDatePicker()


# - uiDateTimePicker *uiNewTimePicker(void);
def uiNewTimePicker():
    """
    Creates a new time picker.

    :return: uiDateTimePicker
    """

    # Set return type
    clibui.uiNewTimePicker.restype = ctypes.POINTER(uiDateTimePicker)

    return clibui.uiNewTimePicker()
