# pylibui

Python3 wrapper for [libui](https://github.com/andlabs/libui/). It uses ctypes 
to interface with the libui shared library.


## Usage

    $ python3
    
    from pylibui import libui
    
    # Initialize libui
    options = libui.main.uiInitOptions()
    libui.main.uiInit(options)
    
    # Window
    window = libui.window.uiNewWindow('Window', 640, 480, 1)
    libui.window.uiWindowSetMargined(window, 1)
    
    # Set quit handler
    def onClosing(window, data):
        control = libui.control.uiControlPointer(window)
        libui.control.uiControlDestroy(control)
        libui.main.uiQuit()
    
    onclose = libui.window.uiWindowOnClosing(window, onClosing, None)
    
    # Show window
    control = libui.control.uiControlPointer(window)
    libui.control.uiControlShow(control)
    
    # Main loop
    libui.main.uiMain()


## Build instructions

Clone pylibui:

    $ git clone https://github.com/joaoventura/pylibui

Clone [libui](https://github.com/andlabs/libui/) and build the shared library: 

    $ git clone https://github.com/andlabs/libui/
    $ cd libui
    $ make

The libui shared library will be inside libui/out. Finally, copy the contents 
of out/ to pylibui/libui/sharedlibs.

Now, you can use pylibui:

    $ python3
    >>> from pylibui import libui
