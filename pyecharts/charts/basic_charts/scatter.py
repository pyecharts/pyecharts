# coding=utf-8

from ...types import *
from ...charts.chart import Chart
from ...options import *


class Scatter(Chart):
    """
    <<< 散点图 >>>

    直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，
    可以用颜色来表现，利用 geo 组件。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis={})
        self.__xaxis_data = None

    def add_xaxis(self, xaxis_data: Any):
        self.options.update(xAxis={"data": xaxis_data})
        self.__xaxis_data = xaxis_data
        return self

    def add_yaxis(
        self,
        name: str,
        y_axis: ListTuple,
        symbol=None,
        symbol_size: Numeric = 10,
        label_opts: LabelOpts = LabelOpts(),
        markpoint_opts: MarkPointOpts = MarkPointOpts(),
        markline_opts: MarkLineOpts = MarkLineOpts(),
    ):

        # show split line, because by default split line is hidden for xaxis
        # xaxis[0]["splitLine"]["show"] = True
        # self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._append_legend(name)
        data = [list(z) for z in zip(self.__xaxis_data, y_axis)]
        self.options.get("series").append(
            {
                "type": "scatter",
                "name": name,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "data": data,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
            }
        )
