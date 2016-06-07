"""
 Shows a simple button.

"""

from pylibui.core import App
from pylibui.controls import Window, Button


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


class MyButton(Button):

    def onClick(self, data):
        if self.getText() == 'click me':
            self.setText('click me again')
        else:
            self.setText('click me')


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(1)

button = MyButton('click me')
window.setChild(button)

window.show()

app.start()
app.close()
