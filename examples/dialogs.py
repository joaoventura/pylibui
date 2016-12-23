"""
 Shows four dialogs:
 - an open file dialog
 - a save file dialog
 - a message dialog
 - an error dialog

"""

from pylibui.core import App
from pylibui.controls import Window, VerticalBox, Combobox


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


class MyCombobox(Combobox):

    def onSelected(self, data):
        selected = self.selected()
        if (selected == 0):
            print(window.openFile())
        elif (selected == 1):
            print(window.saveFile())
        elif (selected == 2):
            window.showMessage("Message", "Description")
        elif (selected == 3):
            window.showError("Error", "Description")


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)

dialogs = MyCombobox([
    "Open",
    "Save",
    "Message",
    "Error"
])

vbox = VerticalBox()
vbox.append(dialogs)
window.setChild(vbox)

window.show()

app.start()
app.close()
