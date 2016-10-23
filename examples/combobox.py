"""
 Shows a simple combobox.

"""

from pylibui.core import App
from pylibui.controls import Window, Combobox


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


class MyCombobox(Combobox):

    def onSelected(self, data):
        print(self.selected())


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)

colors = ['Blue', 'Yellow', 'Green', 'Red']
combobox = MyCombobox(colors)
combobox.append('Pink')
combobox.setSelected(3)

window.setChild(combobox)

window.show()

app.start()
app.close()
