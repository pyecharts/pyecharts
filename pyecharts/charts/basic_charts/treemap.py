# coding=utf-8

from ...charts.chart import Chart
from ...options import *
from ...types import *


class TreeMap(Chart):
    """
    <<< 树图 >>>

    树图是一种常见的表达『层级数据』『树状数据』的可视化形式。它主要用面积的方式，
    便于突出展现出『树』的各层级中重要的节点。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        data,
        left_depth=None,
        drilldown_icon="▶",
        visible_min: Numeric = 10,
        label_opt: LabelOpts = LabelOpts(),
    ):
        if isinstance(label_opt, LabelOpts):
            label_opt = label_opt.opts
        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "treemap",
                "name": name,
                "data": data,
                "label": label_opt,
                "leafDepth": left_depth,
                "drillDownIcon": drilldown_icon,
                "visibleMin": visible_min,
            }
        )
