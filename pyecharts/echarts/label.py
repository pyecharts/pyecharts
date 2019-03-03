from pyecharts.echarts.json_serializable import JsonSerializable
from ..types import Numeric


class Label(JsonSerializable):
    def __init__(
        self,
        visibility: bool = False,
        position: str = "inside",
        text_color: str = None,
        text_size: Numeric = 12,
        formatter: str = "",
        chart_type: str = "",
    ):
        super(Label, self).__init__()
        self._config = {
            "show": visibility,
            "position": position,
            "textStyle": {"color": text_color, "fontSize": text_size},
        }

        if chart_type != "graph":
            if formatter is None:
                if chart_type == "pie":
                    formatter = "{b}: {d}%"
        if formatter:
            self._config["formatter"] = formatter


class EmphasisLabel(Label):
    pass


class NormalLabel(Label):
    def __init__(self, position=None, chart_type=None, **kwargs):
        if position is None:
            position = "outside" if chart_type in ["pie", "graph"] else "top"
        super(NormalLabel, self).__init__(
            position=position, chart_type=chart_type, **kwargs
        )
