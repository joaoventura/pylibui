"""
 Python wrapper for libui.

"""

from . import libui


class Window:

    def __init__(self, title, width=800, height=600, menuBar=True):
        """
        Creates a new window.

        :param title: the title of the window
        :param width: the width
        :param height: the height
        :param menuBar: if has menu bar
        """
        self.window = libui.uiNewWindow(title, width, height, int(menuBar))

    def setMargined(self, margined):
        """
        Sets the margins of the window

        :param margined: the margins
        :return: None
        """
        libui.uiWindowSetMargined(self.window, margined)

    def show(self):
        """
        Shows the window.

        :return: None
        """
        control = libui.uiControlPointer(self.window)
        libui.uiControlShow(control)
