"""
 Pylibui test suite.

"""

from pylibui.controls import Slider
from tests.utils import WindowTestCase


class SliderTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.slider = Slider(0, 100)

    def test_value_attribute(self):
        """Tests the slider's `value` attribute."""
        self.assertEqual(self.slider.getValue(), 0)

        value = 30
        self.slider.setValue(value)
        self.assertEqual(self.slider.getValue(), value)

    def test_onChanged_is_called_when_user_changes_sliders_value(self):
        raise  # TODO: how do we simulate mouse press ?
