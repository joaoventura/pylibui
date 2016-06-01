"""
 Shows an empty window.

"""

from pylibui.core import App
from pylibui.controls import Window


def close(window, data):
    window.destroy()
    app.stop()


app = App()

window = Window('Window', 800, 600)
window.setMargined(1)
window.onClose(close)
window.show()

app.start()
app.close()
