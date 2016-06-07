"""
 Shows an empty window.

"""

from pylibui.core import App
from pylibui.controls import Window


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


def main():
    with App():
        window = MyWindow('Window', 800, 600)
        window.setMargined(1)
        window.show()


if __name__ == "__main__":
    main()
