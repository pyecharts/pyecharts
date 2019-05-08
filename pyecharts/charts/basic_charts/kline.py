from ... import options as opts
from ...charts.chart import RectChart
from ...commons.types import Numeric, Optional, Sequence, Union
from ...globals import ChartType


class Kline(RectChart):
    """
    <<< K-line >>>

    K-line shows the highest value, the lowest value,
    the starting value and the ending value of the data on the day,
    which is used to show the daily fluctuation of the data or
    the fluctuation of a certain period.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[opts.AxisOpts().opts])
        self.set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True),
            yaxis_opts=opts.AxisOpts(is_scale=True),
        )

    def add_yaxis(
        self,
        series_name: str,
        y_axis: Sequence,
        *,
        is_selected: bool = True,
        xaxis_index: Optional[Numeric] = None,
        yaxis_index: Optional[Numeric] = None,
        markline_opts: Union[opts.MarkLineOpts, dict, None] = None,
        markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.KLINE,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": y_axis,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
