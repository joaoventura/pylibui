"""
 Pylibui test suite.

"""

from pylibui.controls import Tab, Button
from tests.utils import WindowTestCase


class TabTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.tab = Tab()

    def test_append_pages(self):
        """Tests that pages can be appended to a tab."""
        button = Button('my button')
        self.tab.append('my tab 1', button)

        button2 = Button('second button')
        self.tab.append('second tab', button2)

        self.assertEqual(self.tab.getNumPages(), 2)

    def test_append_page_at_index(self):
        """Tests that pages can be appended at a specified index."""
        button = Button('my button')
        self.tab.append('my tab 1', button)

        button2 = Button('second button')
        self.tab.insertAt('my tab 1', 0, button2)

        self.assertEqual(self.tab.getNumPages(), 2)

        # TODO: should we do a check on indexes when user calls `insertAt` ?
        #       At the moment, the following code crashes:
        # button3 = Button('second button')
        # self.tab.insertAt('my tab 3', 10, button3) # non-existing page index

    def test_delete_pages(self):
        """Tests that we can delete pages from tab."""
        button = Button('my button')
        self.tab.append('my tab 1', button)

        self.tab.delete(0)
        self.assertEqual(self.tab.getNumPages(), 0)

        # TODO: should we do a check on indexes when user calls `delete` ?
        #       At the moment, the following code crashes:
        # self.tab.delete(40) # non-existing page index

    def test_margins_initial_value(self):
        """Tests the tab's `margin` initial value is zero."""
        button = Button('my button')
        self.tab.append('my tab 1', button)

        self.assertEqual(self.tab.getMargined(0), 0)

    def test_margins_can_be_changed(self):
        """Tests the tab's `margin` attribute can be changed."""
        # we first have to add a page to the tab
        button = Button('my button')
        self.tab.append('my tab 1', button)

        margin = 20
        self.tab.setMargined(0, margin)
        self.assertEqual(self.tab.getMargined(0), margin)

        # TODO: should we do a check on indexes when user calls `getMargined` +
        #       `setMargined` ? At the moment, the following code crashes:
        # self.tab.setMargined(40, margin) # non-existing page index
