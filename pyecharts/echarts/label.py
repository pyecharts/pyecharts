from pyecharts.echarts.json_serializable import JsonSerializable


class Label(JsonSerializable):

    def __init__(
        self,
        visibility,
        position,
        text_color,
        text_size,
        formatter=None,
        chart_type=None
    ):
        self.config = {
            "show": visibility,
            "position": position,
            "textStyle": {"color": text_color, "fontSize": text_size},
        }

        if chart_type != 'graph':
            if formatter is None:
                if type == "pie":
                    formatter = "{b}: {d}%"
        if formatter:
            self.config['formatter'] = formatter


class EmphasisLabel(Label):
    pass


class NormalLabel(Label):

    def __init__(
        self,
        visibility,
        position,
        text_color,
        text_size,
        formatter=None,
        chart_type=None
    ):
        if position is None:
            position = "outside" if chart_type in ["pie", "graph"] else "top"
        super(NormalLabel, self).__init__(
            visibility,
            position,
            text_color,
            text_size,
            formatter=formatter,
            chart_type=chart_type
        )
