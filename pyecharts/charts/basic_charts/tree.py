from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Tree(Chart):
    """
    <<< Tree diagrams >>>

    Tree diagrams are used primarily to visualize tree data structures,
    which are special hierarchical types with unique root nodes, left subtrees,
    and right subtrees.
    """

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
        data: types.Sequence[types.Union[opts.TreeItem, dict]],
        *,
        zoom: types.Optional[types.Numeric] = 1,
        layout: str = "orthogonal",
        symbol: types.JSFunc = "emptyCircle",
        symbol_size: types.Union[types.JSFunc, types.Numeric, types.Sequence] = 7,
        orient: str = "LR",
        pos_top: types.Union[str, types.Numeric, None] = None,
        pos_left: types.Union[str, types.Numeric, None] = None,
        pos_bottom: types.Union[str, types.Numeric, None] = None,
        pos_right: types.Union[str, types.Numeric, None] = None,
        width: types.Union[str, types.Numeric, None] = None,
        height: types.Union[str, types.Numeric, None] = None,
        center: types.Optional[types.Sequence[types.Union[str, types.Numeric]]] = None,
        collapse_interval: types.Numeric = 0,
        edge_shape: str = "curve",
        edge_fork_position: str = "50%",
        is_roam: bool = False,
        is_expand_and_collapse: bool = True,
        initial_tree_depth: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(),
        leaves_opts: types.TreeLeavesOpts = opts.TreeLeavesOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        selected_mode: types.Union[bool, str] = False,
        blur_opts: types.Blur = None,
        select_opts: types.Select = None,
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
                "width": width,
                "height": height,
                "center": center,
                "zoom": zoom,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "edgeShape": edge_shape,
                "edgeForkPosition": edge_fork_position,
                "roam": is_roam,
                "expandAndCollapse": is_expand_and_collapse,
                "initialTreeDepth": initial_tree_depth,
                "layout": layout,
                "orient": orient,
                "label": label_opts,
                "leaves": leaves_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "selectedMode": selected_mode,
                "blur": blur_opts,
                "select": select_opts,
            }
        )
        return self
