from distutils.core import setup, Extension

libui_module = Extension('pylibui._libui',
                             ['pylibui/libui.i'],
                             libraries=['ui'],
                             runtime_library_dirs=['$ORIGIN']
                             )


setup(
    name='pylibui',
    version='0.0.1',
    ext_modules=[libui_module],
    description='Python wrapper for libui',
    packages=['pylibui', 'pylibui.controls']
)
