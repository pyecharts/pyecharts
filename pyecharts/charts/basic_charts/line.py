# coding=utf-8

from ...charts.chart import Chart
from ...options import (
    AreaStyleOpts,
    AxisOpts,
    InitOpts,
    LabelOpts,
    LineStyleOpts,
    MarkLineOpts,
    MarkPointOpts,
)
from ...types import *


class Line(Chart):
    """
    <<< 折线/面积图 >>>

    折线图是用折线将各个数据点标志连接起来的图表，用于展现数据的变化趋势。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
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
        is_symbol_show: bool = True,
        symbol: Optional[str] = None,
        symbol_size: Numeric = 4,
        stack: Optional[str] = None,
        is_smooth: bool = False,
        is_step: bool = False,
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
        markpoint_opts: Union[MarkPointOpts, dict] = MarkPointOpts(),
        markline_opts: Union[MarkLineOpts, dict] = MarkLineOpts(),
        linestyle_opts: Union[LineStyleOpts, dict] = LineStyleOpts(),
        areastyle_opts: Union[AreaStyleOpts, dict] = AreaStyleOpts(),
    ):
        self._append_legend(name)
        # 合并 x 和 y 轴数据，避免当 X 轴的类型设置为 'value' 的时候，
        # X、Y 轴均显示 Y 轴数据
        data = [list(z) for z in zip(self.__xaxis_data, y_axis)]

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
                "data": data,
                "label": label_opts.opts,
                "lineStyle": linestyle_opts.opts,
                "areaStyle": areastyle_opts.opts,
                "markPoint": markpoint_opts.opts,
                "markLine": markline_opts.opts,
            }
        )
        return self
