"""
 Python wrapper for libui.

"""

import ctypes
import os
import sysconfig
import platform

system = platform.system().lower()

if system == 'darwin':
    extension = 'dylib'
elif system == 'windows':
    extension = 'dll'
elif system == 'linux':
    extension = 'so'

path = os.path.join(sysconfig.get_config_var('LIBDIR'), ('libui.%s' % extension))
ctypes.cdll.LoadLibrary(path)
clibui = ctypes.CDLL(path)


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
