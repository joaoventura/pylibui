# pylibui

Python3 wrapper for [libui](https://github.com/andlabs/libui/). It uses ctypes 
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
window.setMargined(1)
window.show()

app.start()
app.close()
```


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

I'm accepting pull requests if the code is cleaned and it comes with an example.
