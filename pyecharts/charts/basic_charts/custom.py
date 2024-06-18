from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Custom(Chart):
    """
    <<< Custom >>>

    Custom series allows you to customize the rendering of graphical elements
    in the series. This enables the extension of different charts.
    """

    def add(
        self,
        series_name: str,
        render_item: types.JSFunc,
        *,
        color_by: str = "series",
        is_legend_hover_link: bool = True,
        coordinate_system: str = "cartesian2d",
        x_axis_index: types.Numeric = 0,
        y_axis_index: types.Numeric = 0,
        polar_index: types.Numeric = 0,
        geo_index: types.Numeric = 0,
        calendar_index: types.Numeric = 0,
        dataset_index: types.Numeric = 0,
        series_layout_by: str = "column",
        selected_mode: types.Union[bool, str] = False,
        dimensions: types.Optional[types.Sequence] = None,
        encode: types.Union[types.Sequence, dict, None] = None,
        data: types.Optional[types.Sequence] = None,
        is_clip: bool = True,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
        itemstyle_opts: types.ItemStyle = None,
        tooltip_opts: types.Tooltip = None,
        emphasis_opts: types.Emphasis = None,
    ):
        self._append_legend(series_name)

        self.options.get("series").append(
            {
                "type": ChartType.CUSTOM,
                "name": series_name,
                "renderItem": render_item,
                "colorBy": color_by,
                "legendHoverLink": is_legend_hover_link,
                "coordinateSystem": coordinate_system,
                "xAxisIndex": x_axis_index,
                "yAxisIndex": y_axis_index,
                "polarIndex": polar_index,
                "geoIndex": geo_index,
                "calendarIndex": calendar_index,
                "datasetIndex": dataset_index,
                "seriesLayoutBy": series_layout_by,
                "itemStyle": itemstyle_opts,
                "selectedMode": selected_mode,
                "dimensions": dimensions,
                "encode": encode,
                "data": data,
                "clip": is_clip,
                "zlevel": z_level,
                "z": z,
                "tooltip": tooltip_opts,
                "emphasis": emphasis_opts,
            }
        )
        return self
