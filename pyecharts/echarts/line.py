from pyecharts.echarts.json_serializable import JsonSerializable


class Line(JsonSerializable):
    def __init__(
        self,
        width=None,
        opacity=None,
        curve=None,
        line_type=None,
        color=None,
        chart_type=None,
    ):
        if color is None and chart_type == "graph":
            color = "#aaa"
        self._config = {
            "width": width,
            "opacity": opacity,
            "curveness": curve,
            "type": line_type,
            "color": color,
        }
