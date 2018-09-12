"""
 Shows the two types of multiline entries.

"""

from pylibui.core import App
from pylibui.controls import (Window, Tab, MultilineEntry,
                              NonWrappingMultilineEntry)


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


class MyMultilineEntry(MultilineEntry):

    def onChanged(self, data):
        print('multiline entry changed!')


app = App()

window = MyWindow('Multiline Entry example')
window.setMargined(True)

tab = Tab()
tab.append("Multiline entry", MyMultilineEntry())
tab.append("Non wrapping multiline entry", NonWrappingMultilineEntry())

window.setChild(tab)
window.show()

app.start()
app.close()
