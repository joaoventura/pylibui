"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiGroup(ctypes.Structure):
    """Wrapper for the uiGroup C struct."""

    pass


def uiGroupPointer(obj):
    """
    Casts an object to uiGroup pointer type.

    :param obj: a generic object
    :return: uiGroup
    """

    return ctypes.cast(obj, ctypes.POINTER(uiGroup))


# - char *uiGroupTitle(uiGroup *g);
def uiGroupTitle(group):
    """
    Returns the title of the group.

    :param group: uiGroup
    :return: string
    """

    clibui.uiGroupTitle.restype = ctypes.c_char_p
    title = clibui.uiGroupTitle(group)

    return title.decode()


# - void uiGroupSetTitle(uiGroup *g, const char *title);
def uiGroupSetTitle(group, title):
    """
    Sets the title of the group.

    :param group: uiGroup
    :param title: string
    :return: None
    """

    clibui.uiGroupSetTitle(group, bytes(title, 'utf-8'))


# - void uiGroupSetChild(uiGroup *g, uiControl *c);
def uiGroupSetChild(group, child):
    """
    Sets the child of a group.

    :param group: uiGroup
    :param child: uiControl
    :return: None
    """

    clibui.uiGroupSetChild(group, child)


# - int uiGroupMargined(uiGroup *g);
def uiGroupMargined(group):
    """
    Returns whether the group is margined.

    :param group: uiGroup
    :return: int
    """

    return clibui.uiGroupMargined(group)


# - void uiGroupSetMargined(uiGroup *g, int margined);
def uiGroupSetMargined(group, margined):
    """
    Sets whether the group is margined.

    :param group: uiGroup
    :param margined: int
    :return: None
    """

    clibui.uiGroupSetMargined(group, margined)


# - uiGroup *uiNewGroup(const char *title);
def uiNewGroup(title):
    """
    Creates a new group.

    :param title: string
    :return: uiGroup
    """

    # Set return type
    clibui.uiNewGroup.restype = ctypes.POINTER(uiGroup)

    return clibui.uiNewGroup(bytes(title, 'utf-8'))
