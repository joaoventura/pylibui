"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Window(Control):

    def __init__(self, title, width=800, height=600, menuBar=True):
        """
        Creates a new window.

        :param title: the title of the window
        :param width: the width
        :param height: the height
        :param menuBar: if has menu bar
        """
        super().__init__()
        self.control = libui.uiNewWindow(title, width, height, int(menuBar))

        def handler(window, data):
            self.onClose(data)
            return 0

        self.closeHandler = libui.uiWindowOnClosing(self.control, handler, None)

    def setChild(self, child):
        """
        Sets a control as child of the window.

        :param child: control
        :return: None
        """
        libui.uiWindowSetChild(self.control, child.pointer())

    def setMargined(self, margined):
        """
        Sets the margins of the window

        :param margined: int
        :return: None
        """
        libui.uiWindowSetMargined(self.control, margined)

    def onClose(self, data):
        """
        Executes when window is closing.

        :param data: data
        :return: None
        """
        self.destroy()
