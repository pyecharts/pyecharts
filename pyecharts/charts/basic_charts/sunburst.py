from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Sunburst(Chart):
    """
    <<< Sunburst >>

    Sunburst graphs are composed of multiple layers of ring graphs.
    In terms of data structure, inner circle is the parent node of outer circle.
    Therefore, it can represent local and global proportions like pie charts and
    hierarchical relationships like rectangle tree graphs.
    """

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence,
        *,
        center: types.Optional[types.Sequence] = None,
        radius: types.Optional[types.Sequence] = None,
        highlight_policy: str = "descendant",
        node_click: str = "rootToNode",
        sort_: types.Optional[types.JSFunc] = "desc",
        is_render_label_for_zero_data: bool = False,
        is_clockwise: bool = True,
        start_angle: types.Numeric = 90,
        levels: types.Optional[types.Sequence[types.SunburstLevelOpts]] = None,
        label_opts: types.Label = opts.LabelOpts(),
        label_line_opts: types.SunburstLabelLine = None,
        label_layout_opts: types.SunburstLabelLayout = None,
        itemstyle_opts: types.ItemStyle = None,
        tooltip_opts: types.Tooltip = None,
        emphasis_opts: types.Emphasis = None,
    ):
        if not center:
            center = ["50%", "50%"]
        if not radius:
            radius = ["0%", "75%"]

        self.options.get("series").append(
            {
                "type": ChartType.SUNBURST,
                "name": series_name,
                "data": data_pair,
                "center": center,
                "radius": radius,
                "highlightPolicy": highlight_policy,
                "nodeClick": node_click,
                "sort": sort_,
                "renderLabelForZeroData": is_render_label_for_zero_data,
                "clockwise": is_clockwise,
                "startAngle": start_angle,
                "levels": levels,
                "label": label_opts,
                "labelLine": label_line_opts,
                "labelLayout": label_layout_opts,
                "itemStyle": itemstyle_opts,
                "tooltip": tooltip_opts,
                "emphasis": emphasis_opts,
            }
        )
        return self
