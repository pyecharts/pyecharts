# coding=utf-8

from ...charts.chart import Chart
from ...options import AxisOpts, InitOpts, LabelOpts, MarkLineOpts, MarkPointOpts
from ...types import *


class Scatter(Chart):
    """
    <<< 散点图 >>>

    直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，
    可以用颜色来表现，利用 geo 组件。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=AxisOpts().opts)
        self.__xaxis_data = None

    def add_xaxis(self, xaxis_data: Any):
        self.options.update(xAxis=AxisOpts().opts)
        self.options["xAxis"].update(data=xaxis_data)
        self.__xaxis_data = xaxis_data
        return self

    def add_yaxis(
        self,
        name: str,
        y_axis: ListTuple,
        symbol=None,
        symbol_size: Numeric = 10,
        label_opts: Union[LabelOpts, dict] = LabelOpts(position="right"),
        markpoint_opts: Union[MarkPointOpts, dict] = MarkPointOpts(),
        markline_opts: Union[MarkLineOpts, dict] = MarkLineOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(markline_opts, MarkLineOpts):
            markline_opts = markline_opts.opts
        if isinstance(markpoint_opts, MarkPointOpts):
            markpoint_opts = markpoint_opts.opts

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
