from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Sequence, Union
from ...globals import ChartType


class Sankey(Chart):
    """
    <<< Sankey >>>

    Sankey diagram is a special flow diagram, which is mainly used to
    express how raw materials, energy and so on from the initial form through
    the intermediate process of processing, transformation to the final form.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
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
