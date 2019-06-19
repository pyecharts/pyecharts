from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Sankey(Chart):
    """
    <<< Sankey >>>

    Sankey diagram is a special flow diagram, which is mainly used to
    express how raw materials, energy and so on from the initial form through
    the intermediate process of processing, transformation to the final form.
    """

    def add(
        self,
        series_name: str,
        nodes: types.Sequence,
        links: types.Sequence,
        *,
        is_selected: bool = True,
        node_width: types.Numeric = 20,
        node_gap: types.Numeric = 8,
        label_opts: types.Label = opts.LabelOpts(),
        linestyle_opt: types.LineStyle = opts.LineStyleOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
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
