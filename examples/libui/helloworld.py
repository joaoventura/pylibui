"""
 Examples for the pylibui.libui module

 Create a simple window with a box and a label.

"""

from pylibui import libui


# Initialize libui
options = libui.uiInitOptions()
libui.uiInit(options)

# Window
window = libui.uiNewWindow('Window', 640, 480, 1)
libui.uiWindowSetMargined(window, 1)

# Create quit handler
def onClosing(window, data):
    print('On closing..')
    control = libui.uiControlPointer(window)
    libui.uiControlDestroy(control)
    libui.uiQuit()
    return 0

# Keep reference to native C onClosing handler
onclose = libui.uiWindowOnClosing(window, onClosing, None)

# Create box
box = libui.uiNewVerticalBox()
libui.uiBoxSetPadded(box, 1)
libui.uiWindowSetChild(window, libui.uiControlPointer(box))

# Create label
label = libui.uiNewLabel('Hello World')
libui.uiBoxAppend(box, libui.uiControlPointer(label), 0)

# Show window
control = libui.uiControlPointer(window)
libui.uiControlShow(control)

# Main loop
libui.uiMain()

# Destroy
#libui.uiUninit()
