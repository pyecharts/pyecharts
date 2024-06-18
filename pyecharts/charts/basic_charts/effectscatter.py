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
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        polar_index: types.Optional[types.Numeric] = None,
        geo_index: types.Optional[types.Numeric] = None,
        calendar_index: types.Optional[types.Numeric] = None,
        dataset_index: types.Optional[types.Numeric] = None,
        color: types.Optional[str] = None,
        color_by: types.Optional[str] = None,
        is_legend_hover_link: bool = True,
        show_effect_on: str = "render",
        coordinate_system: str = "cartesian2d",
        symbol: types.Optional[str] = None,
        symbol_size: types.Numeric = 10,
        symbol_rotate: types.Optional[types.Numeric] = None,
        selected_mode: types.Union[bool, str] = False,
        label_opts: types.Label = opts.LabelOpts(),
        effect_opts: types.Effect = opts.EffectOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        markarea_opts: types.MarkArea = None,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name)

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
                "polarIndex": polar_index,
                "geoIndex": geo_index,
                "calendarIndex": calendar_index,
                "colorBy": color_by,
                "legendHoverLink": is_legend_hover_link,
                "showEffectOn": show_effect_on,
                "rippleEffect": effect_opts,
                "coordinateSystem": coordinate_system,
                "datasetIndex": dataset_index,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "symbolRotate": symbol_rotate,
                "selectedMode": selected_mode,
                "data": y_axis,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
                "zlevel": z_level,
                "z": z,
                "encode": encode,
            }
        )
        return self
