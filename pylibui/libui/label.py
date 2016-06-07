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
def uiLabelText(label):
    """
    Returns the text of the label.

    :param label: uiLabel
    :return: string
    """

    clibui.uiLabelText.restype = ctypes.c_char_p
    text = clibui.uiLabelText(label)

    return text.decode()


# - void uiLabelSetText(uiLabel *l, const char *text);
def uiLabelSetText(label, text):
    """
    Sets the text of the label.

    :param label: uiLabel
    :param text: string
    """

    clibui.uiLabelSetText(label, bytes(text, 'utf-8'))


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
