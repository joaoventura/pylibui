"""
 Shows three entries :
 - a simple entry
 - a password entry
 - a search entry

"""

from pylibui.core import App
from pylibui.controls import (Window, Entry, SearchEntry, PasswordEntry,
                              VerticalBox)


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


class MyEntry(Entry):

    def onChanged(self, data):
        print('entry changed!')


app = App()

window = MyWindow('Entry example')
window.setMargined(True)

entry = MyEntry()
search_entry = SearchEntry()
password_entry = PasswordEntry()

vbox = VerticalBox()
vbox.setPadded(True)
vbox.append(entry)
vbox.append(search_entry)
vbox.append(password_entry)

window.setChild(vbox)
window.show()

app.start()
app.close()
