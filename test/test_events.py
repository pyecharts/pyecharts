import unittest

from pyecharts.commons.utils import JsCode
from pyecharts.components.events import Events


class TestEvents(unittest.TestCase):

    def test_mouse_event(self):
        event = Events(chart_id="test_event")
        event.add_mouse_event_handler(
            event_name="click",
            handler=JsCode(
                "function (params) {return params.name + ' : ' + params.value[2];}"
            ),
        )
        events = event.generate_js_mouse_events()
        self.assertEqual(len(events), 1)

    def test_error_mouse_event(self):
        event = Events(chart_id="test_event")

        with self.assertRaises(ValueError):
            event.add_mouse_event_handler(
                event_name="error_click",
                handler=JsCode(
                    "function (params) {return params.name + ' : ' + params.value[2];}"
                ),
            )
