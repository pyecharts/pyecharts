# coding=utf-8

from ...charts.chart import AxisChart
from ...options import AxisOpts, InitOpts, MarkLineOpts, MarkPointOpts
from ...types import ListTuple


def kline_tooltip_formatter(params):
    text = (
        params[0].seriesName
        + "<br/>"
        + "- open:"
        + params[0].data[1]
        + "<br/>"
        + "- close:"
        + params[0].data[2]
        + "<br/>"
        + "- lowest:"
        + params[0].data[3]
        + "<br/>"
        + "- highest:"
        + params[0].data[4]
    )
    return text


class Kline(AxisChart):
    """
    <<< K 线图 >>>

    红涨蓝跌
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[AxisOpts().opts])

    def add_yaxis(
        self,
        name: str,
        y_axis: ListTuple,
        *,
        markline_opts: MarkLineOpts(),
        markpoint_opts: MarkPointOpts(),
    ):
        # kwargs.update(type="candlestick", x_axis=x_axis)
        # if "tooltip_formatter" not in kwargs:
        #     kwargs["tooltip_formatter"] = kline_tooltip_formatter
        # if "tooltip_trigger" not in kwargs:
        #     kwargs["tooltip_trigger"] = "axis"

        if isinstance(markpoint_opts, MarkPointOpts):
            markpoint_opts = markpoint_opts.opts
        if isinstance(markline_opts, MarkLineOpts):
            markline_opts = markline_opts.opts

        xaxis, yaxis = chart["xy_axis"]
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get("xAxis")[0]["scale"] = True
        self._option.get("yAxis")[0]["scale"] = True
        self._option.get("yAxis")[0]["splitArea"] = {"show": True}

        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "candlestick",
                "name": name,
                "data": y_axis,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
            }
        )
