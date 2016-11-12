"""
 Shows a simple radio buttons.

"""

from pylibui.core import App
from pylibui.controls import Window, RadioButtons, VerticalBox


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


class MyRadioButtons(RadioButtons):

    def onSelected(self, data):
        print(self.selected())


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)

colors = ['Blue', 'Yellow', 'Green', 'Red']
radio_buttons = MyRadioButtons(colors)
radio_buttons.append('Pink')
radio_buttons.setSelected(1)

vbox = VerticalBox()
vbox.setPadded(True)
vbox.append(radio_buttons)
window.setChild(vbox)


window.show()

app.start()
app.close()
