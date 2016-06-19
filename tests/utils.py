"""
 Pylibui test suite.

"""

import unittest

from pylibui.core import App
from pylibui.controls import Window


class WindowTestCase(unittest.TestCase):
    """
    Implements a pylibui window to be used in the
    test suite.

    """

    def setUp(self):
        self.app = App()
        self.window = Window('Window', 800, 600)
