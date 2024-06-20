from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Kline(RectChart):
    """
    <<< K-line >>>

    K-line shows the highest value, the lowest value,
    the starting value and the ending value of the data on the day,
    which is used to show the daily fluctuation of the data or
    the fluctuation of a certain period.
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True),
            yaxis_opts=opts.AxisOpts(is_scale=True),
        )

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Sequence[types.Union[opts.CandleStickItem, dict]],
        *,
        coordinate_system: str = "cartesian2d",
        color_by: types.Optional[str] = "series",
        bar_width: types.Optional[types.Numeric] = None,
        bar_min_width: types.Optional[types.Numeric] = None,
        bar_max_width: types.Optional[types.Numeric] = None,
        layout: types.Optional[str] = None,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        is_legend_hover_link: bool = True,
        is_hover_animation: bool = True,
        markline_opts: types.MarkLine = None,
        markpoint_opts: types.MarkPoint = None,
        markarea_opts: types.MarkArea = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        selected_mode: types.Union[bool, str] = False,
        is_large: bool = False,
        encode: types.Union[types.JSFunc, dict, None] = None,
        is_clip: bool = True,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
    ):
        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.KLINE,
                "name": series_name,
                "coordinateSystem": coordinate_system,
                "colorBy": color_by,
                "legendHoverLink": is_legend_hover_link,
                "hoverAnimation": is_hover_animation,
                "layout": layout,
                "barWidth": bar_width,
                "barMinWidth": bar_min_width,
                "barMaxWidth": bar_max_width,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": y_axis,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "selectedMode": selected_mode,
                "large": is_large,
                "encode": encode,
                "clip": is_clip,
                "zlevel": z_level,
                "z": z,
            }
        )
        return self
