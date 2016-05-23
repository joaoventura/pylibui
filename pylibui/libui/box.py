"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiBox(ctypes.Structure):
    """Wrapper for the uiBox C struct."""

    pass


def uiBoxPointer(obj):
    """
    Casts an object to uiBox pointer type.

    :param obj: a generic object
    :return: uiBox
    """

    return ctypes.cast(obj, ctypes.POINTER(uiBox))


# - void uiBoxAppend(uiBox *b, uiControl *child, int stretchy);
def uiBoxAppend(box, child, stretchy):
    """
    Appends a child to a box.

    :param box: uiBox
    :param child: uiControl
    :param stretchy: int
    :return: None
    """

    return clibui.uiBoxAppend(box, child, stretchy)


# - void uiBoxDelete(uiBox *b, uintmax_t index);
def uiBoxDelete(*args):
    """
    Describe the function.

    :param args: arguments
    :return: value
    """

    # TODO
    return clibui.uiBoxDelete()


# - int uiBoxPadded(uiBox *b);
def uiBoxPadded(*args):
    """
    Describe the function.

    :param args: arguments
    :return: value
    """

    # TODO
    return clibui.uiBoxPadded()


# - void uiBoxSetPadded(uiBox *b, int padded);
def uiBoxSetPadded(box, padded):
    """
    Sets the padding of the box.

    :param box: uiBox
    :param padded: int
    :return: None
    """

    return clibui.uiBoxSetPadded(box, padded)


# - uiBox *uiNewHorizontalBox(void);
def uiNewHorizontalBox():
    """
    Returns an horizonal box

    :return: uiBox
    """

    # Set return type
    clibui.uiNewHorizontalBox.restype = ctypes.POINTER(uiBox)

    return clibui.uiNewHorizontalBox()


# - uiBox *uiNewVerticalBox(void);
def uiNewVerticalBox():
    """
    Returns a vertical box.

    :return: uiBox
    """

    # Set return type
    clibui.uiNewVerticalBox.restype = ctypes.POINTER(uiBox)

    return clibui.uiNewVerticalBox()
