from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class TreeMap(Chart):
    """
    <<< TreeMap >>>

    TreeMap are a common visual representation of "hierarchical data" and "tree data".
    It mainly uses area to highlight the important nodes in the hierarchy of "tree".
    """

    def add(
        self,
        series_name: str,
        data: types.Sequence[types.Union[opts.TreeItem, dict]],
        *,
        is_selected: bool = True,
        leaf_depth: types.Optional[types.Numeric] = None,
        pos_left: types.Optional[str] = None,
        pos_right: types.Optional[str] = None,
        pos_top: types.Optional[str] = None,
        pos_bottom: types.Optional[str] = None,
        width: types.Union[str, types.Numeric] = "80%",
        height: types.Union[str, types.Numeric] = "80%",
        drilldown_icon: str = "▶",
        roam: types.Union[bool, str] = True,
        node_click: types.Union[bool, str] = "zoomToNode",
        visual_min: types.Optional[types.Numeric] = None,
        visual_max: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.TREEMAP,
                "name": series_name,
                "data": data,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "width": width,
                "height": height,
                "bottom": pos_bottom,
                "label": label_opts,
                "leafDepth": leaf_depth,
                "drillDownIcon": drilldown_icon,
                "roam": roam,
                "nodeClick": node_click,
                "visualMin": visual_min,
                "visualMax": visual_max,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
