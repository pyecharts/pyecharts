# coding=utf-8

from ...charts.chart import Chart
from ...options import InitOpts
from ...types import List, ListTuple, Optional, Union


class Liquid(Chart):
    """
    <<< 水球图 >>>

    主要用来突出数据的百分比。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.js_dependencies.add("liquidfill")

    def add(
        self,
        name: str,
        data: ListTuple,
        shape: str = "circle",
        color: Optional[List[str]] = None,
        is_animation: bool = True,
        is_outline_show: bool = True,
    ):

        _animation_dur, _animation_dur_update = 2000, 1000
        if not is_animation:
            _animation_dur, _animation_dur_update = 0, 0

        color = color or ["#294D99", "#156ACF", "#1598ED", "#45BDFF"]

        self.options.get("series").append(
            {
                "type": "liquidFill",
                "name": name,
                "data": data,
                "waveAnimation": is_animation,
                "animationDuration": _animation_dur,
                "animationDurationUpdate": _animation_dur_update,
                "color": color,
                "shape": shape,
                "outline": {"show": is_outline_show},
            }
        )
