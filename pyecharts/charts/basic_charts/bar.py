# coding=utf-8

from ...commons.types import *
from ...charts.chart import Chart
from ...options import *


class BarOpts:
    def __init__(self, stack: Optional[str] = None, category_gap=None):
        self.stack = stack
        self.category_gap = category_gap


class Bar(Chart):
    """
    <<< 柱状图/条形图 >>>

    柱状/条形图，通过柱形的高度/条形的宽度来表现数据的大小。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis={})
        self.__xaxis_data = None

    def add_xaxis(self, xaxis_data: ListTuple):
        self.options.update(xAxis={"data": xaxis_data})
        self.__xaxis_data = xaxis_data
        return self

    def add_yaxis(
        self,
        series_name: str,
        yaxis_data: ListTuple,
        bar_opts: BarOpts = BarOpts(),
        label_opts: LabelOpts = LabelOpts(),
        markpoint_opts: MarkPointOpts = MarkPointOpts(),
        markline_opts: MarkLineOpts = MarkLineOpts(),
    ):
        self.options.get("legend")[0].get("data").append(series_name)
        self.options.get("series").append(
            {
                "type": "bar",
                "name": series_name,
                "data": yaxis_data,
                "stack": bar_opts.stack,
                "barCategoryGap": bar_opts.category_gap,
                "label": label_opts.opts,
                "markPoint": markpoint_opts.opts,
                "markLine": markline_opts.opts,
            }
        )
        return self
