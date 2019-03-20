# coding=utf-8

from ...charts.chart import AxisChart

# from ...options import AxisOpts, InitOpts, MarkLineOpts, MarkPointOpts, TooltipOpts
from ...options import *
from ...commons.types import ListTuple, Union
from ...commons.consts import CHART_TYPE
from ...consts import TOOLTIP_FORMATTER_TYPE


# def kline_tooltip_formatter(params):
#     text = (
#         params[0].seriesName
#         + "<br/>"
#         + "- open:"
#         + params[0].data[1]
#         + "<br/>"
#         + "- close:"
#         + params[0].data[2]
#         + "<br/>"
#         + "- lowest:"
#         + params[0].data[3]
#         + "<br/>"
#         + "- highest:"
#         + params[0].data[4]
#     )
#     return text


class Kline(AxisChart):
    """
    <<< K 线图 >>>

    红涨蓝跌
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[AxisOpts().opts])
        self.set_global_opts(
            xaxis_opt=AxisOpts(is_scale=True), yaxis_opt=AxisOpts(is_scale=True)
        )

    def add_yaxis(
        self,
        name: str,
        y_axis: ListTuple,
        *,
        markline_opts: Union[MarkLineOpts, dict, None] = None,
        markpoint_opts: Union[MarkPointOpts, dict, None] = None,
    ):

        if isinstance(markpoint_opts, MarkPointOpts):
            markpoint_opts = markpoint_opts.opts
        if isinstance(markline_opts, MarkLineOpts):
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
