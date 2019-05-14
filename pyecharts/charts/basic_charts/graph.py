from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Optional, Sequence, Union
from ...globals import ChartType


class Graph(Chart):
    """
    <<< Graph >>>

    The graph is used to represent the relational data.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        nodes: Sequence[Union[opts.GraphNode, dict]],
        links: Sequence[Union[opts.GraphLink, dict]],
        categories: Union[Sequence[Union[opts.GraphCategory, dict]], None] = None,
        *,
        is_selected: bool = True,
        is_focusnode: bool = True,
        is_roam: bool = True,
        is_rotate_label: bool = False,
        layout: str = "force",
        symbol: Optional[str] = None,
        edge_length: Numeric = 50,
        gravity: Numeric = 0.2,
        repulsion: Numeric = 50,
        edge_symbol: Optional[str] = None,
        edge_symbol_size: Numeric = 10,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        linestyle_opts: Union[opts.LineStyleOpts, dict] = opts.LineStyleOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
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
                self._append_legend(c.get("name", ""), is_selected)

        if edge_symbol is None:
            edge_symbol = [None, None]

        self.options.get("series").append(
            {
                "type": ChartType.GRAPH,
                "name": series_name,
                "layout": layout,
                "symbol": symbol,
                "circular": {"rotateLabel": is_rotate_label},
                "force": {
                    "repulsion": repulsion,
                    "edgeLength": edge_length,
                    "gravity": gravity,
                },
                "label": label_opts,
                "lineStyle": linestyle_opts,
                "roam": is_roam,
                "focusNodeAdjacency": is_focusnode,
                "data": _nodes,
                "categories": categories,
                "edgeSymbol": edge_symbol,
                "edgeSymbolSize": edge_symbol_size,
                "links": _links,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
