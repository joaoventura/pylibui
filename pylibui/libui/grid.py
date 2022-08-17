"""
 Python wrapper for libui.

"""

import ctypes
from . import clibui

class uiGrid(ctypes.Structure):
    """Wrapper for the uiGrid C struct."""

    pass


def uiGridPointer(obj):
    """
    Casts an object to uiGrid pointer type.

    :param obj: a generic object
    :return: uiGrid
    """

    return ctypes.cast(obj, ctypes.POINTER(uiGrid))


# - void uiGridAppend(uiGrid *g, uiControl *c, int left, int top, int xspan, int yspan, int hexpand, uiAlign halign, int vexpand, uiAlign valign);
def uiGridAppend(grid, control, left, top, xspan, yspan, hexpand, halign, vexpand, valign):
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

    clibui.uiGridAppend(grid, control, left, top, xspan, yspan, hexpand, halign, vexpand, valign)


# - void uiGridInsertAt(uiGrid *g, uiControl *c, uiControl *existing, uiAt at, int xspan, int yspan, int hexpand, uiAlign halign, int vexpand, uiAlign valign);
def uiGridInsertAt(grid, control, existing, at, xspan, yspan, hexpand, halign, vexpand, valign):
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
    clibui.uiGridInsertAt(grid, control, existing, at, xspan, yspan, hexpand, halign, vexpand, valign)


# - int uiGridPadded(uiGrid *g);
def uiGridPadded(grid):
    """
    Returns whether or not controls within the grid are padded.

    Padding is defined as space between individual controls.

    :param grid: uiGrid
    :return: int
    """
    clibui.uiGridPadded(grid)


# - void uiGridSetPadded(uiGrid *g, int padded);
def uiGridSetPadded(grid, padded):
    """
    Sets whether or not controls within the grid are padded.

    Padding is defined as space between individual controls.

    :param grid: uiGrid
    :param padded: int
    :return: None
    """
    clibui.uiGridSetPadded(grid, padded)
    

# - uiGrid *uiNewGrid(void);
def uiNewGrid():
    """
    Creates a new grid.

    :return: uiGrid
    """

    # Set return type
    clibui.uiNewGrid.restype = ctypes.POINTER(uiGrid)

    return clibui.uiNewGrid()
