"""
 Pylibui test suite.

"""

from pylibui.controls import Spinbox
from tests.utils import WindowTestCase


class SpinboxTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.spinbox = Spinbox(0, 100)

    def test_value_attribute(self):
        """Tests the spinbox's `value` attribute."""
        self.assertEqual(self.spinbox.getValue(), 0)

        value = 30
        self.spinbox.setValue(value)
        self.assertEqual(self.spinbox.getValue(), value)

    def test_onChanged_is_called_when_user_changes_spinbox_value(self):
        raise  # TODO: how do we simulate mouse press ?
