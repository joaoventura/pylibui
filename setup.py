from distutils.core import setup, Extension


module = Extension(
    'pylibui',
    include_dirs = ['libui'],
    libraries = ['ui'],
    library_dirs = ['libui/out'],
    sources = ['src/pylibui.c', 'src/tests.c']
)

setup(
    name = 'pylibui',
    version = '0.0.1',
    description = 'Python wrapper for libui',
    ext_modules = [module]
)
