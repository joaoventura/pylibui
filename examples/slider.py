"""
 Shows a simple slider.

"""

from pylibui.core import App
from pylibui.controls import Window, Slider


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()

class MySlider(Slider):
    
    def onChanged(self, data):
        print(self.getValue())

app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(1)

slider = MySlider(0, 100)
slider.setValue(50)
window.setChild(slider)

window.show()

app.start()
app.close()
