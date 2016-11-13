"""
Shows a window with three date/time pickers.

"""

from pylibui.core import App
from pylibui.controls import (Window, VerticalBox, DateTimePicker, DatePicker,
                              TimePicker)


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)

vbox = VerticalBox()
vbox.setPadded(True)
window.setChild(vbox)

vbox.append(DateTimePicker())
vbox.append(DatePicker())
vbox.append(TimePicker())

window.show()

app.start()
app.close()
