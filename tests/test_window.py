"""
 Pylibui test suite.

"""

from tests.utils import WindowTestCase


class WindowTest(WindowTestCase):

    def test_window_title(self):
        """Tests the window's title"""
        title = 'New window'
        self.window.setTitle(title)
        self.assertEqual(self.window.getTitle(), title)

    def test_window_position(self):
        """Tests the window's position."""
        self.window.setPosition(50, 50)
        self.assertEqual(self.window.getPosition(), (50, 50))
