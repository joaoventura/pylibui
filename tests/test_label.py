"""
 Pylibui test suite.

"""

from pylibui.controls import Label
from tests.utils import WindowTestCase


class LabelTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.label = Label('My label')

    def test_text_attribute(self):
        """Tests the label's `text` attribute."""
        self.assertEqual(self.label.getText(), 'My label')

        text = 'My new label'
        self.label.setText(text)
        self.assertEqual(self.label.getText(), text)
