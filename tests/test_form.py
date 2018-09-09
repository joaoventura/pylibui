"""
 Pylibui test suite.

"""

from pylibui.controls import Form, Entry
from tests.utils import WindowTestCase


class FormTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.form = Form()

    def test_can_append(self):
        self.form.append('Username', Entry())
        self.assertEqual(len(self.form.controls), 1)

    def test_can_delete(self):
        self.form.append('Username', Entry())
        self.form.delete(0)
        self.assertEqual(len(self.form.controls), 0)

    def test_set_padded(self):
        """Tests the form can be padded."""
        self.form.setPadded(True)
        self.assertEqual(self.form.getPadded(), True)

