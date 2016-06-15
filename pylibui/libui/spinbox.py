"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiSpinbox(ctypes.Structure):
    """Wrapper for the uiSpinbox C struct."""

    pass


def uiSpinboxPointer(obj):
    """
    Casts an object to uiSpinbox pointer type.

    :param obj: a generic object
    :return: uiSpinbox
    """

    return ctypes.cast(obj, ctypes.POINTER(uiSpinbox))


# - int uiSpinboxValue(uiSpinbox *s);
def uiSpinboxValue(spinbox):
    """
    Returns the value of the spinbox.

    :param spinbox: uiSpinbox
    :return: int
    """

    return clibui.uiSpinbox(spinbox)


# - void uiSpinboxSetValue(uiSpinbox *s, int value);
def uiSpinboxSetValue(spinbox, value):
    """
    Sets the value of the spinbox.

    :param spinbox: uiSpinbox
    :param value: int
    :return: None
    """

    clibui.uiSpinboxSetValue(spinbox, value)


# - void uiSpinboxOnChanged(uiSpinbox *s, void (*f)(uiSpinbox *s, void *data), void *data);
def uiSpinboxOnChanged(spinbox, callback, data):
    """
    Executes the callback function on value changed.

    :param spinbox: uiSpinbox
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """
    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiSpinbox), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiSpinboxOnChanged(spinbox, c_callback, data)

    return c_callback


# - uiSpinbox *uiNewSpinbox(int min, int max);
def uiNewSpinbox(min_value, max_value):
    """
    Creates a new spinbox.

    :param min_value: int
    :param max_value: int
    :return: uiSpinbox
    """

    # Set return type
    clibui.uiNewSpinbox.restype = ctypes.POINTER(uiSpinbox)

    return clibui.uiNewSpinbox(min_value, max_value)
