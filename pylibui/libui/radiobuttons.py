"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiRadioButtons(ctypes.Structure):
    """Wrapper for the uiRadioButtons C struct."""

    pass


def uiRadioButtonsPointer(obj):
    """
    Casts an object to uiRadioButtons pointer type.

    :param obj: a generic object
    :return: uiRadioButtons
    """

    return ctypes.cast(obj, ctypes.POINTER(uiRadioButtons))


# - void uiRadioButtonsAppend(uiRadioButtons *r, const char *text);
def uiRadioButtonsAppend(radio_buttons, text):
    """
    Appends a new item to the radio buttons.

    :param radio_buttons: uiRadioButtons
    :param text: string
    :return: None
    """

    clibui.uiRadioButtonsAppend(radio_buttons, bytes(text, 'utf-8'))


# - int uiRadioButtonsSelected(uiRadioButtons *r);
def uiRadioButtonsSelected(radio_buttons):
    """
    Returns the selected item's index.

    :param radio_buttons: uiRadioButtons
    :return: int
    """

    return clibui.uiRadioButtonsSelected(radio_buttons)


# - void uiRadioButtonsSetSelected(uiRadioButtons *r, int n);
def uiRadioButtonsSetSelected(radio_buttons, n):
    """
    Sets selected item.

    :param radio_buttons: uiRadioButtons
    :param n: int
    :return: None
    """

    clibui.uiRadioButtonsSetSelected(radio_buttons, n)


# - void uiRadioButtonsOnSelected(uiRadioButtons *r, void (*f)(uiRadioButtons *, void *), void *data);
def uiRadioButtonsOnSelected(radio_buttons, callback, data):
    """
    Executes a callback function when an item selected.

    :param radio_buttons: uiRadioButtons
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """

    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiRadioButtons), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiRadioButtonsOnSelected(radio_buttons, c_callback, data)

    return c_callback


# - uiRadioButtons *uiNewRadioButtons(void);
def uiNewRadioButtons():
    """
    Creates a new radio buttons.

    :return: uiRadioButtons
    """

    clibui.uiNewRadioButtons.restype = ctypes.POINTER(uiRadioButtons)

    return clibui.uiNewRadioButtons()
