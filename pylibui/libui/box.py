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

    clibui.uiBoxAppend(box, child, stretchy)


# - void uiBoxDelete(uiBox *b, int index);
def uiBoxDelete(box, index):
    """
    Deletes a child from a box.

    :param box: uiBox
    :param index: int
    :return: None
    """

    clibui.uiBoxDelete(box, index)


# - int uiBoxPadded(uiBox *b);
def uiBoxPadded(box):
    """
    Returns whether the box is padded.

    :param box: uiBox
    :return: int
    """

    return clibui.uiBoxPadded(box)


# - void uiBoxSetPadded(uiBox *b, int padded);
def uiBoxSetPadded(box, padded):
    """
    Sets the padding of the box.

    :param box: uiBox
    :param padded: int
    :return: None
    """

    clibui.uiBoxSetPadded(box, padded)


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
