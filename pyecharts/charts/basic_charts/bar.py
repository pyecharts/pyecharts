# coding=utf-8

from ...charts.chart import Chart
from ...types import *
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
        self.options.update(yAxis=AxisOpts().opts)
        self.__xaxis_data = None

    def add_xaxis(self, xaxis_data: ListTuple):
        self.options.update(xAxis=AxisOpts().opts)
        self.options["xAxis"].update(data=xaxis_data)
        self.__xaxis_data = xaxis_data
        return self

    def add_yaxis(
        self,
        series_name: str,
        yaxis_data: ListTuple,
        bar_opts: Union[BarOpts, dict] = BarOpts(),
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

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": "bar",
                "name": series_name,
                "data": yaxis_data,
                "stack": bar_opts.stack,
                "barCategoryGap": bar_opts.category_gap,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
            }
        )
        return self
