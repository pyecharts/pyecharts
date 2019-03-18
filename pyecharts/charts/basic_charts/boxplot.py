# coding=utf-8

from ...charts.chart import Chart
from ...options import AxisOpts, InitOpts, LabelOpts, MarkLineOpts, MarkPointOpts
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
        markpoint_opts: MarkPointOpts = MarkPointOpts(),
        markline_opts: MarkLineOpts = MarkLineOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(markpoint_opts, MarkPointOpts):
            markpoint_opts = markpoint_opts.opts
        if isinstance(markline_opts, MarkLineOpts):
            markline_opts = markline_opts.opts

        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "boxplot",
                "name": name,
                "data": y_axis,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
            }
        )
