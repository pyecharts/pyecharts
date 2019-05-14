from ... import options as opts
from ...charts.chart import RectChart
from ...commons.types import Numeric, Optional, Sequence, Union
from ...globals import ChartType


class Line(RectChart):
    """
    <<< Line Chart >>>

    Line chart is a graph that connects all data points
    with single line to show the change trend of data.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[opts.AxisOpts().opts])

    def add_yaxis(
        self,
        series_name: str,
        y_axis: Sequence,
        *,
        is_selected: bool = True,
        xaxis_index: Optional[Numeric] = None,
        yaxis_index: Optional[Numeric] = None,
        color: Optional[str] = None,
        is_symbol_show: bool = True,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence] = 4,
        stack: Optional[str] = None,
        is_smooth: bool = False,
        is_step: bool = False,
        markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,
        markline_opts: Union[opts.MarkLineOpts, dict, None] = None,
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        linestyle_opts: Union[opts.LineStyleOpts, dict] = opts.LineStyleOpts(),
        areastyle_opts: Union[opts.AreaStyleOpts, dict] = opts.AreaStyleOpts(),
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)
        # 合并 x 和 y 轴数据，避免当 X 轴的类型设置为 'value' 的时候，
        # X、Y 轴均显示 Y 轴数据
        data = [list(z) for z in zip(self._xaxis_data, y_axis)]

        self.options.get("series").append(
            {
                "type": ChartType.LINE,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "showSymbol": is_symbol_show,
                "smooth": is_smooth,
                "step": is_step,
                "stack": stack,
                "data": data,
                "label": label_opts,
                "lineStyle": linestyle_opts,
                "areaStyle": areastyle_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
