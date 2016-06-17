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

        def handlerOnPositionChanged(window, data):
            self.onPositionChange(data)
            return 0

        self.positionChangedHandler = libui.uiWindowOnPositionChanged(
            self.control, handlerOnPositionChanged, None)

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

    def getPosition(self):
        """
        Returns the window's position.

        :return: tuple
        """
        return libui.uiWindowPosition(self.control)

    def setPosition(self, x, y):
        """
        Sets the window's position.

        :param window: uiWindow
        :param x: int
        :param y: int
        :return: None
        """
        libui.uiWindowSetPosition(self.control, x, y)

    def center(self):
        """
        Centers the window (horizontally ?) on screen.

        :return: None
        """
        libui.uiWindowCenter(self.control)

    def onPositionChange(self, data):
        """
        Executes when window's position changed.

        :param data: data
        :return: None
        """
        pass

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
        return libui.uiWindowFullscreen(self.control)

    def setFullscreen(self, fullscreen):
        """
        Sets whether the window is in fullscreen.

        :param fullscreen: bool
        :return: None
        """
        libui.uiWindowSetFullscreen(self.control, fullscreen)

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
        return libui.uiWindowBorderless(self.control)

    def setBorderless(self, borderless):
        """
        Sets whether the window is borderless.

        :param borderless: bool
        :return: None
        """
        libui.uiWindowSetBorderless(self.control, borderless)

    def setChild(self, child):
        """
        Sets a control as child of the window.

        :param child: control
        :return: None
        """
        libui.uiWindowSetChild(self.control, child.pointer())

    def getMargined(self):
        """
        Returns the window's margins.

        :return: int
        """
        return libui.uiWindowMargined(self.control)

    def setMargined(self, margined):
        """
        Sets the window's margins.

        :param margined: int
        :return: None
        """
        libui.uiWindowSetMargined(self.control, margined)
