# coding=utf-8

from ...charts.chart import Chart
from ...options import *


class Graph(Chart):
    """
    <<< 关系图 >>>

    用于展现节点以及节点之间的关系数据。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        nodes,
        links,
        categories=None,
        is_focusnode=True,
        is_roam=True,
        is_rotate_label=False,
        layout="force",
        symbol=None,
        edge_length=50,
        gravity=0.2,
        repulsion=50,
        edge_symbol=None,
        edge_symbol_size=10,
        label_opts: LabelOpts = LabelOpts(),
        linestyle_opts: LineStyleOpts = LineStyleOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts

        if categories:
            for c in categories:
                self.options.get("legend")[0].get("data").append(c)

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
