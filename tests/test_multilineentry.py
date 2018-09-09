"""
 Pylibui test suite.

"""

from pylibui.controls import MultilineEntry, NonWrappingMultilineEntry
from tests.utils import WindowTestCase


class MultilineEntryTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.entry = MultilineEntry()

    def test_text_initial_value(self):
        """Tests the multiline entry's `text` initial value is empty."""
        self.assertEqual(self.entry.getText(), '')

    def test_text_can_be_changed(self):
        """Tests the multiline entry's `text` attribute can be changed."""
        text = 'My entry'
        self.entry.setText(text)
        self.assertEqual(self.entry.getText(), text)

    def test_text_can_be_appended(self):
        """Tests the multiline entry's `text` attribute can be appended."""
        self.entry.append('Some')
        self.entry.append('Text')
        self.assertEqual(self.entry.getText(), 'SomeText')

    def test_read_only_initial_value(self):
        """Tests the multiline entry's `read_only` initial value is False."""
        self.assertEqual(self.entry.getReadOnly(), False)

    def test_read_only_can_be_set_to_true(self):
        """Tests the multiline entry's `read_only` attribute can be set
        to True."""
        self.entry.setReadOnly(True)
        self.assertEqual(self.entry.getReadOnly(), True)

    def test_read_only_can_be_set_to_false(self):
        """Tests the multiline entry's `read_only` attribute can be set
        to False."""
        self.entry.setReadOnly(False)
        self.assertEqual(self.entry.getReadOnly(), False)
