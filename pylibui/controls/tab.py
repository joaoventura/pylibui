"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Tab(Control):

    def __init__(self):
        """
        Creates a new tab.
        """
        super().__init__()
        self.control = libui.uiNewTab()

    def append(self, name, control):
        """
        Appends a control to the tab.

        :param name: str
        :param control: uiControl
        :return: None
        """
        libui.uiTabAppend(self.control, name, control.pointer())

    def insertAt(self, name, before, control):
        """
        Deletes a control from the tab.

        :param name: str
        :param before: int
        :param control: uiControl
        :return: None
        """
        libui.uiTabInsertAt(self.control, name, before, control.pointer())

    def delete(self, index):
        """
        Deletes a control from the tab.

        :param tab: uiTab
        :param index: int
        :return: None
        """
        libui.uiTabDelete(self.control, index)

    def setMargined(self, page, margined):
        """
        Sets the margins of the tab.

        :param page: int
        :param margined: int
        :return: None
        """
        libui.uiTabSetMargined(self.control, page, margined)

    def getMargined(self, page):
        """
        Returs the margins of the tab.

        :param page: int
        :return: int
        """
        return libui.uiTabMargined(self.control, page)

    def getNumPages(self):
        """
        Returns the number of pages in the tab.

        :return: int
        """
        return libui.uiTabNumPages(self.control)
