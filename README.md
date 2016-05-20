# pylibui

Python wrapper for [libui](https://github.com/andlabs/libui/).


## Some instructions

Clone libui to pylib/libui and run make. The shared library will be inside
pylib/libui/out.

Run "python3 setup.py build" and find the python extension in pylibui/build/lib.
If you try to import it on the build/lib directory will fail because it will
not be able to find the libui shared library. To do that, you will have to
say where the libui shared library is.

    $ cd <path>/pylibui/build/libxxx/
    $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../../libui/out/

Now you can run the Python3 interpreter and run the test function:

    $ python3
    > import pylibui
    > pylibui.test()

If everything went fine, you'll be able to see a window with a Hello World label.
