from ... import options as opts
from ...charts.chart import RectChart
from ...commons.types import Numeric, Optional, Sequence, Union
from ...globals import ChartType


class Scatter(RectChart):
    """
    <<< Scatter >>>

    The scatter diagram on the rectangular coordinate system can be used to
    show the relationship between x and y of the data. If the data item has
    multiple dimensions, it can be represented by color, and the
    visualmap component can be used.
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
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence] = 10,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(position="right"),
        markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,
        markline_opts: Union[opts.MarkLineOpts, dict, None] = None,
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)
        data = [list(z) for z in zip(self._xaxis_data, y_axis)]
        self.options.get("series").append(
            {
                "type": ChartType.SCATTER,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "data": data,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
