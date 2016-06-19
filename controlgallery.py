"""
Control gallery example

"""

from pylibui.core import App
from pylibui.controls import Window, Tab, Button


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('libui Control Gallery', 640, 480)
window.setMargined(1)

tab = Tab()
window.setChild(tab)


button = Button('click me')
button2 = Button('click me2')
button3 = Button('click me3')

tab.append('first tab', button)
tab.append('second tab', button2)

tab.insertAt('thirt', 1, button3)

tab.setMargined(0, 30)
assert tab.getMargined(0) == 30
assert tab.getNumPages() == 3

window.show()

app.start()
app.close()
