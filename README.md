# pylibui

Python3 wrapper for [libui](https://github.com/andlabs/libui/). It uses ctypes 
to interface with the libui shared library.


## Usage

    :::python3    
    from pylibui.core import App
    from pylibui.controls import Window
    
    
    def close(window, data):
        window.destroy()
        app.stop()
    
    
    app = App()
    
    window = Window('Window', 800, 600)
    window.setMargined(1)
    window.onClose(close)
    window.show()
    
    app.start()
    app.close()


## Build instructions

Clone pylibui:

    $ git clone https://github.com/joaoventura/pylibui

Clone [libui](https://github.com/andlabs/libui/) and build the shared library: 

    $ git clone https://github.com/andlabs/libui/
    $ cd libui
    $ make

The libui shared library will be inside libui/out. Copy the contents of out/ 
to pylibui/libui/sharedlibs. Now, you can use pylibui:

    $ python3
    >>> import pylibui
