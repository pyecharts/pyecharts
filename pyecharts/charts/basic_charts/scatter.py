import itertools

from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Scatter(RectChart):
    """
    <<< Scatter >>>

    The scatter diagram on the rectangular coordinate system can be used to
    show the relationship between x and y of the data. If the data item has
    multiple dimensions, it can be represented by color, and the
    visualmap component can be used.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Sequence,
        *,
        is_selected: bool = True,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        color: types.Optional[str] = None,
        symbol: types.Optional[str] = None,
        symbol_size: types.Union[types.Numeric, types.Sequence] = 10,
        label_opts: types.Label = opts.LabelOpts(position="right"),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_color(color)
        self._append_legend(series_name, is_selected)
        if len(y_axis) > 0 and isinstance(y_axis[0], types.Sequence):
            data = [
                list(itertools.chain(list([x]), y))
                for x, y in zip(self._xaxis_data, y_axis)
            ]
        else:
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
