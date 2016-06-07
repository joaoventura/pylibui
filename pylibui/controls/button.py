"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Button(Control):

    def __init__(self, text):
        """
        Creates a new button.

        :param text: the text of the button
        """
        super().__init__()
        self.control = libui.uiNewButton(text)

        def handler(window, data):
            self.onClick(data)
            return 0

        self.clickHandler = libui.uiButtonOnClicked(self.control, handler, None)

    def setText(self, text):
        """
        Sets the text of the button.

        :param text: the text of the button
        """
        libui.uiButtonSetText(self.control, text)

    def getText(self):
        """
        Returns the text of the button

        :return: string
        """
        return libui.uiButtonText(self.control)

    def onClick(self, data):
        pass