# coding=utf-8

from ...charts.chart import Chart
from ...options import InitOpts, LabelOpts
from ...types import *


class Tree(Chart):
    """
    <<< 树图 >>>

    树图主要用来可视化树形数据结构，是一种特殊的层次类型，具有唯一的根节点，左子树，和右子树。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)

    @staticmethod
    def _set_collapse_interval(data, interval=0):
        """
        间隔折叠节点，当节点过多时可以解决节点显示过杂间隔。

        :param data: 节点数据
        :param interval: 指定间隔
        """
        if interval <= 0:
            return data
        if data and isinstance(data, list):
            children = data[0].get("children", None)
            if children and interval > 0:
                for index, value in enumerate(children):
                    if index % interval == 0:
                        value.update(collapsed="false")
                return data

    def add(
        self,
        name: str,
        data: ListTuple,
        layout: str = "orthogonal",
        symbol: str = "emptyCircle",
        symbol_size=7,
        orient: str = "LR",
        top: str = "12%",
        left: str = "12%",
        bottom: str = "12%",
        right: str = "12%",
        collapse_interval: Numeric = 0,
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
        leaves_label_opts: Union[LabelOpts, dict] = LabelOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(leaves_label_opts, LabelOpts):
            leaves_label_opts = leaves_label_opts.opts

        _data = self._set_collapse_interval(data, collapse_interval)
        self.options.get("series").append(
            {
                "type": "tree",
                "name": name,
                "data": _data,
                "left": left,
                "right": right,
                "top": top,
                "bottom": bottom,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "layout": layout,
                "orient": orient,
                "label": label_opts,
                "leaves": {"label": leaves_label_opts},
            }
        )
