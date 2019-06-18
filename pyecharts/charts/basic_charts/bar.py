from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Bar(RectChart):
    """
    <<< Bar Chart >>>

    Bar chart presents categorical data with rectangular bars
    with heights or lengths proportional to the values that they represent.
    """

    def add_yaxis(
        self,
        series_name: str,
        yaxis_data: types.Sequence[types.Union[types.Numeric, opts.BarItem, dict]],
        *,
        is_selected: bool = True,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        color: types.Optional[str] = None,
        stack: types.Optional[str] = None,
        category_gap: types.Union[types.Numeric, str] = "20%",
        gap: types.Optional[str] = None,
        label_opts: types.Label = opts.LabelOpts(),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.BAR,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": yaxis_data,
                "stack": stack,
                "barCategoryGap": category_gap,
                "barGap": gap,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
