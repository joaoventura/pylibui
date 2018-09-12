"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiMultilineEntry(ctypes.Structure):
    """Wrapper for the uiMultilineEntry C struct."""

    pass


def uiMultilineEntryPointer(obj):
    """
    Casts an object to uiMultilineEntry pointer type.

    :param obj: a generic object
    :return: uiMultilineEntry
    """

    return ctypes.cast(obj, ctypes.POINTER(uiMultilineEntry))


# - char *uiMultilineEntryText(uiMultilineEntry *e);
def uiMultilineEntryText(entry):
    """
    Returns the text of the multiline entry.

    :param entry: uiMultilineEntry
    :return: string
    """

    clibui.uiMultilineEntryText.restype = ctypes.c_char_p
    text = clibui.uiMultilineEntryText(entry)

    return text.decode()


# - void uiMultilineEntrySetText(uiMultilineEntry *e, const char *text);
def uiMultilineEntrySetText(entry, text):
    """
    Sets the text of the multiline entry.

    :param entry: uiMultilineEntry
    :param text: string
    :return: None
    """

    clibui.uiMultilineEntrySetText(entry, bytes(text, 'utf-8'))


# - void uiMultilineEntryAppend(uiMultilineEntry *e, const char *text);
def uiMultilineEntryAppend(entry, text):
    """
    Appends some text to the multiline entry.

    :param entry: uiMultilineEntry
    :param text: string
    :return: None
    """

    clibui.uiMultilineEntryAppend(entry, bytes(text, 'utf-8'))


# - void uiMultilineEntryOnChanged(uiMultilineEntry *e, void (*f)(uiMultilineEntry *e, void *data), void *data);
def uiMultilineEntryOnChanged(entry, callback, data):
    """
    Executes the callback function on multiline entry change.

    :param entry: uiMultilineEntry
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """
    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiMultilineEntry), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiMultilineEntryOnChanged(entry, c_callback, data)

    return c_callback


# - int uiMultilineEntryReadOnly(uiMultilineEntry *e);
def uiMultilineEntryReadOnly(entry):
    """
    Returns whether the multiline entry is read only or not.

    :param entry: uiMultilineEntry
    :return: int
    """

    return clibui.uiMultilineEntryReadOnly(entry)


# - void uiMultilineEntrySetReadOnly(uiMultilineEntry *e, int readonly);
def uiMultilineEntrySetReadOnly(entry, read_only):
    """
    Sets whether the multiline entry is read only or not.

    :param entry: uiMultilineEntry
    :param read_only: int
    :return: None
    """

    clibui.uiMultilineEntrySetReadOnly(entry, read_only)


# - uiMultilineEntry *uiNewMultilineEntry(void);
def uiNewMultilineEntry():
    """
    Creates a new multiline entry.

    :return: uiMultilineEntry
    """

    # Set return type
    clibui.uiNewMultilineEntry.restype = ctypes.POINTER(uiMultilineEntry)

    return clibui.uiNewMultilineEntry()

# - uiMultilineEntry *uiNewNonWrappingMultilineEntry(void);
def uiNewNonWrappingMultilineEntry():
    """
    Creates a new non wrapping multiline entry.

    :return: uiMultilineEntry
    """

    # Set return type
    clibui.uiNewNonWrappingMultilineEntry.restype = ctypes.POINTER(
        uiMultilineEntry)

    return clibui.uiNewNonWrappingMultilineEntry()
