# coding=utf-8

from ...charts.chart import Chart
from ...options import *
from ...types import *


class Boxplot(Chart):
    """
    <<< 箱形图 >>>

    箱形图是一种用作显示一组数据分散情况资料的统计图。它能显示出一组数据
    的最大值、最小值、中位数、下四分位数及上四分位数。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=AxisOpts().opts)
        self.__xaxis_data = None

    def add_xaxis(self, xaxis_data: ListTuple):
        self.options.update(xAxis=AxisOpts().opts)
        self.options["xAxis"].update(data=xaxis_data)
        self.__xaxis_data = xaxis_data
        return self

    def add_yaxis(
        self,
        name: str,
        y_axis: ListTuple,
        label_opts: LabelOpts = LabelOpts(),
        markpoint_opts: MarkPointOpts = MarkPointData(),
        markline_opts: MarkLineOpts = MarkLineOpts(),
    ):
        self.options.get("legend")[0].get("data").append(name)
        self.options.get("series").append(
            {
                "type": "boxplot",
                "name": name,
                "data": y_axis,
                "label": label_opts.opts,
                "markPoint": markpoint_opts.opts,
                "markLine": markline_opts.opts,
            }
        )
