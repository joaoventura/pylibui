"""
 Python wrapper for libui.

"""

from .callback_helper import get_c_callback_func_ptr, c_func_type_int_structp_voidp, c_func_type_void_structp_voidp
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

        self.clickHandler = libui.uiButtonOnClicked(self.control,
                                                        get_c_callback_func_ptr(handler, c_func_type_void_structp_voidp),
                                                    None)

    def setText(self, text):
        """
        Sets the text of the button.

        :param text: string
        :return: None
        """
        libui.uiButtonSetText(self.control, text)

    def getText(self):
        """
        Returns the text of the button

        :return: string
        """
        return libui.uiButtonText(self.control)

    def onClick(self, data):
        """
        Executes when the button is clicked.

        :param data: data
        :return: None
        """
        pass
