"""
 Python wrapper for libui.

"""

from .callback_helper import get_c_callback_func_ptr, c_func_type_int_structp_voidp, c_func_type_void_structp_voidp
from pylibui import libui
from .control import Control


class ColorButton(Control):

    def __init__(self):
        """
        Creates a new color button.

        """
        super().__init__()
        self.control = libui.uiNewColorButton()

        def handler(window, data):
            self.onColorChanged(data)
            return 0

        self.changedHandler = libui.uiColorButtonOnChanged(self.control,
                                                        get_c_callback_func_ptr(handler, c_func_type_void_structp_voidp),
                                                        None)

    def getColor(self):
        '''
        Get color button's color
        :return : color tuple (r, g, b, a)
        '''
        return libui.uiColorButtonColor(self.control)

    def setColor(self, color):
        '''
        Set color button's color

        :param color: new color tuple (r, g, b, a)
        :return : None
        '''
        r, g, b, a = color

        libui.uiColorButtonSetColor(self.control, r, g, b, a)
        
    def onColorChanged(self, data):
        """
        Executes when the color button color changed.

        :param data: data
        :return: None
        """
        pass
