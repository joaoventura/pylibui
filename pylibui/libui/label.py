"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiLabel(ctypes.Structure):
    """Wrapper for the uiLabel C struct."""

    pass


def uiLabelPointer(obj):
    """
    Casts an object to uiLabel pointer type.

    :param obj: a generic object
    :return: uiLabel
    """

    return ctypes.cast(obj, ctypes.POINTER(uiLabel))


# - char *uiLabelText(uiLabel *l);
def uiLabelText(*args):
    """
    Describe the function.

    :param args: arguments
    :return: value
    """

    # TODO
    return clibui.uiLabelText()


# - void uiLabelSetText(uiLabel *l, const char *text);
def uiLabelSetText(*args):
    """
    Describe the function.

    :param args: arguments
    :return: value
    """

    # TODO
    return clibui.uiLabelSetText()


# - uiLabel *uiNewLabel(const char *text);
def uiNewLabel(text):
    """
    Creates a new label.

    :param text: string
    :return: uiLabel
    """

    # Set return type
    clibui.uiNewLabel.restype = ctypes.POINTER(uiLabel)

    return clibui.uiNewLabel(bytes(text, 'utf-8'))
