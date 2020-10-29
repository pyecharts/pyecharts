from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class EffectScatter(RectChart):
    """
    <<< Scatter plots with ripple effects animation >>>

    Use animation effects to visually highlight designated data set.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Sequence[types.Union[opts.EffectScatterItem, dict]],
        *,
        is_selected: bool = True,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        color: types.Optional[str] = None,
        symbol: types.Optional[str] = None,
        symbol_size: types.Numeric = 10,
        symbol_rotate: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(),
        effect_opts: types.Effect = opts.EffectOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)

        if all([isinstance(d, opts.EffectScatterItem) for d in y_axis]):
            y_axis = y_axis
        else:
            y_axis = [list(z) for z in zip(self._xaxis_data, y_axis)]

        self.options.get("series").append(
            {
                "type": ChartType.EFFECT_SCATTER,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "showEffectOn": "render",
                "rippleEffect": effect_opts,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "symbolRotate": symbol_rotate,
                "data": y_axis,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
