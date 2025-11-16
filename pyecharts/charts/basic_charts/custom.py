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

    def register_echarts_x(self, chart_type: str):
        if chart_type not in [
            ChartType.VIOLIN,
            ChartType.STAGE,
            ChartType.DOUGHNUT,
            ChartType.CONTOUR,
            ChartType.BAR_RANGE,
            ChartType.LINE_RANGE,
        ]:
            raise ValueError(f"Not support register this chart type: {chart_type}")

        if chart_type == ChartType.VIOLIN:
            self.js_dependencies.add("echarts-x-violin")
            self.options.update(xAxis=[{}], yAxis=[{}])

        if chart_type == ChartType.STAGE:
            self.js_dependencies.add("echarts-x-stage")
            self.options.update(xAxis=[{}], yAxis=[{}])

        if chart_type == ChartType.DOUGHNUT:
            self.js_dependencies.add("echarts-x-segmented-doughnut")

        if chart_type == ChartType.LINE_RANGE:
            self.js_dependencies.add("echarts-x-line-range")
            self.options.update(xAxis=[{}], yAxis=[{}])

        if chart_type == ChartType.CONTOUR:
            self.js_dependencies.add("echarts-x-contour-d3")
            self.js_dependencies.add("echarts-x-contour")
            self.options.update(xAxis=[{}], yAxis=[{}])

        if chart_type == ChartType.BAR_RANGE:
            self.js_dependencies.add("echarts-x-bar-range")
            self.options.update(xAxis=[{}], yAxis=[{}])

        return self

    def add_xaxis(self, xaxis_data: types.Sequence):
        self.options["xAxis"][0].update(data=xaxis_data)
        self._xaxis_data = xaxis_data
        return self

    def add(
        self,
        series_name: str,
        render_item: types.JSFunc,
        *,
        type_: str = ChartType.CUSTOM,
        color_by: str = "series",
        is_legend_hover_link: bool = True,
        coordinate_system: str = "cartesian2d",
        coordinate_system_usage: types.Optional[str] = None,
        coord: types.Union[types.Sequence, types.Numeric, str] = None,
        x_axis_index: types.Numeric = 0,
        xaxis_id: types.Optional[types.Numeric] = None,
        y_axis_index: types.Numeric = 0,
        yaxis_id: types.Optional[types.Numeric] = None,
        polar_index: types.Numeric = 0,
        polar_id: types.Optional[types.Numeric] = None,
        single_axis_index: types.Optional[types.Numeric] = None,
        single_axis_id: types.Optional[types.Numeric] = None,
        geo_index: types.Numeric = 0,
        geo_id: types.Optional[types.Numeric] = None,
        calendar_index: types.Numeric = 0,
        calendar_id: types.Optional[types.Numeric] = None,
        matrix_index: types.Optional[types.Numeric] = None,
        matrix_id: types.Optional[types.Numeric] = None,
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
        label_opts: types.Label = None,
        emphasis_opts: types.Emphasis = None,
        item_payload_opts: types.CustomItemPayload = None,
    ):
        self._append_legend(series_name)

        self.options.get("series").append(
            {
                "type": type_,
                "name": series_name,
                "renderItem": render_item,
                "colorBy": color_by,
                "legendHoverLink": is_legend_hover_link,
                "coordinateSystem": coordinate_system,
                "coordinateSystemUsage": coordinate_system_usage,
                "coord": coord,
                "xAxisIndex": x_axis_index,
                "xAxisId": xaxis_id,
                "yAxisIndex": y_axis_index,
                "yAxisId": yaxis_id,
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
                "label": label_opts,
                "emphasis": emphasis_opts,
                "itemPayload": item_payload_opts,
            }
        )
        return self
