from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class HeatMap(RectChart):
    """
    <<< HeatMap >>>

    The heat map is mainly used to represent the size of the value by color,
    which must be used in conjunction with the visualMap component.
    Two categories of axes must be used in rectangular coordinates.
    """

    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.set_global_opts(visualmap_opts=opts.VisualMapOpts(orient="horizontal"))

    def add_yaxis(
        self,
        series_name: str,
        yaxis_data: types.Sequence,
        value: types.Sequence,
        *,
        is_selected: bool = True,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_legend(series_name, is_selected)
        self.options.get("yAxis")[0].update(data=yaxis_data)
        self.options.get("series").append(
            {
                "type": ChartType.HEATMAP,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": value,
                "label": label_opts,
                "markLine": markline_opts,
                "markPoint": markpoint_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
