"""
 Shows a window with a vertical box and some labels.

"""

from pylibui.core import App
from pylibui.controls import Window, Label, VerticalBox, Button


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


class MyButton(Button):

    def onClick(self, data):
        vbox.delete(0)
        self.setEnabled(False)


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)

delete = MyButton("Delete 'Hello World!'")

vbox = VerticalBox()
vbox.setPadded(True)
window.setChild(vbox)

vbox.append(Label('Hello World!'))
vbox.append(Label('Goodbye World!'))
vbox.append(delete)

window.show()

app.start()
app.close()
