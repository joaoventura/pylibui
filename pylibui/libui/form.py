"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui


class uiForm(ctypes.Structure):
    """Wrapper for the uiForm C struct."""

    pass


def uiFormPointer(obj):
    """
    Casts an object to uiForm pointer type.

    :param obj: a generic object
    :return: uiForm
    """

    return ctypes.cast(obj, ctypes.POINTER(uiForm))


# - void uiFormAppend(uiForm *f, const char *label, uiControl *c, int stretchy);
def uiFormAppend(form, label, control, stretchy):
    """
    Appends a control to a form.

    :param form: uiForm
    :param label: str
    :param control: uiControl
    :param stretchy: int
    :return: None
    """

    clibui.uiFormAppend(form, bytes(label, 'utf-8'), control, stretchy)


# - void uiFormDelete(uiForm *f, int index);
def uiFormDelete(form, index):
    """
    Deletes a child from a form.

    :param form: uiForm
    :param index: int
    :return: None
    """

    clibui.uiFormDelete(form, index)


# - int uiFormPadded(uiForm *f);
def uiFormPadded(form):
    """
    Returns whether the form is padded.

    :param form: uiForm
    :return: int
    """

    return clibui.uiFormPadded(form)


# - void uiFormSetPadded(uiForm *f, int padded);
def uiFormSetPadded(form, padded):
    """
    Sets whether the form is padded.

    :param form: uiForm
    :param padded: int
    :return: None
    """

    clibui.uiFormSetPadded(form, padded)


# - uiForm *uiNewForm(void);
def uiNewForm():
    """
    Creates a new form.

    :return: uiForm
    """

    # Set return type
    clibui.uiNewForm.restype = ctypes.POINTER(uiForm)

    return clibui.uiNewForm()
