# coding=utf-8
from ... import options as opts
from ...charts.chart import AxisChart
from ...commons.types import ListTuple, Union
from ...consts import CHART_TYPE


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
        name: str,
        y_axis: ListTuple,
        *,
        markline_opts: Union[opts.MarkLineOpts, dict, None] = None,
        markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,
    ):

        if isinstance(markpoint_opts, opts.MarkPointOpts):
            markpoint_opts = markpoint_opts.opts
        if isinstance(markline_opts, opts.MarkLineOpts):
            markline_opts = markline_opts.opts

        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": CHART_TYPE.KLINE,
                "name": name,
                "data": y_axis,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
            }
        )
        return self
