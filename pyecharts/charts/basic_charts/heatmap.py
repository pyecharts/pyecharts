from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class HeatMap(RectChart):
    """
    <<< HeatMap >>>

    The heat map is mainly used to represent the size of the value by color,
    which must be used in conjunction with the visualMap component.
    Two categories of axes must be used in rectangular coordinates.
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.set_global_opts(visualmap_opts=opts.VisualMapOpts(orient="horizontal"))

    def add_yaxis(
        self,
        series_name: str,
        yaxis_data: types.Sequence[types.Union[dict]],
        value: types.Sequence[types.Union[dict]],
        *,
        coordinate_system: str = "cartesian2d",
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        geo_index: types.Optional[types.Numeric] = None,
        calendar_index: types.Optional[types.Numeric] = None,
        dataset_index: types.Optional[types.Numeric] = None,
        point_size: types.Optional[types.Numeric] = None,
        blur_size: types.Optional[types.Numeric] = None,
        min_opacity: types.Optional[types.Numeric] = None,
        max_opacity: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        markarea_opts: types.MarkArea = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        selected_mode: types.Union[bool, str] = False,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        self._append_legend(series_name)
        self.options.get("yAxis")[0].update(data=yaxis_data)
        self.options.get("series").append(
            {
                "type": ChartType.HEATMAP,
                "name": series_name,
                "coordinateSystem": coordinate_system,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "geoIndex": geo_index,
                "calendarIndex": calendar_index,
                "datasetIndex": dataset_index,
                "pointSize": point_size,
                "blurSize": blur_size,
                "minOpacity": min_opacity,
                "maxOpacity": max_opacity,
                "data": value,
                "label": label_opts,
                "markLine": markline_opts,
                "markPoint": markpoint_opts,
                "markArea": markarea_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "selectedMode": selected_mode,
                "zlevel": z_level,
                "z": z,
                "encode": encode,
            }
        )
        return self
