# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import List, Numeric, Optional, Union
from ...globals import ChartType


class TreeMap(Chart):
    """
    <<< 树图 >>>

    树图是一种常见的表达『层级数据』『树状数据』的可视化形式。它主要用面积的方式，
    便于突出展现出『树』的各层级中重要的节点。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        data: List[Union[opts.TreeItem, dict]],
        *,
        is_selected: bool = True,
        leaf_depth: Optional[Numeric] = None,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        drilldown_icon: str = "▶",
        visual_min: Optional[Numeric] = None,
        visual_max: Optional[Numeric] = None,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts
        if isinstance(itemstyle_opts, opts.ItemStyleOpts):
            itemstyle_opts = itemstyle_opts.opts

        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.TREEMAP,
                "name": series_name,
                "data": data,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "label": label_opts,
                "leafDepth": leaf_depth,
                "drillDownIcon": drilldown_icon,
                "visualMin": visual_min,
                "visualMax": visual_max,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
