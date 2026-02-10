from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class ThemeRiver(Chart):
    """
    <<< ThemeRiver >>>

    ThemeRiver graph is a special kind of flow graph,
    which is mainly used to show the changes of events or themes
    over a period of time.
    """

    def add(
        self,
        series_name: types.Sequence,
        data: types.Sequence[types.Union[opts.ThemeRiverItem, dict]],
        *,
        color_by: types.Optional[str] = None,
        pos_left: types.Union[str, types.Numeric] = "5%",
        pos_top: types.Union[str, types.Numeric] = "5%",
        pos_right: types.Union[str, types.Numeric] = "5%",
        pos_bottom: types.Union[str, types.Numeric] = "5%",
        width: types.Union[str, types.Numeric] = None,
        height: types.Union[str, types.Numeric] = None,
        coordinate_system: types.Optional[str] = None,
        coordinate_system_usage: types.Optional[str] = None,
        coord: types.Union[types.Sequence, types.Numeric, str] = None,
        single_axis_index: types.Optional[types.Numeric] = None,
        single_axis_id: types.Optional[types.Numeric] = None,
        boundary_gap: types.Optional[types.Sequence] = None,
        label_opts: types.Label = opts.LabelOpts(),
        singleaxis_opts: types.SingleAxis = opts.SingleAxisOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
    ):
        for n in series_name:
            self._append_legend(n)

        self.options.get("series").append(
            {
                "type": ChartType.THEMERIVER,
                "name": series_name,
                "data": data,
                "colorBy": color_by,
                "left": pos_left,
                "top": pos_top,
                "right": pos_right,
                "bottom": pos_bottom,
                "width": width,
                "height": height,
                "coordinateSystem": coordinate_system,
                "coordinateSystemUsage": coordinate_system_usage,
                "coord": coord,
                "singleAxisIndex": single_axis_index,
                "singleAxisId": single_axis_id,
                "boundaryGap": boundary_gap,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
            }
        )

        self.options.update(singleAxis=singleaxis_opts)
        self.options.get("tooltip").update(trigger="axis")
        return self
