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
    Returns the window's title.

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
    Sets the window's title.

    :param window: uiWindow
    :param title: string
    :return: None
    """

    clibui.uiWindowSetTitle(window, bytes(title, 'utf-8'))


# - void uiWindowContentSize(uiWindow *w, int *width, int *height);
def uiWindowContentSize(window):
    """
    Returns the window's content size.

    :param window: uiWindow
    :return: tuple
    """

    width = ctypes.c_int()
    height = ctypes.c_int()
    clibui.uiWindowContentSize(window, ctypes.byref(width),
                               ctypes.byref(height))

    return (width.value, height.value)


# - void uiWindowSetContentSize(uiWindow *w, int width, int height);
def uiWindowSetContentSize(window, width, height):
    """
    Sets the window's content size.

    :param window: uiWindow
    :param width: int
    :param height: int
    :return: None
    """

    clibui.uiWindowSetContentSize(window, width, height)


# - int uiWindowFullscreen(uiWindow *w);
def uiWindowFullscreen(window):
    """
    Returns whether the window is in fullscreen.

    :param window: uiWindow
    :return: int
    """

    return clibui.uiWindowFullscreen(window)


# - void uiWindowSetFullscreen(uiWindow *w, int fullscreen);
def uiWindowSetFullscreen(window, fullscreen):
    """
    Sets whether the window is in fullscreen.

    :param window: uiWindow
    :param fullscreen: int
    :return: None
    """

    clibui.uiWindowSetFullscreen(window, fullscreen)


# - void uiWindowOnContentSizeChanged(uiWindow *w, void (*f)(uiWindow *, void *), void *data);
def uiWindowOnContentSizeChanged(window, callback, data):
    """
    Executes the callback function on window's content size change.

    :param window: uiWindow
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """

    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiWindow), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiWindowOnContentSizeChanged(window, c_callback, data)

    return c_callback


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


# - int uiWindowBorderless(uiWindow *w);
def uiWindowBorderless(window):
    """
    Returns whether the window is borderless.

    :param window: uiWindow
    :return: int
    """

    return clibui.uiWindowBorderless(window)


# - void uiWindowSetBorderless(uiWindow *w, int borderless);
def uiWindowSetBorderless(window, borderless):
    """
    Sets whether the window is borderless.

    :param window: uiWindow
    :param borderless: int
    :return: None
    """

    clibui.uiWindowSetBorderless(window, borderless)


# - void uiWindowSetChild(uiWindow *w, uiControl *child);
def uiWindowSetChild(window, child):
    """
    Sets the child of a window.

    :param window: uiWindow
    :param child: uiControl
    :return: None
    """

    clibui.uiWindowSetChild(window, child)


# - int uiWindowMargined(uiWindow *w);
def uiWindowMargined(window):
    """
    Returns the window's margins.

    :param window: uiWindow
    :return: int
    """

    return clibui.uiWindowMargined(window)


# - void uiWindowSetMargined(uiWindow *w, int margined);
def uiWindowSetMargined(window, margined):
    """
    Sets the window's margins.

    :param window: uiWindow
    :param margined: int
    :return: None
    """

    clibui.uiWindowSetMargined(window, margined)


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
