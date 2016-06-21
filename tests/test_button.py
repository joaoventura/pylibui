"""
 Pylibui test suite.

"""

from pylibui.controls import Button
from tests.utils import WindowTestCase


class ButtonTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.button = Button('my button')

    def test_text_initial_value(self):
        """Tests the button's `text` initial value is the one passed to
        constructor."""
        self.assertEqual(self.button.getText(), 'my button')

    def test_text_can_be_changed(self):
        """Tests the button text."""
        text = 'My new button'
        self.button.setText(text)
        self.assertEqual(self.button.getText(), text)

    def test_onClick_is_called_when_user_presses_button(self):
        raise  # TODO: how do we simulate mouse press ?
