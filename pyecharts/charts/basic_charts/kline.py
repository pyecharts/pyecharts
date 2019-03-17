# coding=utf-8

from ...charts.chart import Chart
from ...options import *


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


class Kline(Chart):
    """
    <<< K 线图 >>>

    红涨蓝跌
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis={})
        self.__xaxis_data = None

    def add(
        self,
        name,
        x_axis,
        y_axis,
        markline_opts: MarkLineOpts(),
        markpoint_opts: MarkPointOpts(),
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param x_axis:
            x 坐标轴数据。
        :param y_axis:
            y 坐标轴数据。数据中，每一行是一个『数据项』，每一列属于一个『维度』。
            数据项具体为 [open, close, lowest, highest] （即：[开盘值, 收盘值,
             最低值, 最高值]）。
        :param kwargs:
        """
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
