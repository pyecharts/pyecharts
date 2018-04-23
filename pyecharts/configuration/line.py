from pyecharts.configuration.json_serializable import JsonSerializable


class Line(JsonSerializable):

    def __init__(
        self,
        width,
        opacity,
        curve,
        line_type,
        color,
        chart_type=None
    ):
        if color is None and chart_type == 'graph':
            color = '#aaa'
        self.config = {
            "width": width,
            "opacity": opacity,
            "curveness": curve,
            "type": line_type,
            "color": color,
        }
