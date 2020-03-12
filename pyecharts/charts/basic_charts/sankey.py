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
        pos_left: types.Union[str, types.Numeric] = "5%",
        pos_top: types.Union[str, types.Numeric] = "5%",
        pos_right: types.Union[str, types.Numeric] = "20%",
        pos_bottom: types.Union[str, types.Numeric] = "5%",
        node_width: types.Numeric = 20,
        node_gap: types.Numeric = 8,
        node_align: str = "justify",
        layout_iterations: types.Numeric = 32,
        orient: str = "horizontal",
        is_draggable: bool = True,
        focus_node_adjacency: types.Union[bool, str] = False,
        levels: types.SankeyLevel = None,
        label_opts: types.Label = opts.LabelOpts(),
        linestyle_opt: types.LineStyle = opts.LineStyleOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        if layout_iterations < 32:
            layout_iterations = 32

        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.SANKEY,
                "name": series_name,
                "data": nodes,
                "links": links,
                "left": pos_left,
                "top": pos_top,
                "right": pos_right,
                "bottom": pos_bottom,
                "nodeWidth": node_width,
                "nodeGap": node_gap,
                "nodeAlign": node_align,
                "layoutIteration": layout_iterations,
                "orient": orient,
                "draggable": is_draggable,
                "focusNodeAdjacency": focus_node_adjacency,
                "levels": levels,
                "label": label_opts,
                "lineStyle": linestyle_opt,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
