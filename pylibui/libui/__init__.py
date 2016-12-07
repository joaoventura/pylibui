"""
 Python wrapper for libui.

"""

import ctypes
import os

if os.path.exists('sharedlibs'):
  current = os.path.dirname(os.path.realpath(__file__))
  path = os.path.join(current, 'sharedlibs')
  import platform
  if platform.system() == 'Linux':
    library = os.path.join(path, 'libui.so')
  elif platform.system() == 'Darwin':
    library = os.path.join(path, 'libui.dylib')
  elif platform.system() == 'Windows':
    library = os.path.join(path, 'libui.dll')
  else:
    raise RuntimeError('Unsupported platform')
else:
  import sysconfig
  from ctypes.util import find_library
  library = os.path.join(sysconfig.get_config_var('LIBDIR'), find_library('ui'))

ctypes.cdll.LoadLibrary(library)
clibui = ctypes.CDLL(os.path.join(library))

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
