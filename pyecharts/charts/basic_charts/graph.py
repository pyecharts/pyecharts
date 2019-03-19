# coding=utf-8

from ...charts.chart import Chart
from ...options import InitOpts, LabelOpts, LineStyleOpts
from ...types import Numeric, Union


class Graph(Chart):
    """
    <<< 关系图 >>>

    用于展现节点以及节点之间的关系数据。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        nodes,
        links,
        categories=None,
        is_focusnode: bool = True,
        is_roam: bool = True,
        is_rotate_label: bool = False,
        layout: str = "force",
        symbol=None,
        edge_length: Numeric = 50,
        gravity: Numeric = 0.2,
        repulsion: Numeric = 50,
        edge_symbol=None,
        edge_symbol_size: Numeric = 10,
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
        linestyle_opts: Union[LineStyleOpts, dict] = LineStyleOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts

        if categories:
            for c in categories:
                self._append_legend(c)

        if edge_symbol is None:
            edge_symbol = [None, None]

        self.options.get("series").append(
            {
                "type": "graph",
                "name": name,
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
                "data": nodes,
                "categories": categories,
                "edgeSymbol": edge_symbol,
                "edgeSymbolSize": edge_symbol_size,
                "links": links,
            }
        )
