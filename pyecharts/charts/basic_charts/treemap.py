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
        leaf_depth: types.Optional[types.Numeric] = None,
        pos_left: types.Optional[str] = None,
        pos_right: types.Optional[str] = None,
        pos_top: types.Optional[str] = None,
        pos_bottom: types.Optional[str] = None,
        width: types.Union[str, types.Numeric] = "80%",
        height: types.Union[str, types.Numeric] = "80%",
        square_ratio: types.Optional[types.JSFunc] = None,
        drilldown_icon: str = "▶",
        roam: types.Union[bool, str] = True,
        node_click: types.Union[bool, str] = "zoomToNode",
        zoom_to_node_ratio: types.Numeric = 0.32 * 0.32,
        levels: types.TreeMapLevel = None,
        visual_min: types.Optional[types.Numeric] = None,
        visual_max: types.Optional[types.Numeric] = None,
        visual_dimension: types.Optional[types.Numeric] = None,
        color_alpha: types.Union[types.Numeric, types.Sequence] = None,
        color_saturation: types.Union[types.Numeric, types.Sequence] = None,
        color_mapping_by: str = "index",
        visible_min: types.Numeric = 10,
        children_visible_min: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(position="inside"),
        upper_label_opts: types.Label = opts.LabelOpts(position="inside"),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        breadcrumb_opts: types.TreeMapBreadcrumb = None,
        emphasis_opts: types.Emphasis = None,
    ):
        self._append_legend(series_name)
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
                "squareRatio": square_ratio,
                "label": label_opts,
                "upperLabel": upper_label_opts,
                "leafDepth": leaf_depth,
                "drillDownIcon": drilldown_icon,
                "roam": roam,
                "nodeClick": node_click,
                "zoomToNodeRatio": zoom_to_node_ratio,
                "levels": levels,
                "visualMin": visual_min,
                "visualMax": visual_max,
                "visualDimension": visual_dimension,
                "colorAlpha": color_alpha,
                "colorSaturation": color_saturation,
                "colorMappingBy": color_mapping_by,
                "visibleMin": visible_min,
                "childrenVisibleMin": children_visible_min,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "breadcrumb": breadcrumb_opts,
                "emphasis": emphasis_opts,
            }
        )
        return self
