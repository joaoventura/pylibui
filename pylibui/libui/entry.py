"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiEntry(ctypes.Structure):
    """Wrapper for the uiEntry C struct."""

    pass


def uiEntryPointer(obj):
    """
    Casts an object to uiEntry pointer type.

    :param obj: a generic object
    :return: uiEntry
    """

    return ctypes.cast(obj, ctypes.POINTER(uiEntry))


# - char *uiEntryText(uiEntry *e);
def uiEntryText(entry):
    """
    Returns the text of the entry.

    :param entry: uiEntry
    :return: string
    """

    clibui.uiEntryText.restype = ctypes.c_char_p
    text = clibui.uiEntryText(entry)

    return text.decode()


# - void uiEntrySetText(uiEntry *e, const char *text);
def uiEntrySetText(entry, text):
    """
    Sets the text of the entry.

    :param entry: uiEntry
    :param text: string
    :return: None
    """

    clibui.uiEntrySetText(entry, bytes(text, 'utf-8'))


# - void uiEntryOnChanged(uiEntry *e, void (*f)(uiEntry *e, void *data), void *data);
def uiEntryOnChanged(entry, callback, data):
    """
    Executes the callback function on entry change.

    :param entry: uiEntry
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """
    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiEntry), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiEntryOnChanged(entry, c_callback, data)

    return c_callback


# - int uiEntryReadOnly(uiEntry *e);
def uiEntryReadOnly(entry):
    """
    Returns whether the entry is read only or not.

    :param entry: uiEntry
    :return: string
    """

    return bool(clibui.uiEntryReadOnly(entry))


# - void uiEntrySetReadOnly(uiEntry *e, int readonly);
def uiEntrySetReadOnly(entry, read_only):
    """
    Sets whether the entry is read only or not.

    :param entry: uiEntry
    :param read_only: int
    :return: None
    """

    clibui.uiEntrySetReadOnly(entry, read_only)


# - uiEntry *uiNewEntry(void);
def uiNewEntry():
    """
    Creates a new entry.

    :return: uiEntry
    """

    # Set return type
    clibui.uiNewEntry.restype = ctypes.POINTER(uiEntry)

    return clibui.uiNewEntry()


# uiEntry *uiNewPasswordEntry(void);
def uiNewPasswordEntry():
    """
    Creates a new password entry.

    :return: uiEntry
    """

    # Set return type
    clibui.uiNewPasswordEntry.restype = ctypes.POINTER(uiEntry)

    return clibui.uiNewPasswordEntry()


# uiEntry *uiNewSearchEntry(void);
def uiNewSearchEntry():
    """
    Creates a new search entry.

    :return: uiEntry
    """

    # Set return type
    clibui.uiNewSearchEntry.restype = ctypes.POINTER(uiEntry)

    return clibui.uiNewSearchEntry()
