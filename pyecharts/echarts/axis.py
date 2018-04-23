import types

from pyecharts.echarts.json_serializable import JsonSerializable


class AxisLabel(JsonSerializable):

    def __init__(
        self,
        interval,
        rotate,
        margin,
        text_size,
        text_color,
        formatter
    ):
        self.config = {
            "interval": interval,
            "formatter": formatter,
            "rotate": rotate,
            "margin": margin,
            "formatter": formatter,
            "textStyle": {"fontSize": text_size, "color": text_color},
        }


class XAxisLabel(AxisLabel):

    def __init__(
        self,
        interval,
        rotate,
        margin,
        text_size,
        text_color,
        formatter
    ):
        super(XAxisLabel, self).__init__(
            interval,
            rotate,
            margin,
            text_size,
            text_color,
            formatter
        )


class YAxisLabel(AxisLabel):

    def __init__(
        self,
        interval,
        rotate,
        margin,
        text_size,
        text_color,
        formatter
    ):
        if not isinstance(formatter, types.FunctionType):
            formatter = "{value} " + formatter
        super(YAxisLabel, self).__init__(
            interval,
            rotate,
            margin,
            text_size,
            text_color,
            formatter
        )


class Axis(JsonSerializable):

    def __init__(
        self,
        name,
        visibility,
        name_location,
        name_gap,
        name_size,
        position,
        boundary_gap,
        label_alignment,
        inverse,
        split_line=True,
        value_range=None,
        axis_type="value",
        chart_type=None
    ):
        self.config = {
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
        }


class XAxis(Axis):

    def __init__(
        self,
        name,
        visibility,
        name_location,
        name_gap,
        name_size,
        position,
        boundary_gap,
        label_alignment,
        inverse,
        split_line=True,
        value_range=None,
        axis_type=None,
        chart_type=None
    ):
        if axis_type is None:
            if chart_type == "scatter":
                axis_type = "value"
            else:
                axis_type = "category"

        super(XAxis, self).__init__(
            name,
            visibility,
            name_location,
            name_gap,
            name_size,
            position,
            boundary_gap,
            label_alignment,
            inverse,
            split_line=split_line,
            value_range=value_range,
            axis_type=axis_type,
            chart_type=chart_type
        )


class YAxis(Axis):

    def __init__(
        self,
        name,
        visibility,
        name_location,
        name_gap,
        name_size,
        position,
        boundary_gap,
        label_alignment,
        inverse,
        split_line=True,
        value_range=None,
        axis_type="value",
        chart_type=None
    ):
        super(YAxis, self).__init__(
            name,
            visibility,
            name_location,
            name_gap,
            name_size,
            position,
            boundary_gap,
            label_alignment,
            inverse,
            split_line=split_line,
            value_range=value_range,
            axis_type=axis_type,
            chart_type=chart_type
        )
