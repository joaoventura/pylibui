"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiWindow(ctypes.Structure):
    """Wrapper for the uiWindow C struct."""

    pass


def uiWindowPointer(obj):
    """
    Casts an object to uiWindow pointer type.

    :param obj: a generic object
    :return: uiWindow
    """

    return ctypes.cast(obj, ctypes.POINTER(uiWindow))


# - char *uiWindowTitle(uiWindow *w);
def uiWindowTitle(window):
    """
    Returns the window title.

    :param window: uiWindow
    :return: string
    """

    # Set return type
    clibui.uiWindowTitle.restype = ctypes.c_char_p

    title = clibui.uiWindowTitle(window)
    return title.decode()


# - void uiWindowSetTitle(uiWindow *w, const char *title);
def uiWindowSetTitle(window, title):
    """
    Sets the window title.

    :param window: uiWindow
    :param title: string
    :return: None
    """

    return clibui.uiWindowSetTitle(window, bytes(title, 'utf-8'))


# - void uiWindowOnClosing(uiWindow *w, int (*f)(uiWindow *w, void *data), void *data);
def uiWindowOnClosing(window, callback, data):
    """
    Executes the callback function on window closing.

    :param window: uiWindow
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """

    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiWindow), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiWindowOnClosing(window, c_callback, data)

    return c_callback


# - void uiWindowSetChild(uiWindow *w, uiControl *child);
def uiWindowSetChild(window, child):
    """
    Sets the child of a window.

    :param window: uiWindow
    :param child: uiControl
    :return: None
    """

    return clibui.uiWindowSetChild(window, child)


# - int uiWindowMargined(uiWindow *w);
def uiWindowMargined(window):
    """
    Returns the window margined.

    :param window: uiWindow
    :return: int
    """

    # Set return type
    clibui.uiWindowMargined.restype = ctypes.c_int

    return clibui.uiWindowMargined(window)


# - void uiWindowSetMargined(uiWindow *w, int margined);
def uiWindowSetMargined(window, margined):
    """
    Sets the margins of the window

    :param window: uiWindow
    :param margined: int
    :return: None
    """

    return clibui.uiWindowSetMargined(window, margined)


# - uiWindow *uiNewWindow(const char *title, int width, int height, int hasMenubar);
def uiNewWindow(title, width, height, hasMenubar):
    """
    Creates a new Window.

    :param title: string
    :param width: int
    :param height: int
    :param hasMenubar: int
    :return: uiWindow
    """

    # Set return type
    clibui.uiNewWindow.restype = ctypes.POINTER(uiWindow)

    return clibui.uiNewWindow(
        ctypes.c_char_p(bytes(title, 'utf-8')), width, height, hasMenubar)
