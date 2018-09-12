"""
 Python wrapper for libui.

"""

import ctypes
import ctypes.util
import os

# Find system library
lib = ctypes.util.find_library('ui')

# If system library is not available, use embedded one
if not lib:
    curr_path = os.path.dirname(os.path.realpath(__file__))
    lib_dir = os.path.join(curr_path, 'sharedlibs')

    import platform
    ext_hash = { 'darwin': 'dylib', 'windows': 'dll', 'linux': 'so' }
    try:
        ext = ext_hash.get( platform.system().lower())
    except KeyError:
        import sys
        raise RuntimeError( 'Extension type npt found for %', platform.system().lower() )
        sys.exit(1)

    lib = os.path.join(lib_dir, ('libui.%s' % ext))

ctypes.cdll.LoadLibrary(lib)
clibui = ctypes.CDLL(lib)


from .box import *
from .button import *
from .control import *
from .combobox import *
from .checkbox import *
from .datetimepicker import *
from .dialogs import *
from .entry import *
from .form import *
from .group import *
from .label import *
from .main import *
from .multilineentry import *
from .progressbar import *
from .radiobuttons import *
from .separator import *
from .slider import *
from .spinbox import *
from .tab import *
from .window import *
