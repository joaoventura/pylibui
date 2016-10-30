"""
 Pylibui test suite.

"""

from pylibui.controls import HorizontalSeparator
from tests.utils import WindowTestCase


class SeparatorTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.hseparator = HorizontalSeparator()
