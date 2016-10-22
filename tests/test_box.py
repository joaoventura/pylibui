"""
 Pylibui test suite.

"""

from pylibui.controls import HorizontalBox
from tests.utils import WindowTestCase


class BoxTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.hbox = HorizontalBox()

    def test_set_padded(self):
        """Tests the box can be padded."""
        self.hbox.setPadded(True)
        self.assertEqual(self.hbox.getPadded(), True)
