"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiSeparator(ctypes.Structure):
    """Wrapper for the uiSeparator C struct."""

    pass


def uiSeparatorPointer(obj):
    """
    Casts an object to uiSeparator pointer type.

    :param obj: a generic object
    :return: uiSeparator
    """

    return ctypes.cast(obj, ctypes.POINTER(uiSeparator))


# - uiSeparator *uiNewHorizontalSeparator(void);
def uiNewHorizontalSeparator():
    """
    Returns an horizonal separator.

    :return: uiHorizontalSeparator
    """

    # Set return type
    clibui.uiNewHorizontalSeparator.restype = ctypes.POINTER(uiSeparator)

    return clibui.uiNewHorizontalSeparator()


# - uiSeparator *uiNewVerticalSeparator(void);
def uiNewVerticalSeparator():
    """
    Returns aa vertical separator.

    :return: uiVerticalSeparator
    """

    # Set return type
    clibui.uiNewVerticalSeparator.restype = ctypes.POINTER(uiSeparator)

    return clibui.uiNewVerticalSeparator()
