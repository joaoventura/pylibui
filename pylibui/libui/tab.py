"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiTab(ctypes.Structure):
    """Wrapper for the uiTab C struct."""

    pass


def uiTabPointer(obj):
    """
    Casts an object to uiTab pointer type.

    :param obj: a generic object
    :return: uiTab
    """

    return ctypes.cast(obj, ctypes.POINTER(uiTab))


# - void uiTabAppend(uiTab *t, const char *name, uiControl *c);
def uiTabAppend(tab, name, control):
    """
    Appends a control to the tab.

    :param tab: uiTab
    :param name: str
    :param control: uiControl
    :return: None
    """

    clibui.uiTabAppend(tab, bytes(name, 'utf-8'), control)


# - void uiTabInsertAt(uiTab *t, const char *name, int before, uiControl *c);
def uiTabInsertAt(tab, name, before, control):
    """
    Appends a control to the tab.

    :param tab: uiTab
    :param name: str
    :param before: int
    :param control: uiControl
    :return: None
    """

    clibui.uiTabInsertAt(tab, bytes(name, 'utf-8'), before, control)


# void uiTabDelete(uiTab *t, int index);
def uiTabDelete(tab, index):
    """
    Deletes a control from the tab.

    :param tab: uiTab
    :param index: int
    :return: None
    """

    clibui.uiTabDelete(tab, index)


# - int uiTabNumPages(uiTab *t);
def uiTabNumPages(tab):
    """
    Returns the number of pages of the tab.

    :param tab: uiTab
    :return: int
    """

    return clibui.uiTabNumPages(tab)


# - int uiTabMargined(uiTab *t, int page);
def uiTabMargined(tab, page):
    """
    Returns the window margined.

    :param tab: uiTab
    :param page: int
    :return: int
    """

    return clibui.uiTabMargined(tab, page)


# - void uiTabSetMargined(uiTab *t, int page, int margined);
def uiTabSetMargined(tab, page, margined):
    """
    Sets the margin of the tab.

    :param tab: uiTab
    :param page: int
    :param margined: int
    :return: None
    """

    clibui.uiTabSetMargined(tab, page, margined)


# - uiTab *uiNewTab(void);
def uiNewTab():
    """
    Creates a new tab.

    :return: uiTab
    """

    # Set return type
    clibui.uiNewTab.restype = ctypes.POINTER(uiTab)

    return clibui.uiNewTab()
