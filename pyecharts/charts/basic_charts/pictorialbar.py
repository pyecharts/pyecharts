from ... import options as opts
from ...commons.types import Numeric, Optional, Sequence, Union
from ...globals import ChartType
from .. import Bar


class PictorialBar(Bar):
    """
    <<< PictorialBar Chart >>>

    PictorialBar is a histogram that can set various figurative graphic
    elements (such as images, SVG PathData, etc.)
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add_yaxis(
        self,
        series_name: str,
        yaxis_data: Sequence[Union[Numeric, opts.BarItem, dict]],
        *,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        symbol_pos: Optional[str] = None,
        symbol_offset: Optional[Sequence] = None,
        symbol_rotate: Optional[Numeric] = None,
        symbol_repeat: Optional[str] = None,
        symbol_repeat_direction: Optional[str] = None,
        symbol_margin: Union[Numeric, str, None] = None,
        is_symbol_clip: bool = False,
        is_selected: bool = True,
        xaxis_index: Optional[Numeric] = None,
        yaxis_index: Optional[Numeric] = None,
        color: Optional[str] = None,
        category_gap: Union[Numeric, str] = "20%",
        gap: Optional[str] = None,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,
        markline_opts: Union[opts.MarkLineOpts, dict, None] = None,
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
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
                "data": yaxis_data,
                "barCategoryGap": category_gap,
                "barGap": gap,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
