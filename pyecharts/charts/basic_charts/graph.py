from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Graph(Chart):
    """
    <<< Graph >>>

    The graph is used to represent the relational data.
    """

    def add(
        self,
        series_name: str,
        nodes: types.Sequence[types.GraphNode],
        links: types.Sequence[types.GraphLink],
        categories: types.Union[types.Sequence[types.GraphCategory], None] = None,
        *,
        coordinate_system: types.Optional[str] = None,
        coordinate_system_usage: types.Optional[str] = None,
        coord: types.Union[types.Sequence, types.Numeric, str] = None,
        xaxis_index: types.Optional[types.Numeric] = None,
        xaxis_id: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        yaxis_id: types.Optional[types.Numeric] = None,
        polar_index: types.Optional[types.Numeric] = None,
        polar_id: types.Optional[types.Numeric] = None,
        single_axis_index: types.Optional[types.Numeric] = None,
        single_axis_id: types.Optional[types.Numeric] = None,
        geo_index: types.Optional[types.Numeric] = None,
        geo_id: types.Optional[types.Numeric] = None,
        calendar_index: types.Optional[types.Numeric] = None,
        calendar_id: types.Optional[types.Numeric] = None,
        matrix_index: types.Optional[types.Numeric] = None,
        matrix_id: types.Optional[types.Numeric] = None,
        is_focusnode: bool = True,
        is_roam: bool = True,
        roam_trigger: types.Optional[str] = None,
        node_scale_ratio: types.Numeric = 0.6,
        is_draggable: bool = False,
        is_rotate_label: bool = False,
        layout: str = "force",
        symbol: types.Optional[str] = None,
        symbol_size: types.Numeric = 10,
        edge_length: types.Numeric = 30,
        gravity: types.Numeric = 0.2,
        friction: types.Numeric = 0.6,
        is_layout_animation: bool = True,
        repulsion: types.Numeric = 50,
        edge_label: types.Label = None,
        edge_symbol: types.Union[types.Sequence[str], str] = None,
        edge_symbol_size: types.Numeric = 10,
        label_opts: types.Label = opts.LabelOpts(),
        linestyle_opts: types.LineStyle = opts.LineStyleOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        is_preserve_aspect: bool = False,
        preserve_aspect_align: types.Optional[str] = None,
        preserve_aspect_vertical_align: types.Optional[str] = None,
    ):
        _nodes = []
        for n in nodes:
            if isinstance(n, opts.GraphNode):
                n = n.opts
            _nodes.append(n)

        _links = []
        for link in links:
            if isinstance(link, opts.GraphLink):
                link = link.opts
            _links.append(link)

        if categories:
            for c in categories:
                if isinstance(c, opts.GraphCategory):
                    c = c.opts
                self._append_legend(c.get("name", ""))

        if edge_label is None:
            edge_label = opts.LabelOpts(is_show=False)

        if edge_symbol is None:
            edge_symbol = [None, None]

        self.options.get("series").append(
            {
                "type": ChartType.GRAPH,
                "name": series_name,
                "coordinateSystem": coordinate_system,
                "coordinateSystemUsage": coordinate_system_usage,
                "coord": coord,
                "xaxisIndex": xaxis_index,
                "xaxisId": xaxis_id,
                "yaxisIndex": yaxis_index,
                "yaxisId": yaxis_id,
                "polarIndex": polar_index,
                "polarId": polar_id,
                "singleAxisIndex": single_axis_index,
                "singleAxisId": single_axis_id,
                "geoIndex": geo_index,
                "geoId": geo_id,
                "calendarIndex": calendar_index,
                "calendarId": calendar_id,
                "matrixIndex": matrix_index,
                "matrixId": matrix_id,
                "layout": layout,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "circular": {"rotateLabel": is_rotate_label},
                "force": {
                    "repulsion": repulsion,
                    "gravity": gravity,
                    "edgeLength": edge_length,
                    "friction": friction,
                    "layoutAnimation": is_layout_animation,
                },
                "label": label_opts,
                "lineStyle": linestyle_opts,
                "roam": is_roam,
                "roamTrigger": roam_trigger,
                "nodeScaleRatio": node_scale_ratio,
                "draggable": is_draggable,
                "focusNodeAdjacency": is_focusnode,
                "data": _nodes,
                "categories": categories,
                "edgeLabel": edge_label,
                "edgeSymbol": edge_symbol,
                "edgeSymbolSize": edge_symbol_size,
                "links": _links,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "preserveAspect": is_preserve_aspect,
                "preserveAspectAlign": preserve_aspect_align,
                "preserveAspectVerticalAlign": preserve_aspect_vertical_align,
            }
        )
        return self
