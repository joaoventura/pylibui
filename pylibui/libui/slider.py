"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiSlider(ctypes.Structure):
    """Wrapper for the uiSlider C struct."""

    pass


def uiSliderPointer(obj):
    """
    Casts an object to uiSlider pointer type.

    :param obj: a generic object
    :return: uiSlider
    """

    return ctypes.cast(obj, ctypes.POINTER(uiSlider))


# - int uiSliderValue(uiSlider *s);
def uiSliderValue(slider):
    """
    Returns the value of the slider.

    :param slider: uiSlider
    :return: int
    """

    return clibui.uiSliderValue(slider)


# - void uiSliderSetValue(uiSlider *s, int value);
def uiSliderSetValue(slider, value):
    """
    Sets the value of the slider.

    :param slider: uiSlider
    :param value: int
    :return: None
    """

    clibui.uiSliderSetValue(slider, value)


# - void uiSliderOnChanged(uiSlider *s, void (*f)(uiSlider *s, void *data), void *data);
def uiSliderOnChanged(slider, callback, data):
    """
    Executes the callback function on value changed.

    :param slider: uiSlider
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """
    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiSlider), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiSliderOnChanged(slider, c_callback, data)

    return c_callback


# - uiSlider *uiNewSlider(int min, int max);
def uiNewSlider(min_value, max_value):
    """
    Creates a new slider.

    :param min_value: int
    :param max_value: int
    :return: uiSlider
    """

    # Set return type
    clibui.uiNewSlider.restype = ctypes.POINTER(uiSlider)

    return clibui.uiNewSlider(min_value, max_value)
