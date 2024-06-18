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
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        polar_index: types.Optional[types.Numeric] = None,
        is_round_cap: types.Optional[bool] = None,
        color_by: types.Optional[str] = None,
        is_legend_hover_link: bool = True,
        color: types.Optional[str] = None,
        is_realtime_sort: bool = False,
        is_show_background: bool = False,
        background_style: types.Union[types.BarBackground, dict, None] = None,
        stack: types.Optional[str] = None,
        stack_strategy: types.Optional[str] = "samesign",
        sampling: types.Optional[str] = None,
        cursor: types.Optional[str] = "pointer",
        bar_width: types.Union[types.Numeric, str] = None,
        bar_max_width: types.Union[types.Numeric, str] = None,
        bar_min_width: types.Union[types.Numeric, str] = None,
        bar_min_height: types.Numeric = 0,
        category_gap: types.Union[types.Numeric, str] = "20%",
        gap: types.Optional[str] = "30%",
        is_large: bool = False,
        large_threshold: types.Numeric = 400,
        progressive: types.Optional[types.Numeric] = None,
        progressive_threshold: types.Optional[types.Numeric] = None,
        progressive_chunk_mode: types.Optional[str] = None,
        dimensions: types.Union[types.Sequence, None] = None,
        series_layout_by: str = "column",
        dataset_index: types.Numeric = 0,
        is_clip: bool = True,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
        label_opts: types.Label = opts.LabelOpts(),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        markarea_opts: types.MarkArea = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        blur_opts: types.Blur = None,
        select_opts: types.Select = None,
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name)

        if self.options.get("dataset") is not None:
            y_axis = None

        self.options.get("series").append(
            {
                "type": ChartType.BAR,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "polarIndex": polar_index,
                "roundCap": is_round_cap,
                "colorBy": color_by,
                "legendHoverLink": is_legend_hover_link,
                "data": y_axis,
                "realtimeSort": is_realtime_sort,
                "showBackground": is_show_background,
                "backgroundStyle": background_style,
                "stack": stack,
                "stackStrategy": stack_strategy,
                "sampling": sampling,
                "cursor": cursor,
                "barWidth": bar_width,
                "barMaxWidth": bar_max_width,
                "barMinWidth": bar_min_width,
                "barMinHeight": bar_min_height,
                "barCategoryGap": category_gap,
                "barGap": gap,
                "large": is_large,
                "largeThreshold": large_threshold,
                "progressive": progressive,
                "progressiveThreshold": progressive_threshold,
                "progressiveChunkMode": progressive_chunk_mode,
                "dimensions": dimensions,
                "seriesLayoutBy": series_layout_by,
                "datasetIndex": dataset_index,
                "clip": is_clip,
                "zlevel": z_level,
                "z": z,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "blur": blur_opts,
                "select": select_opts,
                "encode": encode,
            }
        )
        return self
