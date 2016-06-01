"""
 Python wrapper for libui.

"""

from pylibui import libui


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

        def handler(window, data):
            self.onClose(data)
            return 0

        self.closeHandler = libui.uiWindowOnClosing(self.window, handler, None)

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

    def destroy(self):
        """
        Destroys the window.

        :return: None
        """
        control = libui.uiControlPointer(self.window)
        libui.uiControlDestroy(control)

    def onClose(self, data):
        """
        Executes when window is closing.

        :param data: data
        :return: None
        """

        self.destroy()
