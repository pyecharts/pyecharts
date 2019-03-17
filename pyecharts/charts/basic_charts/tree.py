# coding=utf-8

from ...charts.chart import Chart
from ...options import *


class Tree(Chart):
    """
    <<< 树图 >>>

    树图主要用来可视化树形数据结构，是一种特殊的层次类型，具有唯一的根节点，左子树，和右子树。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
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

    @staticmethod
    def _get_label_config(position, vertical_align, align, text_size, rotate):
        return {
            "position": position,
            "verticalAlign": vertical_align,
            "align": align,
            "fontSize": text_size,
            "rotate": rotate,
        }

    def add(
        self,
        name,
        data,
        layout="orthogonal",
        symbol="emptyCircle",
        symbol_size=7,
        orient="LR",
        top="12%",
        left="12%",
        bottom="12%",
        right="12%",
        collapse_interval=0,
        label_position="left",
        label_vertical_align="middle",
        label_align="right",
        label_text_size=12,
        label_rotate=0,
        leaves_position="right",
        leaves_vertical_align="middle",
        leaves_align="left",
        leaves_text_size=12,
        leaves_rotate=0,
    ):
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
                "label": {
                    "normal": self._get_label_config(
                        position=label_position,
                        vertical_align=label_vertical_align,
                        align=label_align,
                        text_size=label_text_size,
                        rotate=label_rotate,
                    )
                },
                "leaves": {
                    "label": {
                        "normal": self._get_label_config(
                            position=leaves_position,
                            vertical_align=leaves_vertical_align,
                            align=leaves_align,
                            text_size=leaves_text_size,
                            rotate=leaves_rotate,
                        )
                    }
                },
            }
        )
