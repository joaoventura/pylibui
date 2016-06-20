"""
 Pylibui test suite.

"""

from pylibui.controls import Tab, Button
from tests.utils import WindowTestCase


class TabTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.tab = Tab()

    def test_can_append_pages_to_tab(self):
        """Tests that we can append pages to tab."""
        button = Button('my button')
        self.tab.append('my tab 1', button)

        button2 = Button('second button')
        self.tab.append('second tab', button2)

        self.assertEqual(self.tab.getNumPages(), 2)

    def test_can_append_pages_at_specified_index(self):
        """Tests that we can append pages at a specified index."""
        button = Button('my button')
        self.tab.append('my tab 1', button)

        button2 = Button('second button')
        self.tab.insertAt('my tab 1', 0, button2)

        # TODO: should we do a check on indexes when user calls `insertAt` ?
        #       At the moment, the following code crashes:
        # button3 = Button('second button')
        # self.tab.insertAt('my tab 3', 10, button3) # non-existing page index

    def test_can_delete_pages_from_tab(self):
        """Tests that we can delete pages from tab."""
        button = Button('my button')
        self.tab.append('my tab 1', button)
        self.assertEqual(self.tab.getNumPages(), 1)

        self.tab.delete(0)
        self.assertEqual(self.tab.getNumPages(), 0)

        # TODO: should we do a check on indexes when user calls `delete` ?
        #       At the moment, the following code crashes:
        # self.tab.delete(40) # non-existing page index

    def test_tab_margins(self):
        """Tests that we can set/get the margins of the tab."""

        # we first have to add a page to the tab
        button = Button('my button')
        self.tab.append('my tab 1', button)

        self.assertEqual(self.tab.getMargined(0), 0)

        margin = 20
        self.tab.setMargined(0, margin)
        self.assertEqual(self.tab.getMargined(0), margin)

        # TODO: should we do a check on indexes when user calls `getMargined` +
        #       `setMargined` ? At the moment, the following code crashes:
        # self.tab.setMargined(40, margin) # non-existing page index
