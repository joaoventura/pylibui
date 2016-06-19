"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiButton(ctypes.Structure):
    """Wrapper for the uiButton C struct."""

    pass


def uiButtonPointer(obj):
    """
    Casts an object to uiButton pointer type.

    :param obj: a generic object
    :return: uiButton
    """

    return ctypes.cast(obj, ctypes.POINTER(uiButton))


# - char *uiButtonText(uiButton *b);
def uiButtonText(button):
    """
    Returns the text of the button.

    :param button: uiButton
    :return: string
    """
    clibui.uiButtonText.restype = ctypes.c_char_p
    text = clibui.uiButtonText(button)

    return text.decode()


# - void uiButtonSetText(uiButton *b, const char *text);
def uiButtonSetText(button, text):
    """
    Sets the text of the button.

    :param button: uiButton
    :param text: string
    :return: None
    """

    clibui.uiButtonSetText(button, bytes(text, 'utf-8'))


# - void uiButtonOnClicked(uiButton *b, void (*f)(uiButton *b, void *data), void *data);
def uiButtonOnClicked(button, callback, data):
    """
    Executes the callback function on button click.

    :param button: uiButton
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """
    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiButton), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiButtonOnClicked(button, c_callback, data)

    return c_callback


# - uiButton *uiNewButton(const char *text);
def uiNewButton(text):
    """
    Creates a new button.

    :param text: string
    :return: uiButton
    """

    # Set return type
    clibui.uiNewButton.restype = ctypes.POINTER(uiButton)

    return clibui.uiNewButton(bytes(text, 'utf-8'))
