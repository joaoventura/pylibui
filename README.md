# pylibui

Python3 wrapper for [libui](https://github.com/andlabs/libui/).


## Usage

    $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../../libui/out/
    $ python3
    >>> import pylibui
    >>> pylibui.init()
    >>> window = pylibui.uiNewWindow('Title', 640, 480, 1)
    >>> pylibui.uiWindowSetMargined(window, 1)
    >>> pylibui.test_show_window(window)
    >>> pylibui.main()
    >>> pylibui.uninit()


## Build instructions

Currently it works in OSX Mavericks and it may work on Linux.

Clone pylibui:

    $ git clone https://github.com/joaoventura/pylibui

Clone libui inside pylibui:

    $ cd pylibui
    $ git clone https://github.com/andlabs/libui/

Make the libui shared library:

    $ cd libui
    $ make

The shared library will be in pylibui/libui/out. Now you can build pylibui:

    $ cd ..
    $ python3 setup.py build

The pylibui shared library will be in pylibui/build/libxxx. Cd into that
directory and try to import it:

    $ cd build/libxxx
    $ python3
    >>> import pylibui
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ImportError: dlopen(...)
        Reason: image not found

You have to explicitly define where the system will find libui's shared lib.

    $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../../libui/out/
    $ python3
    >>> import pylibui

You can now use pylibui.
