"""
 Shows a simple form.

"""

from pylibui.core import App
from pylibui.controls import Window, Form, Entry, PasswordEntry


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Form example')
window.setMargined(True)

form = Form()
form.setPadded(True)
form.append('Username', Entry())
form.append('Password', PasswordEntry())
window.setChild(form)

window.show()

app.start()
app.close()
