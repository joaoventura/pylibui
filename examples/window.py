"""
 Shows an empty window.

"""

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
