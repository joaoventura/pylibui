A Python library for creating **desktop** applications for :

+ Windows
+ Mac OS X
+ Linux (GTK)

This library is a **wrapper** for [libui](https://github.com/andlabs/libui).

Installation
------------

As `pylibui` is not **yet** stable, only `beta` versions are available on [packagecloud](https://packagecloud.io/waghanza/pylibui/packages/python/pylibui-0.0.1-py2.py3-none-any.whl).

~~~sh
pip install pylibui --extra-index-url=https://packagecloud.io/waghanza/pylibui/pypi/simple
~~~

Getting started
------------

A simple **window** application could be built using :

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
