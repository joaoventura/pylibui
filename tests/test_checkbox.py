"""
 Pylibui test suite.

"""

from pylibui.controls import Checkbox
from tests.utils import WindowTestCase


class CheckboxTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.checkbox = Checkbox('my checkbox')

    def test_text_initial_value(self):
        """Tests the checkbox's `text` initial value is the one passed to
        constructor."""
        self.assertEqual(self.checkbox.getText(), 'my checkbox')

    def test_text_can_be_changed(self):
        """Tests the checkbox's `text` attribute can be changed."""
        text = 'My new checkbox'
        self.checkbox.setText(text)
        self.assertEqual(self.checkbox.getText(), text)

    def test_checked_initial_value(self):
        """Tests the checkbox's `checked` initial value is False."""
        self.assertEqual(self.checkbox.getChecked(), False)

    def test_checked_can_be_set_to_true(self):
        """Tests the checkbox's `checked` attribute can be set to True."""
        self.checkbox.setChecked(True)
        self.assertEqual(self.checkbox.getChecked(), True)

    def test_checked_can_be_set_to_false(self):
        """Tests the checkbox's `checked` attribute can be set to False."""
        self.checkbox.setChecked(False)
        self.assertEqual(self.checkbox.getChecked(), False)
