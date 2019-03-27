# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Optional, Sequence, Union
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
        data: Sequence,
        *,
        is_selected: bool = True,
        left_depth: Optional[Numeric] = None,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        drilldown_icon: str = "▶",
        visible_min: Numeric = 10,
        visible_max: Optional[Numeric] = None,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts

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
                "leafDepth": left_depth,
                "drillDownIcon": drilldown_icon,
                "visibleMin": visible_min,
                "visibleMax": visible_max,
                "tooltip": tooltip_opts,
            }
        )
        return self
