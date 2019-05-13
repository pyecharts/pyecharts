from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Sequence, Union
from ...globals import ChartType


class Gauge(Chart):
    """
    <<< Gauge >>>

    The gauge displays a single key business measure.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        data_pair: Sequence,
        *,
        is_selected: bool = True,
        min_: Numeric = 0,
        max_: Numeric = 100,
        start_angle: Numeric = 225,
        end_angle: Numeric = -45,
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        axisline_opts: Union[opts.AxisLineOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.GAUGE,
                "detail": {"formatter": "{value}%"},
                "name": series_name,
                "min": min_,
                "max": max_,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "data": [{"name": n, "value": v} for n, v in data_pair],
                "tooltip": tooltip_opts,
                "axisLine": axisline_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
