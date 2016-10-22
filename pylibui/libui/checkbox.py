"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiCheckbox(ctypes.Structure):
    """Wrapper for the uiCheckbox C struct."""

    pass


def uiCheckboxPointer(obj):
    """
    Casts an object to uiCheckbox pointer type.

    :param obj: a generic object
    :return: uiCheckbox
    """

    return ctypes.cast(obj, ctypes.POINTER(uiCheckbox))


# - char *uiCheckboxText(uiCheckbox *c);
def uiCheckboxText(checkbox):
    """
    Returns the text of the checkbox.

    :param checkbox: uiCheckbox
    :return: string
    """

    clibui.uiCheckboxText.restype = ctypes.c_char_p
    text = clibui.uiCheckboxText(checkbox)

    return text.decode()


# - void uiCheckboxSetText(uiCheckbox *c, const char *text);
def uiCheckboxSetText(checkbox, text):
    """
    Sets the text of the checkbox.

    :param checkbox: uiCheckbox
    :param text: string
    :return: None
    """

    clibui.uiCheckboxSetText(checkbox, bytes(text, 'utf-8'))


# - void uiCheckboxOnToggled(uiCheckbox *c, void (*f)(uiCheckbox *c, void *data), void *data);
def uiCheckboxOnToggled(checkbox, callback, data):
    """
    Executes the callback function on checkbox toggle.

    :param checkbox: uiCheckbox
    :param callback: function
    :param data: data
    :return: reference to C callback function
    """
    c_type = ctypes.CFUNCTYPE(
        ctypes.c_int, ctypes.POINTER(uiCheckbox), ctypes.c_void_p)
    c_callback = c_type(callback)

    clibui.uiCheckboxOnToggled(checkbox, c_callback, data)

    return c_callback


# - int uiCheckboxChecked(uiCheckbox *c);
def uiCheckboxChecked(checkbox):
    """
    Returns whether the checkbox is checked or not.

    :param checkbox: uiCheckbox
    :return: int
    """

    return clibui.uiCheckboxChecked(checkbox)


# - void uiCheckboxSetChecked(uiCheckbox *c, int checked);
def uiCheckboxSetChecked(checkbox, checked):
    """
    Sets whether the checkbox is checked or not.

    :param checkbox: uiCheckbox
    :param checked: int
    :return: None
    """

    clibui.uiCheckboxSetChecked(checkbox, checked)


# - uiCheckbox *uiNewCheckbox(const char *text);
def uiNewCheckbox(text):
    """
    Creates a new checkbox.

    :return: uiCheckbox
    """

    # Set return type
    clibui.uiNewCheckbox.restype = ctypes.POINTER(uiCheckbox)

    return clibui.uiNewCheckbox(bytes(text, 'utf-8'))
