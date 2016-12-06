"""
 Python wrapper for libui.

"""

import ctypes
import os
from ctypes.util import find_library

LIB = find_library('ui')

# if library is not present on the system
if LIB is None:
  CURR_PATH = os.path.dirname(os.path.realpath(__file__))
  SHARED_LIBS_PATH = os.path.join(CURR_PATH, 'sharedlibs')
  LIB = os.path.join(SHARED_LIBS_PATH, libname)

ctypes.cdll.LoadLibrary(LIB)
clibui = ctypes.CDLL(LIB)


from .box import *
from .button import *
from .control import *
from .combobox import *
from .checkbox import *
from .datetimepicker import *
from .entry import *
from .group import *
from .label import *
from .main import *
from .progressbar import *
from .radiobuttons import *
from .separator import *
from .slider import *
from .spinbox import *
from .tab import *
from .window import *
