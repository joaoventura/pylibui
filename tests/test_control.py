"""
 Pylibui test suite.

"""

from pylibui import libui
from pylibui.controls import Control
from tests.utils import WindowTestCase


class ControlTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.control = Control(libui.uiNewButton(''))

    def test_visible_attribute(self):
        """Tests the control's `visible` attribute."""
        self.assertEqual(self.control.getVisible(), True)
        self.control.hide()
        self.assertEqual(self.control.getVisible(), False)
        self.control.show()
        self.assertEqual(self.control.getVisible(), True)

    def test_enabled_attribute(self):
        """Tests the control's `enabled` attribute."""
        self.assertEqual(self.control.getEnabled(), True)
        self.control.setEnabled(False)
        self.assertEqual(self.control.getEnabled(), False)
        self.control.setEnabled(True)
        self.assertEqual(self.control.getEnabled(), True)
