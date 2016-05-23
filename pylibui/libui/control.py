"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiControl(ctypes.Structure):
    """Wrapper for the uiControl C structure."""

    pass


def uiControlPointer(obj):
    """
    Casts an object to uiControl pointer type.

    :param obj: an ui object
    :return: uiControl
    """

    return ctypes.cast(obj, ctypes.POINTER(uiControl))


def uiControlShow(control):
    """
    Shows a control.

    :param control: uiControl object
    :return: None
    """

    return clibui.uiControlShow(control)


def uiControlDestroy(control):
    """
    Frees the resources allocated by a control

    :param control: uiControl object
    :return: None
    """

    return clibui.uiControlDestroy(control)
