"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiProgressBar(ctypes.Structure):
    """Wrapper for the uiProgressBar C struct."""

    pass


def uiProgressBarPointer(obj):
    """
    Casts an object to uiProgressBar pointer type.

    :param obj: a generic object
    :return: uiProgressBar
    """

    return ctypes.cast(obj, ctypes.POINTER(uiProgressBar))


# - int uiProgressBarValue(uiProgressBar *p);
def uiProgressBarValue(progressbar):
    """
    Returns the value of the progress bar.

    :param slider: uiProgressBar
    :return: int
    """

    return clibui.uiProgressBarValue(progressbar)


# - void uiProgressBarSetValue(uiProgressBar *p, int n);
def uiProgressBarSetValue(progressbar, value):
    """
    Sets the value of the progress bar.

    :param progressbar: uiProgressBar
    :param value: int
    :return: None
    """

    clibui.uiProgressBarSetValue(progressbar, value)


# - uiProgressBar *uiNewProgressBar(void);
def uiNewProgressBar():
    """
    Creates a new progress bar.

    :return: uiProgressBar
    """

    # Set return type
    clibui.uiNewProgressBar.restype = ctypes.POINTER(uiProgressBar)

    return clibui.uiNewProgressBar()
