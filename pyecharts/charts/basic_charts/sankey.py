from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Sankey(Chart):
    """
    <<< Sankey >>>

    Sankey diagram is a special flow diagram, which is mainly used to
    express how raw materials, energy and so on from the initial form through
    the intermediate process of processing, transformation to the final form.
    """

    def add(
        self,
        series_name: str,
        nodes: types.Sequence,
        links: types.Sequence,
        *,
        pos_left: types.Union[str, types.Numeric] = "5%",
        pos_top: types.Union[str, types.Numeric] = "5%",
        pos_right: types.Union[str, types.Numeric] = "20%",
        pos_bottom: types.Union[str, types.Numeric] = "5%",
        width: types.Union[str, types.Numeric] = None,
        height: types.Union[str, types.Numeric] = None,
        coordinate_system: types.Optional[str] = None,
        coordinate_system_usage: types.Optional[str] = None,
        coord: types.Union[types.Sequence, types.Numeric, str] = None,
        calendar_index: types.Optional[types.Numeric] = None,
        calendar_id: types.Optional[types.Numeric] = None,
        matrix_index: types.Optional[types.Numeric] = None,
        matrix_id: types.Optional[types.Numeric] = None,
        node_width: types.Numeric = 20,
        node_gap: types.Numeric = 8,
        node_align: str = "justify",
        layout_iterations: types.Optional[types.Numeric] = None,
        orient: str = "horizontal",
        is_draggable: bool = True,
        center: types.Optional[types.Sequence] = None,
        zoom: types.Numeric = 1,
        is_roam: bool = False,
        roam_trigger: types.Optional[str] = None,
        edge_label_opt: types.Label = None,
        levels: types.SankeyLevel = None,
        label_opts: types.Label = opts.LabelOpts(),
        linestyle_opt: types.LineStyle = opts.LineStyleOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
    ):
        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.SANKEY,
                "name": series_name,
                "data": nodes,
                "links": links,
                "left": pos_left,
                "top": pos_top,
                "right": pos_right,
                "bottom": pos_bottom,
                "width": width,
                "height": height,
                "coordinateSystem": coordinate_system,
                "coordinateSystemUsage": coordinate_system_usage,
                "coord": coord,
                "calendarIndex": calendar_index,
                "calendarId": calendar_id,
                "matrixIndex": matrix_index,
                "matrixId": matrix_id,
                "nodeWidth": node_width,
                "nodeGap": node_gap,
                "nodeAlign": node_align,
                "layoutIterations": layout_iterations,
                "orient": orient,
                "draggable": is_draggable,
                "center": center,
                "zoom": zoom,
                "roam": is_roam,
                "roamTrigger": roam_trigger,
                "edgeLabel": edge_label_opt,
                "levels": levels,
                "label": label_opts,
                "lineStyle": linestyle_opt,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
            }
        )
        return self
