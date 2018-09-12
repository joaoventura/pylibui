"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Form(Control):

    def __init__(self):
        """
        Creates a new empty form.

        """
        super().__init__()
        self.control = libui.uiNewForm()
        self.controls = []

    def append(self, label, control, stretchy=False):
        """
        Appends a control to the form.

        :param label: str
        :param control: control
        :param stretchy: bool
        :return: None
        """
        libui.uiFormAppend(self.control, label, control.pointer(),
                           int(stretchy))
        self.controls.append(control)

    def delete(self, index):
        """
        Deletes a child from a form.

        :param index: int
        :return: None
        """
        libui.uiFormDelete(self.control, index)
        self.controls[index].destroy()
        del self.controls[index]

    def getPadded(self):
        """
        Returns whether the form is padded.

        :return: bool
        """
        return bool(libui.uiFormPadded(self.control))

    def setPadded(self, padded):
        """
        Sets whether the form is padded.

        :param padded: bool
        :return: None
        """
        libui.uiFormSetPadded(self.control, int(padded))
