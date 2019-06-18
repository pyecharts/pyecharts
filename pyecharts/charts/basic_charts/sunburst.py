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
        levels: types.Optional[types.Sequence] = None,
        label_opts: types.Label = opts.LabelOpts(),
        itemstyle_opts: types.ItemStyle = None,
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
                "levels": levels,
                "label": label_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
