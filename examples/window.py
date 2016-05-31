"""
 Examples for the pylibui.libui module

 Create a simple window.

"""

from pylibui import libui
from pylibui.core import App
from pylibui.window import Window


app = App()

window = Window('Window', 800, 600)
window.setMargined(1)

# Create quit handler
def onClosing(window, data):
    print('On closing..')
    control = libui.uiControlPointer(window)
    libui.uiControlDestroy(control)
    libui.uiQuit()
    return 0

# Keep reference to native C onClosing handler
onclose = libui.uiWindowOnClosing(window.window, onClosing, None)

window.show()

app.start()
app.close()
