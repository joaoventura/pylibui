"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiInitOptions(ctypes.Structure):
    """Wrapper for the uiInitOptions C structure."""

    pass


def uiInit(options):
    """
    Initializes the libui.

    :param options: uiInitOptions object
    :return: String if error else None
    """

    return clibui.uiInit(ctypes.byref(options))


def uiUninit():
    """
    Uninitializes the libui and frees resources.

    :return: None
    """

    clibui.uiUninit()


def uiMain():
    """
    Executes the libui main loop.

    :return: None
    """

    clibui.uiMain()


def uiQuit():
    """
    Quits the libui main loop.

    :return:
    """

    clibui.uiQuit()
