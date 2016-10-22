"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class BaseEntry(Control):

    def setText(self, text):
        """
        Sets the text of the entry.

        :param text: string
        :return: None
        """
        libui.uiEntrySetText(self.control, text)

    def getText(self):
        """
        Returns the text of the entry.

        :return: string
        """
        return libui.uiEntryText(self.control)

    def setReadOnly(self, read_only):
        """
        Sets whether the entry is read only or not.

        :param read_only: bool
        :return: None
        """
        libui.uiEntrySetReadOnly(self.control, read_only)

    def getReadOnly(self):
        """
        Returns whether the entry is read only or not.

        :return: bool
        """
        return bool(libui.uiEntryReadOnly(self.control))

    def onChanged(self, data):
        """
        Executes when the entry is changed.

        :param data: data
        :return: None
        """
        pass


class Entry(BaseEntry):

    def __init__(self):
        """
        Creates a new entry.

        """
        super().__init__()
        self.control = libui.uiNewEntry()

        def handler(window, data):
            self.onChanged(data)
            return 0

        self.changedHandler = libui.uiEntryOnChanged(self.control, handler,
                                                     None)


class PasswordEntry(Entry):

    def __init__(self):
        """
        Creates a new password entry.

        """
        super().__init__()
        self.control = libui.uiNewPasswordEntry()

        def handler(window, data):
            self.onChanged(data)
            return 0

        self.changedHandler = libui.uiEntryOnChanged(self.control, handler,
                                                     None)


class SearchEntry(Entry):

    def __init__(self):
        """
        Creates a new search entry.

        """
        super().__init__()
        self.control = libui.uiNewSearchEntry()

        def handler(window, data):
            self.onChanged(data)
            return 0

        self.changedHandler = libui.uiEntryOnChanged(self.control, handler,
                                                     None)
