"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiCombobox(ctypes.Structure):
    """Wrapper for the uiCombobox C struct."""

    pass


def uiComboboxPointer(obj):
    """
    Casts an object to uiCombobox pointer type.

    :param obj: a generic object
    :return: uiCombobox
    """

    return ctypes.cast(obj, ctypes.POINTER(uiCombobox))


# - void uiComboboxAppend(uiCombobox *c, const char *text);
def uiComboboxAppend(combobox, text):
    """
    Appends a new item to the combobox.

    :param combobox: uiCombobox
    :param text: string
    :return: None
    """

    clibui.uiComboboxAppend(combobox, bytes(text, 'utf-8'))


# - int uiComboboxSelected(uiCombobox *c);
def uiComboboxSelected(combobox):
    """
    Returns selected items index.

    :param combobox: uiCombobox
    :return: int
    """

    return clibui.uiComboboxSelected(combobox)


# - void uiComboboxSetSelected(uiCombobox *c, int n);
def uiComboboxSetSelected(combobox, n):
    """
    Sets selected item.

    :param combobox: uiCombobox
    :param n: integer
    :return: None
    """

    clibui.uiComboboxSetSelected(combobox, n)


# - void uiComboboxOnSelected(uiCombobox *c, void (*f)(uiCombobox *c, void *data), void *data);
def uiComboboxOnSelected(combobox, callback, data):
    """
    Executes a callback function when an item selected.

    :param combobox: uiCombobox
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """

    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiCombobox), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiComboboxOnSelected(combobox, c_callback, data)

    return c_callback


def uiNewCombobox():
    """
    Creates a new combobox.

    :return: uiCombobox
    """

    clibui.uiNewCombobox.restype = ctypes.POINTER(uiCombobox)

    return clibui.uiNewCombobox()
