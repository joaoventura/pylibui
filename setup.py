from distutils.core import setup
from setuptools import find_packages

setup(
    name='pylibui',
    version='0.0.1.1',
    description='Python wrapper for libui',
    packages=find_packages(),
    package_data={'pylibui.libui.sharedlibs': '*'},
    include_package_data=True,
)
