"""
 Shows a simple checkbox.

"""

from pylibui.core import App
from pylibui.controls import Window, Checkbox


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


class MyCheckbox(Checkbox):

    def onToggled(self, data):
        print('checkbox toggled!')


app = App()

window = MyWindow('Checkbox example')
window.setMargined(1)

checkbox = MyCheckbox('a checkbox!')
checkbox.setText('a checkbox')
checkbox.setChecked(True)
window.setChild(checkbox)

window.show()

app.start()
app.close()
