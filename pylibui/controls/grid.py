"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control
from enum import Enum

class uiAlign(Enum):
    """ 
        Wrapper for the uiAlign enum.
        Alignment specifiers to define placement within the reserved area.

        Used in uiGrid.
    """

    uiAlignFill = 0
    uiAlignStart = 1
    uiAlignCenter = 2
    uiAlignEnd = 3


class uiAt(Enum):
    """
        Wrapper for the uiAt enum.
        Placement specifier to define placement in relation to another control.

        Used in uiGrid.
    """
    
    uiAtLeading = 0
    uiAtTop = 1
    uiAtTrailing = 2
    uiAtBottom = 3


class Grid(Control):

    def __init__(self):
        """
        Creates a new empty grid.

        """
        super().__init__()
        self.control = libui.uiNewGrid()
        self.children = []

    def append(self, control, left, top, xspan, yspan, hexpand, halign, vexpand, valign):
        """
        Appends a control to the grid.

        :param grid: uiGrid
        :param control: uiControl, the control to insert.
        :param left: Placement as number of columns from the left. Integer in range of `[INT_MIN, INT_MAX]`.
        :param top: Placement as number of rows from the top. Integer in range of `[INT_MIN, INT_MAX]`.
        :param xspan: Number of columns to span. Integer in range of `[0, INT_MAX]`.
        :param yspan: Number of rows to span. Integer in range of `[0, INT_MAX]`.
        :param hexpand: `TRUE` to expand reserved area horizontally, `FALSE` otherwise.
        :param halign: Horizontal alignment of the control within the reserved space.
        :param vexpand: `TRUE` to expand reserved area vertically, `FALSE` otherwise.
        :param valign: Vertical alignment of the control within the reserved space.
        :return: None
        """
        libui.uiGridAppend(self.control, control.pointer(), left, top, xspan, yspan, int(hexpand), halign.value, int(vexpand), valign.value)
        self.children.append(control)

    def insertAt(self, control, existing, at, xspan, yspan, hexpand, halign, vexpand, valign):
        """
        Inserts a control positioned in relation to another control within the grid.

        :param grid: uiGrid
        :param control: uiControl, the control to insert.
        :param existing: uiControl, the existing control to position relatively to.
        :param at: Placement specifier in relation to @p existing control.
        :param xspan: Number of columns to span. Integer in range of `[0, INT_MAX]`.
        :param yspan: Number of rows to span. Integer in range of `[0, INT_MAX]`.
        :param hexpand: `TRUE` to expand reserved area horizontally, `FALSE` otherwise.
        :param halign: Horizontal alignment of the control within the reserved space.
        :param vexpand: `TRUE` to expand reserved area vertically, `FALSE` otherwise.
        :param valign: Vertical alignment of the control within the reserved space.
        :return: None
        """
        libui.uiGridInsertAt(self.control, control.pointer(), existing.pointer(), at.value, xspan, yspan, int(hexpand), halign.value, int(vexpand), valign.value)
        self.children.append(control)

    def getPadded(self):
        """
        Returns whether the grid is padded.

        :return: bool
        """
        return bool(libui.uiGridPadded(self.control))

    def setPadded(self, padded):
        """
        Sets whether the grid is padded.

        :param padded: bool
        :return: None
        """
        libui.uiGridSetPadded(self.control, int(padded))
