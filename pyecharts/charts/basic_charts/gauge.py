# coding=utf-8
from ...charts.chart import Chart
from ...commons.types import ListTuple, Numeric, Union
from ...options import InitOpts


class Gauge(Chart):
    """
    <<< 仪表盘 >>>
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        data_pair: ListTuple,
        min_: Numeric = 0,
        max_: Numeric = 100,
        start_angle: Numeric = 225,
        end_angle: Numeric = -45,
    ):
        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "gauge",
                "detail": {"formatter": "{value}%"},
                "name": name,
                "min": min_,
                "max": max_,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "data": [{"value": v, "name": n} for (v, n) in data_pair],
            }
        )
        return self
