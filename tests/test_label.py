"""
 Pylibui test suite.

"""

from pylibui.controls import Label
from tests.utils import WindowTestCase


class LabelTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.label = Label('My label')

    def test_text_initial_value(self):
        """Tests the label's `text` initial value is the one passed to the
        constructor."""
        self.assertEqual(self.label.getText(), 'My label')

    def test_text_can_be_changed(self):
        """Tests the label's `text` attribute can be changed."""
        text = 'My new label'
        self.label.setText(text)
        self.assertEqual(self.label.getText(), text)
