A Python library for creating **desktop** application for :

+ Windows
+ Mac OS X
+ Linux (GTK)

This library is a **wrapper** for the great [libui](https://github.com/andlabs/libui)

Installation
------------

As `pylibui` in not **yet** stable, only `beta` version is available on [packagecloud](https://packagecloud.io/waghanza/pylibui/packages/python/pylibui-0.0.1-py2.py3-none-any.whl).

~~~sh
pip install pylibui --extra-index-url=https://packagecloud.io/waghanza/pylibui/pypi/simple
~~~

Getting started
------------

A simple **window** could be started using :

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
