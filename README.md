# pylibui

[![Build Status](https://travis-ci.org/joaoventura/pylibui.svg)](https://travis-ci.org/joaoventura/pylibui)

Python3 wrapper for [libui](https://github.com/andlabs/libui/) and [libui-ng](https://github.com/libui-ng/libui-ng). It uses ctypes 
to interface with the libui shared library.


## Usage

```python    
from pylibui.core import App
from pylibui.controls import Window


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)
window.show()

app.start()
app.close()
```


## Build instructions

Clone pylibui:

    $ git clone https://github.com/joaoventura/pylibui

Clone [libui-ng](https://github.com/libui-ng/libui-ng)(recommended) or [libui](https://github.com/andlabs/libui/) and build the shared library: 

    $ git clone https://github.com/libui-ng/libui-ng
    $ cd libui-ng
    $ # in the top-level libui-ng directory run:
    $ meson setup build [options]
    $ ninja -C build

The libui-ng shared library will be inside build/meson-out/. Copy the contents of it 
to pylibui/libui/sharedlibs. Now, you can use pylibui:

    $ python3
    >>> import pylibui


## Run Tests

The tests are located in the `tests` folder. To run the entire test suite 
execute the following in the outer pylibui directory: 

    $ python3 -m unittest
    ..
    ----------------------------------------------------------------------
    Ran 20 tests in 0.055s
    
    Ok

To execute a single test file:
 
    $ python3 -m unittest tests/test_window.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.033s
    
    Ok
    

## Contributing

The project is divided in two major sections:

* pylibui.libui: a ctypes wrapper around the libui C shared library. 
* pylibui: an object oriented pythonic wrapper that makes calls to pylibui.libui.
 
If you want to contribute, these are the two places that you can implement some
code and make a pull request. 

If the functionality you are looking for is still not implemented in the 
pylibui.libui ctypes wrapper, there's two things you may need to do:

* Implement the function if the function header is already declared (it will have
a TODO in there).
* Generate the function. Use the bindings.py script in scripts/ to generate most 
of the function declarations for a given section of the "ui.h" header file. 
 
If you need to use the bindings.py file, just run it changing the section that 
you want to generate the bindings, copy-paste the contents to an empty file, and
implement the ctypes calls. Most of them are easy, but you can check what's already
done for some guidance.

I'm accepting pull requests if the code is clean and it comes with a working example.
