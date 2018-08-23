import types

from pyecharts.echarts.json_serializable import JsonSerializable


class AxisLabel(JsonSerializable):
    def __init__(
        self,
        interval=None,
        rotate=None,
        margin=None,
        text_size=None,
        text_color=None,
        formatter=None,
    ):
        self._config = {
            "interval": interval,
            "formatter": formatter,
            "rotate": rotate,
            "margin": margin,
            "textStyle": {"fontSize": text_size, "color": text_color},
        }


class XAxisLabel(AxisLabel):
    def __init__(self, **kwargs):
        super(XAxisLabel, self).__init__(**kwargs)


class YAxisLabel(AxisLabel):
    def __init__(self, formatter=None, **kwargs):
        if not isinstance(formatter, types.FunctionType):
            formatter = "{value} " + formatter
        super(YAxisLabel, self).__init__(formatter=formatter, **kwargs)


class Axis(JsonSerializable):
    def __init__(
        self,
        name=None,
        visibility=True,
        name_location="end",
        name_gap=15,
        name_size=12,
        position=None,
        boundary_gap=None,
        label_alignment=None,
        inverse=None,
        split_line=True,
        value_range=None,
        axis_type="value",
        axis_line_color=None,
        axis_line_width=1,
        chart_type=None,
    ):
        self._config = {
            "name": name,
            "show": visibility,
            "nameLocation": name_location,
            "nameGap": name_gap,
            "nameTextStyle": {"fontSize": name_size},
            "axisTick": {"alignWithLabel": label_alignment},
            "inverse": inverse,
            "position": position,
            "boundaryGap": boundary_gap,
            "min": value_range[0],
            "max": value_range[1],
            "type": axis_type,
            "splitLine": {"show": split_line},
            "axisLine": {
                "lineStyle": {
                    "color": axis_line_color,
                    "width": axis_line_width,
                }
            },
        }


class XAxis(Axis):
    def __init__(
        self, axis_type=None, chart_type=None, split_line=False, **kwargs
    ):
        if axis_type is None:
            if chart_type == "scatter":
                axis_type = "value"
            else:
                axis_type = "category"

        super(XAxis, self).__init__(
            axis_type=axis_type, split_line=split_line, **kwargs
        )


class YAxis(Axis):
    def __init__(self, axis_type=None, **kwargs):
        if axis_type is None:
            axis_type = "value"
        super(YAxis, self).__init__(axis_type=axis_type, **kwargs)
