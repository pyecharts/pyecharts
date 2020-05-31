from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Bar(RectChart):
    """
    <<< Bar Chart >>>

    Bar chart presents categorical data with rectangular bars
    with heights or lengths proportional to the values that they represent.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Sequence[types.Union[types.Numeric, opts.BarItem, dict]],
        *,
        is_selected: bool = True,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        is_legend_hover_link: bool = True,
        color: types.Optional[str] = None,
        is_show_background: bool = False,
        background_style: types.Union[types.BarBackground, dict, None] = None,
        stack: types.Optional[str] = None,
        bar_width: types.Union[types.Numeric, str] = None,
        bar_max_width: types.Union[types.Numeric, str] = None,
        bar_min_width: types.Union[types.Numeric, str] = None,
        bar_min_height: types.Numeric = 0,
        category_gap: types.Union[types.Numeric, str] = "20%",
        gap: types.Optional[str] = "30%",
        is_large: bool = False,
        large_threshold: types.Numeric = 400,
        dimensions: types.Union[types.Sequence, None] = None,
        series_layout_by: str = "column",
        dataset_index: types.Numeric = 0,
        is_clip: bool = True,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
        label_opts: types.Label = opts.LabelOpts(),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)

        if self.options.get("dataset") is not None:
            y_axis = None

        self.options.get("series").append(
            {
                "type": ChartType.BAR,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "legendHoverLink": is_legend_hover_link,
                "data": y_axis,
                "showBackground": is_show_background,
                "backgroundStyle": background_style,
                "stack": stack,
                "barWidth": bar_width,
                "barMaxWidth": bar_max_width,
                "barMinWidth": bar_min_width,
                "barMinHeight": bar_min_height,
                "barCategoryGap": category_gap,
                "barGap": gap,
                "large": is_large,
                "largeThreshold": large_threshold,
                "dimensions": dimensions,
                "seriesLayoutBy": series_layout_by,
                "datasetIndex": dataset_index,
                "clip": is_clip,
                "zlevel": z_level,
                "z": z,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
