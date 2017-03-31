"""
 Python wrapper for libui.

"""

import ctypes

from .callback_helper import get_c_callback_func_ptr
from .callback_helper import c_func_type_void_structp_structp_structp
from .callback_helper import c_func_type_int_structp_structp_structp
from .callback_helper import c_func_type_void_structp_structp
from .callback_helper import c_func_type_void_structp_structp_int

from pylibui import libui
from .control import Control

class AreaHandler(libui.uiAreaHandler):
    def __init__(self, *args, **kwargs):
        super().__init__()

        def handleOnDraw(ah, a, params):
            _draw_params = libui.toUIAreaDrawParamsPointer(params)

            self.onDraw(self._area, _draw_params)

        def handleOnMouseEvent(ah, a, event):
            _mouse_event = libui.toUIAreaMouseEventPointer(event)

            self.onMouseEvent(self._area, _mouse_event)

        def handleOnMouseCrossed(ah, a, left):
            self.onMouseCrossed(self._area, left)

        def handleOnDragBroken(ah, a):
            self.onDragBroken(self._area)

        def handleOnKeyEvent(ah, a, event):
            _key_event = libui.toUIAreaKeyEventPointer(event)

            return self.onKeyEvent(self._area, _key_event)

        self.Draw = get_c_callback_func_ptr(handleOnDraw,
                                                c_func_type_void_structp_structp_structp)
        self.MouseEvent = get_c_callback_func_ptr(handleOnMouseEvent,
                                                c_func_type_void_structp_structp_structp)
        self.MouseCrossed = get_c_callback_func_ptr(handleOnMouseCrossed,
                                                c_func_type_void_structp_structp_int)
        self.DragBroken = get_c_callback_func_ptr(handleOnDragBroken,
                                                c_func_type_void_structp_structp)
        self.KeyEvent = get_c_callback_func_ptr(handleOnKeyEvent,
                                                c_func_type_int_structp_structp_structp)

    def onDraw(self, a, params):
        pass

    def onMouseEvent(self, a, event):
        pass

    def onMouseCrossed(self, a, left):
        pass

    def onDragBroken(self, a):
        pass

    def onKeyEvent(self, a, event):
        return 0

class Area(Control):

    def __init__(self, ah, *args, **kwargs):
        """
        Creates a new Area.

        """
        super().__init__()
        self.control = self._createControl(ah, args, kwargs)
        ah._area = self

    def _createControl(self, ah, *args, **kwargs):
        return libui.uiNewArea(ah)

    def setSize(self, w, h):
        '''
        Set area size

        :param w: int
        :param h: int
        :return : None
        '''
        libui.uiAreaSetSize(self.control, int(w), int(h))

    def redrawAll(self):
        '''
        queue redraw all for area
        :return : None
        '''
        libui.uiAreaQueueRedrawAll(self.control)

    def scrollTo(self, x, y, width, height):
        '''
        scroll aree
        :param x: float
        :param y: float
        :param width: float
        :param height: float
        :return : None
        '''
        libui.scrollTo(self.control, float(x), float(y), float(width), float(height))

    def beginUserWindowMove(self):
        '''
        call only when in mouse event to indicate window move
        :return : None
        '''
        libui.uiAreaBeginUserWindowMove(self.control)

    def beginUserWindowResize(self, edge):
        '''
        call only when in mouse event to indicate window resizen
        :param edge: one of the edge variable uiWindowResizeEdge*
        :return : None
        '''
        libui.uiAreaBeginUserWindowResize(self.control, edge)

class ScrollingArea(Area):
    def __init__(self, ah, w, h):
        super().__init__(ah, w, h)

    def _createControl(self, ah, *args, **kwargs):
        w, h = args
        return libui.uiNewScrollingArea(ah, w, h)
