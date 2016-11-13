"""
 Pylibui test suite.

"""

from pylibui.controls import Group, Control
from tests.utils import WindowTestCase


class GroupTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.group = Group('my group')

    def test_title_initial_value(self):
        """Tests the group's `title` initial value is the one passed to the
        constructor."""
        self.assertEqual(self.group.getTitle(), 'my group')

    def test_title_can_be_changed(self):
        """Tests the group's `title` attribute can be changed."""
        new_title = 'My new group'
        self.group.setTitle(new_title)
        self.assertEqual(self.group.getTitle(), new_title)

    def test_margins_initial_value(self):
        """Tests the group's `margin` initial value is False."""
        self.assertEqual(self.group.getMargined(), False)

    def test_margins_can_be_changed(self):
        """Tests the group's `margin` attribute can be changed."""
        self.group.setMargined(True)
        self.assertEqual(self.group.getMargined(), True)
