"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Group(Control):

    def __init__(self, title):
        """
        Creates a new group.

        :param title: string
        """
        super().__init__()
        self.control = libui.uiNewGroup(title)

    def getTitle(self):
        """
        Returns the title of the group.

        :return: string
        """
        return libui.uiGroupTitle(self.control)

    def setTitle(self, title):
        """
        Sets the title of the group.

        :param title: string
        :return: None
        """
        libui.uiGroupSetTitle(self.control, title)

    def setChild(self, child):
        """
        Sets a control as child of the group.

        :param child: control
        :return: None
        """
        libui.uiGroupSetChild(self.control, child.pointer())

    def getMargined(self):
        """
        Returns whether the group is margined.

        :return: bool
        """
        return bool(libui.uiGroupMargined(self.control))

    def setMargined(self, margined):
        """
        Sets whether the group is margined.

        :param margined: bool
        :return: None
        """
        libui.uiGroupSetMargined(self.control, int(margined))
