"""
 Python wrapper for libui.

"""

import ctypes
import os
from ctypes.util import find_library

lib = find_library('ui')

# if library is not present on the system
if lib is None:
  CURR_PATH = os.path.dirname(os.path.realpath(__file__))
  SHARED_LIBS_PATH = os.path.join(CURR_PATH, 'sharedlibs')
  LIB_PATH = os.path.join(SHARED_LIBS_PATH, 'libui.so')
else:
  import sysconfig
  LIB_PATH = os.path.join(sysconfig.get_config_var('LIBDIR'), lib)

ctypes.cdll.LoadLibrary(LIB_PATH)
clibui = ctypes.CDLL(os.path.join(LIB_PATH))

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
