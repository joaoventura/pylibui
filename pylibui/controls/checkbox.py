"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Checkbox(Control):

    def __init__(self, text):
        """
        Creates a new checkbox.

        """
        super().__init__()
        self.control = libui.uiNewCheckbox(text)

        def handler(window, data):
            self.onToggled(data)
            return 0

        self.toggledHandler = libui.uiCheckboxOnToggled(self.control, handler,
                                                        None)

    def setText(self, text):
        """
        Sets the text of the checkbox.

        :param text: the text of the checkbox
        :return: None
        """
        libui.uiCheckboxSetText(self.control, text)

    def getText(self):
        """
        Returns the text of the checkbox.

        :return: string
        """
        return libui.uiCheckboxText(self.control)

    def setChecked(self, checked):
        """
        Sets whether the checkbox is checked or not.

        :param checked: bool
        :return: None
        """
        libui.uiCheckboxSetChecked(self.control, checked)

    def getChecked(self):
        """
        Sets whether the checkbox is checked or not.

        :return: bool
        """
        return bool(libui.uiCheckboxChecked(self.control))

    def onToggled(self, data):
        """
        Executes when the checkbox is toggled.

        :param data: data
        :return: None
        """
        pass
