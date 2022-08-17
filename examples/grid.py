"""
 Shows a simple form.

"""

from pylibui.core import App
from pylibui.controls import Window, Grid, Label, uiAlign, uiAt


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Form example')
window.setMargined(True)

grid = Grid()
grid.setPadded(True)
grid.append(Label("(1, 1)"), 0, 0, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)
grid.insertAt(Label("(1, 2)"), grid.children[0], uiAt.uiAtTrailing, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)
grid.insertAt(Label("(1, 3)"), grid.children[1], uiAt.uiAtTrailing, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)
grid.insertAt(Label("(2, 1)"), grid.children[0], uiAt.uiAtBottom, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)
grid.insertAt(Label("(3, 1)"), grid.children[3], uiAt.uiAtBottom, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)
grid.insertAt(Label("(3, 2)"), grid.children[4], uiAt.uiAtTrailing, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)
grid.insertAt(Label("(3, 3)"), grid.children[5], uiAt.uiAtTrailing, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)
grid.insertAt(Label("(2, 3)"), grid.children[6], uiAt.uiAtTop, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)
grid.insertAt(Label("(2, 2)"), grid.children[7], uiAt.uiAtLeading, 1, 1, True, uiAlign.uiAlignCenter, True, uiAlign.uiAlignCenter)

window.setChild(grid)

window.show()

app.start()
app.close()
