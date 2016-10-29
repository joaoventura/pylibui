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
