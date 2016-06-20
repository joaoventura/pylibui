"""
 Pylibui test suite.

"""

from pylibui.controls import Checkbox
from tests.utils import WindowTestCase


class CheckboxTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.checkbox = Checkbox('my checkbox')

    def test_text_attribute(self):
        """Tests the checkbox's `text` attribute."""
        text = 'My new checkbox'
        self.checkbox.setText(text)
        self.assertEqual(self.checkbox.getText(), text)

    def test_checked_attribute(self):
        """Tests the checkbox's `checked` attribute."""
        self.assertEqual(self.checkbox.getChecked(), False)
        self.checkbox.setChecked(True)
        self.assertEqual(self.checkbox.getChecked(), True)
        self.checkbox.setChecked(False)
        self.assertEqual(self.checkbox.getChecked(), False)

    def test_onToggle_is_called_when_user_toggles_checkbox(self):
        raise  # TODO: how do we simulate mouse press ?
