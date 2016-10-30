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
    Describe the function.

    :return: HorizontalSeparator
    """

    return clibui.uiNewHorizontalSeparator()


# - uiSeparator *uiNewVerticalSeparator(void);
def uiNewVerticalSeparator():
    """
    Describe the function.

    :return: VerticalSeparator
    """

    #clibui.uiNewVerticalSeparator.restype = ctypes.POINTER(uiSeparator)

    return clibui.uiNewVerticalSeparator()
