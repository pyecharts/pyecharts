from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Liquid(Chart):
    """
    <<< Liquid >>>

    The liquid chart is mainly used to highlight the percentage of data.
    """

    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.js_dependencies.add("echarts-liquidfill")

    def add(
        self,
        series_name: str,
        data: types.Sequence,
        *,
        shape: str = "circle",
        color: types.Optional[types.Sequence[str]] = None,
        background_color: types.Union[str, dict, None] = None,
        is_animation: bool = True,
        is_outline_show: bool = True,
        outline_border_distance: types.Numeric = 8,
        outline_itemstyle_opts: types.ItemStyle = None,
        center: types.Sequence = None,
        tooltip_opts: types.Tooltip = None,
        label_opts: types.Label = opts.LabelOpts(font_size=50, position="inside"),
    ):
        _animation_dur, _animation_dur_update = 2000, 1000
        if not is_animation:
            _animation_dur, _animation_dur_update = 0, 0

        color = color or ["#294D99", "#156ACF", "#1598ED", "#45BDFF"]

        self.options.get("series").append(
            {
                "type": ChartType.LIQUID,
                "name": series_name,
                "data": data,
                "waveAnimation": is_animation,
                "animationDuration": _animation_dur,
                "animationDurationUpdate": _animation_dur_update,
                "color": color,
                "shape": shape,
                "backgroundStyle": {"color": background_color},
                "outline": {
                    "show": is_outline_show,
                    "borderDistance": outline_border_distance,
                    "itemStyle": outline_itemstyle_opts,
                },
                "tooltip": tooltip_opts,
                "label": label_opts,
                "center": center,
            }
        )
        return self
