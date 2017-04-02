# pylibui

Python3 wrapper for [libui](https://github.com/andlabs/libui/). It uses [swig](http://www.swig.org/) 
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

    $ git clone https://github.com/stonewell/pylibui

Clone [libui](https://github.com/andlabs/libui/) and build the shared library: 

    $ git clone https://github.com/andlabs/libui/
    $ cd libui
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make

The libui shared library will be inside libui/build/out.

Build and install pylibui

    python3 setup.py build_ext -I<libui path> --swig-opts="-I<libui path>" -L<libui path>/build/out install
    
cp libui/build/out/libui* to pylibui installation path, For unix user, donot copy the symbol link libui.so

Now, you can use pylibui:

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
    

