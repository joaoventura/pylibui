"""
 Pylibui test suite.

"""

from pylibui.controls import Combobox
from tests.utils import WindowTestCase


class ComboboxTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.combobox = Combobox()

    def test_set_selected(self):
        """Tests the setSelected method of the combobox."""
        self.combobox.append("option1")
        value = 0
        self.combobox.setSelected(value)
        self.assertEqual(self.combobox.selected(), value)

    def test_can_pass_items_to_constructor(self):
        """Tests user can pass items to the constructor of the combobox."""
        combobox = Combobox(['Blue', 'Yellow', 'Red'])
