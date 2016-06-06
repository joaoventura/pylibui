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

    def __enter__(self):
     self.start()
     
    def start(self):
        """
        Starts the application main loop.

        :return: None
        """
        libui.uiMain()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        self.close()
        

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
