"""
 Pylibui test suite.

"""

from pylibui.controls import Spinbox
from tests.utils import WindowTestCase


class SpinboxTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.spinbox = Spinbox(0, 100)

    def test_value_initial_value(self):
        """Tests the spinbox's `value` initial value is the first parameter
        passed to constructor."""
        spinbox = Spinbox(10, 110)
        self.assertEqual(spinbox.getValue(), 10)

    def test_value_can_be_changed(self):
        """Tests the spinbox's `value` attribute can be changed."""
        value = 30
        self.spinbox.setValue(value)
        self.assertEqual(self.spinbox.getValue(), value)
