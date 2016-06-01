"""
 Shows a window with a vertical box and some labels.

"""

from pylibui.core import App
from pylibui.controls import Window, Label, VerticalBox


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(1)

vbox = VerticalBox()
vbox.setPadded(1)
window.setChild(vbox)

vbox.append(Label('Hello World!'))
vbox.append(Label('Goodbye World!'))

window.show()

app.start()
app.close()
