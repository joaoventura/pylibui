from distutils.core import setup, Extension

module = Extension('pylibui', sources = ['pylibui.c'])

setup (name = 'pylibui',
       version = '0.0.1',
       description = 'Python wrapper for libui',
       ext_modules = [module])
