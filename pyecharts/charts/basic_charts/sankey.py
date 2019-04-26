# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Sequence, Union
from ...globals import ChartType


class Sankey(Chart):
    """
    <<< 桑基图  >>>

    桑基图是一种特殊的流图, 它主要用来表示原材料、能量等如何从初始形式经过中
    间过程的加工、转化到达最终形式。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        nodes: Sequence,
        links: Sequence,
        *,
        is_selected: bool = True,
        node_width: Numeric = 20,
        node_gap: Numeric = 8,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        linestyle_opt: Union[opts.LineStyleOpts, dict] = opts.LineStyleOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(linestyle_opt, opts.LineStyleOpts):
            linestyle_opt = linestyle_opt.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts
        if isinstance(itemstyle_opts, opts.ItemStyleOpts):
            itemstyle_opts = itemstyle_opts.opts

        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.SANKEY,
                "name": series_name,
                "data": nodes,
                "links": links,
                "nodeWidth": node_width,
                "nodeGap": node_gap,
                "label": label_opts,
                "lineStyle": linestyle_opt,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
