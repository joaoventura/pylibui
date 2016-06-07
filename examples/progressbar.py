"""
 Shows a simple progress bar.

"""

from pylibui.core import App
from pylibui.controls import Window, ProgressBar


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Progress bar example')
window.setMargined(1)

progressbar = ProgressBar()
progressbar.setValue(60)
window.setChild(progressbar)

window.show()

app.start()
app.close()
