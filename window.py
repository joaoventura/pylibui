"""
 Shows an empty window.

"""

from pylibui.core import App
from pylibui.controls import Window


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()

    def onPositionChange(self, data):
        print('position changed !')

    def onContentSizeChange(self, data):
        print('content size changed !')


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(1)
window.show()

print(window.getPosition())

window.setPosition(50, 50)
assert window.getPosition() == (50, 50)
window.setTitle('hello ppl')
assert window.getTitle() == 'hello ppl'

assert window.getContentSize() == (800, 600)
window.setContentSize(200, 200)

assert window.getFullscreen() == False
# window.setFullscreen(True)

assert window.getBorderless() == False
# window.setBorderless(True)

assert window.getMargined() == 1

window.center()

app.start()
app.close()
