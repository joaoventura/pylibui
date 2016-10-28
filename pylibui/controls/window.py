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

        self.closeHandler = libui.uiWindowOnClosing(self.control, handler,
                                                    None)

        def handlerOnContentSizeChanged(window, data):
            self.onContentSizeChange(data)
            return 0

        self.contentSizeChangedHandler = libui.uiWindowOnContentSizeChanged(
            self.control, handlerOnContentSizeChanged, None)

    def getTitle(self):
        """
        Returns the window's title.

        :return: string
        """
        return libui.uiWindowTitle(self.control)

    def setTitle(self, title):
        """
        Sets the window's title.

        :param title: string
        :return: None
        """
        libui.uiWindowSetTitle(self.control, title)

    def getContentSize(self):
        """
        Returns the window's content size.

        :return: tuple
        """
        return libui.uiWindowContentSize(self.control)

    def setContentSize(self, width, height):
        """
        Sets the window's content size.

        :param width: int
        :param height: int
        :return: None
        """
        libui.uiWindowSetContentSize(self.control, width, height)

    def getFullscreen(self):
        """
        Returns whether the window is in fullscreen.

        :return: bool
        """
        return bool(libui.uiWindowFullscreen(self.control))

    def setFullscreen(self, fullscreen):
        """
        Sets whether the window is in fullscreen.

        :param fullscreen: bool
        :return: None
        """
        libui.uiWindowSetFullscreen(self.control, int(fullscreen))

    def onContentSizeChange(self, data):
        """
        Executes when window's content size changed.

        :param data: data
        :return: None
        """
        pass

    def onClose(self, data):
        """
        Executes when window is closing.

        :param data: data
        :return: None
        """
        self.destroy()

    def getBorderless(self):
        """
        Returns whether the window is borderless.

        :return: bool
        """
        return bool(libui.uiWindowBorderless(self.control))

    def setBorderless(self, borderless):
        """
        Sets whether the window is borderless.

        :param borderless: bool
        :return: None
        """
        libui.uiWindowSetBorderless(self.control, int(borderless))

    def setChild(self, child):
        """
        Sets a control as child of the window.

        :param child: control
        :return: None
        """
        libui.uiWindowSetChild(self.control, child.pointer())

    def getMargined(self):
        """
        Returns whether the window is margined or not.

        :return: bool
        """
        return bool(libui.uiWindowMargined(self.control))

    def setMargined(self, margined):
        """
        Sets whether the window is margined or not.

        :param margined: bool
        :return: None
        """
        libui.uiWindowSetMargined(self.control, int(margined))
