# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import List, Optional, Sequence, Union
from ...globals import ChartType


class Liquid(Chart):
    """
    <<< 水球图 >>>

    主要用来突出数据的百分比。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.js_dependencies.add("echarts-liquidfill")

    def add(
        self,
        series_name: str,
        data: Sequence,
        *,
        shape: str = "circle",
        color: Optional[List[str]] = None,
        is_animation: bool = True,
        is_outline_show: bool = True,
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
    ):
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts

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
                "outline": {"show": is_outline_show},
                "tooltip": tooltip_opts,
            }
        )
        return self
