"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiWindow(ctypes.Structure):
    """Wrapper for the uiWindow C structure."""

    pass


def uiNewWindow(title, width, height, hasMenubar):
    """
    Creates a new Window.

    :param title: the title
    :param width: the width
    :param height: the height
    :param hasMenubar: if has menu bar
    :return: uiWindow object
    """

    return clibui.uiNewWindow(
        ctypes.c_char_p(bytes(title, 'utf-8')), width, height, hasMenubar)

clibui.uiNewWindow.restype = ctypes.POINTER(uiWindow)


def uiWindowSetMargined(window, margined):
    """
    Sets the margins of the window

    :param window: uiWindow object
    :param margined: the margined property
    :return: None
    """

    return clibui.uiWindowSetMargined(window, margined)


def uiWindowOnClosing(window, callback, data):
    """
    Executes the callback function on window closing.

    :param window: uiWindow object
    :param callback: the callback function
    :param data: data information
    :return: reference to C callback function
    """

    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiWindow), ctypes.c_void_p)

    c_callback = c_type(callback)

    clibui.uiWindowOnClosing(window, c_callback, data)

    return c_callback
