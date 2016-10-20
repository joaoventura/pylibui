"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Box(Control):

    def __init__(self):
        """
        Creates a new empty box.

        """
        super().__init__()
        self.children = []

    def append(self, child, stretchy=False):
        """
        Appends a child to the box.

        :param child: control
        :param stretchy: bool
        :return: None
        """
        libui.uiBoxAppend(self.control, child.pointer(), int(stretchy))
        self.children.append(child)

    def delete(self, index):
        """
        Deletes a child from a box.

        :param index: int
        :return: None
        """
        libui.uiBoxDelete(self.control, index)
        self.children[index].destroy()
        del self.children[index]

    def getPadded(self):
        """
        Returns whether the box is padded.

        :return: bool
        """
        return bool(libui.uiBoxPadded(self.control))

    def setPadded(self, padded):
        """
        Sets whether the box is padded.

        :param padded: bool
        :return: None
        """
        libui.uiBoxSetPadded(self.control, int(padded))


class HorizontalBox(Box):

    def __init__(self):
        """
        Creates an empty horizontal box.

        """
        super().__init__()
        self.control = libui.uiNewHorizontalBox()


class VerticalBox(Box):

    def __init__(self):
        """
        Creates an empty vertical box.

        """
        super().__init__()
        self.control = libui.uiNewVerticalBox()
