import os, sysconfig, sys, subprocess
from ctypes.util import find_library

# search for libui
link = None
for root, dirs, files in os.walk(sysconfig.get_config_var('LIBDIR')):
  for f in files:
    if f == 'libui.so':
      link = os.path.join(root, f)

if link is None:
  raise RuntimeError('Please install libui first')

library = os.readlink(link)

# replicate it on all python environments
command = 'find $HOME/virtualenv -maxdepth 1 -type d -name "python*" -not -name "*system*"'
directories = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
for path in directories.stdout.readlines():
  version = path.decode('utf-8').strip().split(os.sep).pop().replace('python','')
  os.symlink(('/usr/lib/%s' % library), ('/opt/python/%s/lib/%s' % (version, library)))
