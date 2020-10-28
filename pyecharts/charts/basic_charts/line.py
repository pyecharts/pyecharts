from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Line(RectChart):
    """
    <<< Line Chart >>>

    Line chart is a graph that connects all data points
    with single line to show the change trend of data.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Sequence[types.Union[opts.LineItem, dict]],
        *,
        is_selected: bool = True,
        is_connect_nones: bool = False,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        color: types.Optional[str] = None,
        is_symbol_show: bool = True,
        symbol: types.Optional[str] = None,
        symbol_size: types.Union[types.Numeric, types.Sequence] = 4,
        stack: types.Optional[str] = None,
        is_smooth: bool = False,
        is_clip: bool = True,
        is_step: bool = False,
        is_hover_animation: bool = True,
        z_level: types.Numeric = 0,
        z: types.Numeric = 0,
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        label_opts: types.Label = opts.LabelOpts(),
        linestyle_opts: types.LineStyle = opts.LineStyleOpts(),
        areastyle_opts: types.AreaStyle = opts.AreaStyleOpts(),
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)

        if all([isinstance(d, opts.LineItem) for d in y_axis]):
            data = y_axis
        else:
            # 合并 x 和 y 轴数据，避免当 X 轴的类型设置为 'value' 的时候，
            # X、Y 轴均显示 Y 轴数据
            data = [list(z) for z in zip(self._xaxis_data, y_axis)]

        self.options.get("series").append(
            {
                "type": ChartType.LINE,
                "name": series_name,
                "connectNulls": is_connect_nones,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "showSymbol": is_symbol_show,
                "smooth": is_smooth,
                "clip": is_clip,
                "step": is_step,
                "stack": stack,
                "data": data,
                "hoverAnimation": is_hover_animation,
                "label": label_opts,
                "lineStyle": linestyle_opts,
                "areaStyle": areastyle_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "zlevel": z_level,
                "z": z,
            }
        )
        return self
