"""
 Pylibui test suite.

"""

from pylibui.controls import ProgressBar
from tests.utils import WindowTestCase


class ProgressBarTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.progressbar = ProgressBar()

    def test_value_initial_value(self):
        """Tests the progressbar's `value` initial value is zero."""
        self.assertEqual(self.progressbar.getValue(), 0)

    def test_value_can_be_changed(self):
        """Tests the progressbar's `value` attribute can be changed."""
        value = 30
        self.progressbar.setValue(value)
        self.assertEqual(self.progressbar.getValue(), value)

        # TODO: should we check for variable type to avoid app crashes ?
        # NOTE: weirdly enough, the sliders don't crash like this; this may
        #       be a bug in libui.
        # with self.assertRaises(ValueError):
        #     self.progressbar.setValue('hello')
