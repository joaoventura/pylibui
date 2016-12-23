"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


# - char *uiOpenFile(uiWindow *parent);
def uiOpenFile(parent):
    """
    Creates a new open file dialog.

    :param parent: uiWindow
    :return: string
    """

    clibui.uiOpenFile.restype = ctypes.c_char_p
    path = clibui.uiOpenFile(parent)

    if path is not None:
        return path.decode()
    else:
        return ""


# - char *uiSaveFile(uiWindow *parent);
def uiSaveFile(parent):
    """
    Creates a new save file dialog.

    :param parent: uiWindow
    :return: string
    """

    clibui.uiSaveFile.restype = ctypes.c_char_p
    path = clibui.uiSaveFile(parent)

    if path is not None:
        return path.decode()
    else:
        return ""


# - void uiMsgBox(uiWindow *parent, const char *title, const char *description);
def uiMsgBox(parent, title, description):
    """
    Creates a new dialog.

    :param parent: uiWindow
    :param title: string
    :param description: string
    :return: None
    """

    clibui.uiMsgBox(parent, bytes(title, 'utf-8'), bytes(description, 'utf-8'))


# - void uiMsgBoxError(uiWindow *parent, const char *title, const char *description);
def uiMsgBoxError(window, title, description):
    """
    Creates a new error dialog.

    :param window: uiWindow
    :param title: string
    :param description: string
    :return: None
    """

    clibui.uiMsgBoxError(window,
                         bytes(title, 'utf-8'), bytes(description, 'utf-8'))
