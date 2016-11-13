"""
 Shows a simple group.

"""

from pylibui.core import App
from pylibui.controls import Window, Group, Button


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)

button = Button('My Label')
group = Group('my Group')
group.setMargined(True)
group.setChild(button)
window.setChild(group)

window.show()

app.start()
app.close()
