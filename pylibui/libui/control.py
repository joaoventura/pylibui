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


# - void uiControlDestroy(uiControl *);
def uiControlDestroy(control):
    """
    Frees the resources allocated by a control.

    :param control: uiControl object
    :return: None
    """

    clibui.uiControlDestroy(control)


# - uiControl *uiControlParent(uiControl *);
def uiControlParent(control):
    """
    Returns the parent control.

    :param control: uiControl
    :return: uiControl
    """

    return clibui.uiControlParent(control)


# - void uiControlSetParent(uiControl *, uiControl *);
def uiControlSetParent(control, parent):
    """
    Sets the parent control.

    :param control: uiControl
    :param parent: uiControl
    :return: None
    """

    clibui.uiControlSetParent(control, parent)


# - int uiControlVisible(uiControl *);
def uiControlVisible(control):
    """
    Returns whether the control is visible.

    :param control: uiControl
    :return: uiControl
    """

    return clibui.uiControlVisible(control)


# - void uiControlShow(uiControl *);
def uiControlShow(control):
    """
    Shows a control.

    :param control: uiControl object
    :return: None
    """

    clibui.uiControlShow(control)


# - void uiControlHide(uiControl *);
def uiControlHide(control):
    """
    Hides a control.

    :param control: uiControl object
    :return: None
    """

    clibui.uiControlHide(control)


# - int uiControlEnabled(uiControl *);
def uiControlEnabled(control):
    """
    Returns whether a control is enabled.

    :param control: uiControl object
    :return: bool
    """

    return bool(clibui.uiControlEnabled(control))


# - void uiControlEnable(uiControl *);
def uiControlEnable(control):
    """
    Enables a control.

    :param control: uiControl object
    :return: None
    """

    clibui.uiControlEnable(control)


# - void uiControlDisable(uiControl *);
def uiControlDisable(control):
    """
    Disables a control.

    :param control: uiControl object
    :return: None
    """

    clibui.uiControlDisable(control)
