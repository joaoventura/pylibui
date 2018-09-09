"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class BaseMultilineEntry(Control):

    def getText(self):
        """
        Returns the text of the multiline entry.

        :return: string
        """
        return libui.uiMultilineEntryText(self.control)

    def setText(self, text):
        """
        Sets the text of the multiline entry.

        :param text: string
        :return: None
        """
        libui.uiMultilineEntrySetText(self.control, text)

    def append(self, text):
        """
        Appends some text to the multiline entry.

        :param text: string
        :return: None
        """
        libui.uiMultilineEntryAppend(self.control, text)

    def onChanged(self, data):
        """
        Executes when the multiline entry is changed.

        :param data: data
        :return: None
        """
        pass

    def getReadOnly(self):
        """
        Returns whether the multiline entry is read only or not.

        :return: bool
        """
        return bool(libui.uiMultilineEntryReadOnly(self.control))

    def setReadOnly(self, read_only):
        """
        Sets whether the multiline entry is read only or not.

        :param read_only: bool
        :return: None
        """
        libui.uiMultilineEntrySetReadOnly(self.control, int(read_only))


class MultilineEntry(BaseMultilineEntry):

    def __init__(self):
        """
        Creates a new multiline entry.

        """
        super().__init__()
        self.control = libui.uiNewMultilineEntry()

        def handler(window, data):
            self.onChanged(data)
            return 0

        self.changedHandler = libui.uiMultilineEntryOnChanged(
            self.control, handler, None)


class NonWrappingMultilineEntry(BaseMultilineEntry):

    def __init__(self):
        """
        Creates a new non wrapping multiline entry.

        """
        super().__init__()
        self.control = libui.uiNewNonWrappingMultilineEntry()

        def handler(window, data):
            self.onChanged(data)
            return 0

        self.changedHandler = libui.uiMultilineEntryOnChanged(
            self.control, handler, None)
