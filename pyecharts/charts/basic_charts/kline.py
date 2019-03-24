# coding=utf-8
from ... import options as opts
from ...charts.chart import AxisChart
from ...commons.types import ListTuple, Numeric, Optional, Union
from ...consts import ChartType


class Kline(AxisChart):
    """
    <<< K 线图 >>>

    红涨蓝跌
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[opts.AxisOpts().opts])
        self.set_global_opts(
            xaxis_opt=opts.AxisOpts(is_scale=True),
            yaxis_opt=opts.AxisOpts(is_scale=True),
        )

    def add_yaxis(
        self,
        series_name: str,
        y_axis: ListTuple,
        *,
        xaxis_index: Optional[Numeric] = None,
        yaxis_index: Optional[Numeric] = None,
        markline_opts: Union[opts.MarkLineOpts, dict, None] = None,
        markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,
    ):

        if isinstance(markpoint_opts, opts.MarkPointOpts):
            markpoint_opts = markpoint_opts.opts
        if isinstance(markline_opts, opts.MarkLineOpts):
            markline_opts = markline_opts.opts

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.KLINE,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": y_axis,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
            }
        )
        return self
