from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Optional, Sequence, Union
from ...globals import ChartType


class Tree(Chart):
    """
    <<< Tree diagrams >>>

    Tree diagrams are used primarily to visualize tree data structures,
    which are special hierarchical types with unique root nodes, left subtrees,
    and right subtrees.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    @staticmethod
    def _set_collapse_interval(data, interval):
        """
        间隔折叠节点，当节点过多时可以解决节点显示过杂间隔。

        :param data: 节点数据
        :param interval: 指定间隔
        """
        if interval <= 0:
            return data
        if data and isinstance(data, list):
            for d in data:
                children = d.get("children", None)
                if children and interval > 0:
                    for index, value in enumerate(children):
                        if index % interval == 0:
                            value.update(collapsed="false")
            return data

    def add(
        self,
        series_name: str,
        data: Sequence[Union[opts.TreeItem, dict]],
        *,
        layout: str = "orthogonal",
        symbol: str = "emptyCircle",
        symbol_size: Numeric = 7,
        orient: str = "LR",
        pos_top: Optional[str] = None,
        pos_left: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        pos_right: Optional[str] = None,
        collapse_interval: Numeric = 0,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        leaves_label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        _data = self._set_collapse_interval(data, collapse_interval)
        self.options.get("series").append(
            {
                "type": ChartType.TREE,
                "name": series_name,
                "data": _data,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "layout": layout,
                "orient": orient,
                "label": label_opts,
                "leaves": {"label": leaves_label_opts},
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
