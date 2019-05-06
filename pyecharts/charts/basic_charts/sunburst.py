from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import JSFunc, Optional, Sequence, Union
from ...globals import ChartType


class Sunburst(Chart):
    """
    <<< 旭日图 >>>

    旭日图（Sunburst）由多层的环形图组成，在数据结构上，内圈是外圈的父节点。
    因此，它既能像饼图一样表现局部和整体的占比，又能像矩形树图一样表现层级关系。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
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
                "label": label_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
