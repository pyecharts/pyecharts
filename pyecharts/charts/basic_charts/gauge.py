# coding=utf-8

from ...charts.chart import Chart
from ...options import *
from ...types import *

DEFAULT_GAUGE_TOOLTIP_FORMATTER = "{a} <br/>{b} : {c}%"


class Gauge(Chart):
    """
    <<< 仪表盘 >>>
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        attr: str,
        value: Numeric,
        min_: Numeric = 0,
        max_: Numeric = 100,
        start_angle: Numeric = 225,
        end_angle: Numeric = -45,
    ):

        self.options.get("legend")[0].get("data").append(name)
        self.options.get("series").append(
            {
                "type": "gauge",
                "detail": {"formatter": "{value}%"},
                "name": name,
                "min": min_,
                "max": max_,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "data": [{"value": value, "name": attr}],
            }
        )
