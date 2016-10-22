"""
 Pylibui test suite.

"""

from pylibui.controls import Slider
from tests.utils import WindowTestCase


class SliderTest(WindowTestCase):

    def setUp(self):
        super().setUp()
        self.slider = Slider(0, 100)

    def test_value_initial_value(self):
        """Tests the sliders's `value` initial value is the first parameter
        passed to constructor."""
        slider = Slider(10, 110)
        self.assertEqual(slider.getValue(), 10)

    def test_value_can_be_changed(self):
        """Tests the slider's `value` attribute can be changed."""
        value = 30
        self.slider.setValue(value)
        self.assertEqual(self.slider.getValue(), value)
