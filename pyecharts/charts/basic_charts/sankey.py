# coding=utf-8
from ...charts.chart import Chart
from ...commons.types import ListTuple, Numeric, Union
from ...options import InitOpts, LabelOpts, LineStyleOpts


class Sankey(Chart):
    """
    <<< 桑基图  >>>

    桑基图是一种特殊的流图, 它主要用来表示原材料、能量等如何从初始形式经过中
    间过程的加工、转化到达最终形式。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        nodes: ListTuple,
        links: ListTuple,
        node_width: Numeric = 20,
        node_gap: Numeric = 8,
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
        linestyle_opt: Union[LineStyleOpts, dict] = LineStyleOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(linestyle_opt, LineStyleOpts):
            linestyle_opt = linestyle_opt.opts

        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "sankey",
                "name": name,
                "layout": None,
                "data": nodes,
                "links": links,
                "nodeWidth": node_width,
                "nodeGap": node_gap,
                "label": label_opts,
                "lineStyle": linestyle_opt,
            }
        )
        return self
