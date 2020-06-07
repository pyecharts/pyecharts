from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class PictorialBar(RectChart):
    """
    <<< PictorialBar Chart >>>

    PictorialBar is a histogram that can set various figurative graphic
    elements (such as images, SVG PathData, etc.)
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Sequence[types.Union[types.Numeric, opts.BarItem, dict]],
        *,
        symbol: types.Optional[str] = None,
        symbol_size: types.Union[types.Numeric, types.Sequence, None] = None,
        symbol_pos: types.Optional[str] = None,
        symbol_offset: types.Optional[types.Sequence] = None,
        symbol_rotate: types.Optional[types.Numeric] = None,
        symbol_repeat: types.Optional[str] = None,
        symbol_repeat_direction: types.Optional[str] = None,
        symbol_margin: types.Union[types.Numeric, str, None] = None,
        is_symbol_clip: bool = False,
        is_selected: bool = True,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        color: types.Optional[str] = None,
        category_gap: types.Union[types.Numeric, str] = "20%",
        gap: types.Optional[str] = None,
        label_opts: types.Label = opts.LabelOpts(),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        encode: types.Union[types.JsCode, dict] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.PICTORIALBAR,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "symbolPosition": symbol_pos,
                "symbolOffset": symbol_offset,
                "symbolRotate": symbol_rotate,
                "symbolRepeat": symbol_repeat,
                "symbolRepeatDirection": symbol_repeat_direction,
                "symbolMargin": symbol_margin,
                "symbolClip": is_symbol_clip,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": y_axis,
                "barCategoryGap": category_gap,
                "barGap": gap,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
