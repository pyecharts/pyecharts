from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import JSFunc, Optional, Sequence, Union
from ...globals import ChartType


class Sunburst(Chart):
    """
    <<< Sunburst >>

    Sunburst graphs are composed of multiple layers of ring graphs.
    In terms of data structure, inner circle is the parent node of outer circle.
    Therefore, it can represent local and global proportions like pie charts and
    hierarchical relationships like rectangle tree graphs.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        data_pair: Sequence,
        *,
        center: Optional[Sequence] = None,
        radius: Optional[Sequence] = None,
        highlight_policy: str = "descendant",
        node_click: str = "rootToNode",
        sort_: Optional[JSFunc] = "desc",
        levels: Optional[Sequence] = None,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
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
