from ..types import JSFunc


class Events:

    MOUSE_EVENTS = [
        "click",
        "dblclick",
        "mousedown",
        "mousemove",
        "mouseup",
        "mouseover",
        "mouseout",
        "globalout",
        "contextmenu",
    ]

    def __init__(self, chart_id: str):
        self._chart_id = chart_id
        self._event_handlers = []

    def add_mouse_event_handler(self, event_name: str, handler: JSFunc):
        if event_name not in self.MOUSE_EVENTS:
            raise ValueError(f"Invalid event name: {event_name}")

        self._event_handlers.append((event_name, handler))
        return self

    def generate_js_mouse_events(self):
        return [
            f"chart_{self._chart_id}.on('{name}', function(params) {{{handler}}})"
            for name, handler in self._event_handlers
        ]
