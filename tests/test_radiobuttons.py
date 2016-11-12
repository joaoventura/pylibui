"""
 Pylibui test suite.

"""

from pylibui.controls import RadioButtons
from tests.utils import WindowTestCase


class RadioButtonsTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.radio_buttons = RadioButtons()

    def test_set_selected(self):
        """Tests the setSelected method of the combobox."""
        self.radio_buttons.append("option1")
        self.radio_buttons.append("option2")
        value = 1
        self.radio_buttons.setSelected(value)
        self.assertEqual(self.radio_buttons.selected(), value)
