"""
 Python wrapper for libui.

"""

from . import libui


class App:

    def __init__(self):
        """
        Creates a new pylibui app.

        """
        options = libui.uiInitOptions()
        libui.uiInit(options)

    def start(self):
        """
        Starts the application main loop.

        :return: None
        """
        libui.uiMain()

    def stop(self):
        """
        Stops the application main loop.

        :return: None
        """
        libui.uiQuit()

    def close(self):
        """
        Closes the application and frees resources.

        :return: None
        """
        libui.uiUninit()
