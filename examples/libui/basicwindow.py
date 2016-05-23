"""
 Examples for the pylibui.libui module

 Create a simple window.

"""

from pylibui import libui


# Initialize libui
options = libui.main.uiInitOptions()
libui.main.uiInit(options)

# Window
window = libui.window.uiNewWindow('Window', 640, 480, 1)
libui.window.uiWindowSetMargined(window, 1)

# Create quit handler
def onClosing(window, data):
    print('On closing..')
    control = libui.control.uiControlPointer(window)
    libui.control.uiControlDestroy(control)
    libui.main.uiQuit()
    return 0

# Keep reference to native C onClosing handler
onclose = libui.window.uiWindowOnClosing(window, onClosing, None)

# Show window
control = libui.control.uiControlPointer(window)
libui.control.uiControlShow(control)

# Main loop
libui.main.uiMain()

# Destroy
libui.main.uiUninit()
