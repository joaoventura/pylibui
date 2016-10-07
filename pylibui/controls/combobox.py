"""
Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Combobox(Control):

    def __init__(self):
        """
        Creates a new combobox.

        """
        super().__init__()
        self.control = libui.uiNewCombobox()

        def handlerOnSelected(combobox, data):
            self.onSelected(data)
            return 0

        self.selectedHandler = libui.uiComboboxOnSelected(
            self.control, handlerOnSelected, None)

    def append(self, text):
        """
        Appends a new to the combobox.

        :param text: string
        :return: None
        """
        libui.uiComboboxAppend(self.control, text)

    def selected(self):
        """
        Returns index of the selected item.

        :return: int
        """
        return libui.uiComboboxSelected(self.control)

    def setSelected(self, n):
        """
        Sets selected item.

        :n: integer
        :return: None
        """
        libui.uiComboboxSetSelected(self.control, n)

    def onSelected(self, data):
        """
        Executes when an item in combobox selected.

        :param data: data
        :return: None
        """
        pass
