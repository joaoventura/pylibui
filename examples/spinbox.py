"""
 Shows a simple spinbox.

"""

from pylibui.core import App
from pylibui.controls import Window, Spinbox


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)

spinbox = Spinbox(0, 100)
window.setChild(spinbox)

window.show()

app.start()
app.close()
