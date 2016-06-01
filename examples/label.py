"""
 Shows a window with a label as child.

"""

from pylibui.core import App
from pylibui.controls import Window, Label


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(1)

label = Label('Hello World!')
window.setChild(label)

window.show()

app.start()
app.close()
