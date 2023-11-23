from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Graph(Chart):
    """
    <<< Graph >>>

    The graph is used to represent the relational data.
    """

    def add(
        self,
        series_name: str,
        nodes: types.Sequence[types.GraphNode],
        links: types.Sequence[types.GraphLink],
        categories: types.Union[types.Sequence[types.GraphCategory], None] = None,
        *,
        is_focusnode: bool = True,
        is_roam: bool = True,
        is_draggable: bool = False,
        is_rotate_label: bool = False,
        layout: str = "force",
        symbol: types.Optional[str] = None,
        symbol_size: types.Numeric = 10,
        edge_length: types.Numeric = 30,
        gravity: types.Numeric = 0.2,
        friction: types.Numeric = 0.6,
        is_layout_animation: bool = True,
        repulsion: types.Numeric = 50,
        edge_label: types.Label = None,
        edge_symbol: types.Union[types.Sequence[str], str] = None,
        edge_symbol_size: types.Numeric = 10,
        label_opts: types.Label = opts.LabelOpts(),
        linestyle_opts: types.LineStyle = opts.LineStyleOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
    ):
        _nodes = []
        for n in nodes:
            if isinstance(n, opts.GraphNode):
                n = n.opts
            _nodes.append(n)

        _links = []
        for link in links:
            if isinstance(link, opts.GraphLink):
                link = link.opts
            _links.append(link)

        if categories:
            for c in categories:
                if isinstance(c, opts.GraphCategory):
                    c = c.opts
                self._append_legend(c.get("name", ""))

        if edge_label is None:
            edge_label = opts.LabelOpts(is_show=False)

        if edge_symbol is None:
            edge_symbol = [None, None]

        self.options.get("series").append(
            {
                "type": ChartType.GRAPH,
                "name": series_name,
                "layout": layout,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "circular": {"rotateLabel": is_rotate_label},
                "force": {
                    "repulsion": repulsion,
                    "gravity": gravity,
                    "edgeLength": edge_length,
                    "friction": friction,
                    "layoutAnimation": is_layout_animation,
                },
                "label": label_opts,
                "lineStyle": linestyle_opts,
                "roam": is_roam,
                "draggable": is_draggable,
                "focusNodeAdjacency": is_focusnode,
                "data": _nodes,
                "categories": categories,
                "edgeLabel": edge_label,
                "edgeSymbol": edge_symbol,
                "edgeSymbolSize": edge_symbol_size,
                "links": _links,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
            }
        )
        return self
