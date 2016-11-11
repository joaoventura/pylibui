"""
 Shows a simple vertical separator.

"""

from pylibui.core import App
from pylibui.controls import Window, VerticalSeparator


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()

app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)

separator = VerticalSeparator()
window.setChild(separator)

window.show()

app.start()
app.close()
