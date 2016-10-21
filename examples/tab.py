"""
 Shows a simple tab with two pages, one margined, one not margined.

"""

from pylibui.core import App
from pylibui.controls import Window, Tab, HorizontalBox, Label


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 400, 300)
window.setMargined(1)

tab = Tab()

tabPage1 = HorizontalBox()
tabPage2 = HorizontalBox()

labelPage1 = Label("Page 1, margined")
labelPage2 = Label("Page 2, not margined")

tabPage1.append(labelPage1)
tabPage2.append(labelPage2)

tab.append("Page 1", tabPage1)
tab.setMargined(0, 1)

tab.append("Page 2", tabPage2)
tab.setMargined(1, 0)

print("Number of pages: " + str(tab.getNumPages()))

window.setChild(tab)

window.show()

app.start()
app.close()
