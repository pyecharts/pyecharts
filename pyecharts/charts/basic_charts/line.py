# coding=utf-8

from ...charts.chart import Chart
from ...commons.types import *
from ...options import *


class Line(Chart):
    """
    <<< 折线/面积图 >>>

    折线图是用折线将各个数据点标志连接起来的图表，用于展现数据的变化趋势。
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
        name,
        y_axis,
        is_symbol_show=True,
        symbol: str = None,
        symbol_size=4,
        is_smooth=False,
        stack=None,
        is_step=False,
        label_opts: LabelOpts = LabelOpts(),
        markpoint_opts: MarkPointOpts = MarkPointOpts(),
        markline_opts: MarkLineOpts = MarkLineOpts(),
        linestyle_opts: LineStyleOpts = LineStyleOpts(),
        areastyle_opts: AreaStyleOpts = AreaStyleOpts(),
    ):
        self.options.get("legend")[0].get("data").append(name)
        # 合并 x 和 y 轴数据，避免当 X 轴的类型设置为 'value' 的时候，
        # X、Y 轴均显示 Y 轴数据
        _data = [list(z) for z in zip(self.__xaxis_data, y_axis)]

        self.options.get("series").append(
            {
                "type": "line",
                "name": name,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "smooth": is_smooth,
                "step": is_step,
                "stack": stack,
                "showSymbol": is_symbol_show,
                "data": _data,
                "label": label_opts.opts,
                "lineStyle": linestyle_opts.opts,
                "areaStyle": areastyle_opts.opts,
                "markPoint": markpoint_opts.opts,
                "markLine": markline_opts.opts,
            }
        )
        return self
