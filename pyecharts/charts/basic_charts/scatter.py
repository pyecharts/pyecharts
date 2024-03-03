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

    def _parse_data(
        self, y_axis: types.Sequence[types.Union[opts.ScatterItem, dict]]
    ) -> types.Optional[types.Sequence]:
        if self.options.get("dataset") is not None:
            return None
        elif len(self._xaxis_data) == 0:
            return y_axis
        elif isinstance(y_axis[0], (opts.ScatterItem, dict)):
            return y_axis
        elif isinstance(y_axis[0], types.Sequence):
            return [
                list(itertools.chain(list([x]), y))
                for x, y in zip(self._xaxis_data, y_axis)
            ]
        else:
            return [list(z) for z in zip(self._xaxis_data, y_axis)]

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Sequence[types.Union[opts.ScatterItem, dict]],
        *,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        color: types.Optional[str] = None,
        symbol: types.Optional[str] = None,
        symbol_size: types.Union[types.Numeric, types.Sequence] = 10,
        symbol_rotate: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(position="right"),
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        markarea_opts: types.MarkArea = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        self._append_color(color)
        self._append_legend(series_name)

        data = self._parse_data(y_axis=y_axis)

        self.options.get("series").append(
            {
                "type": ChartType.SCATTER,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "symbolRotate": symbol_rotate,
                "data": data,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "encode": encode,
            }
        )
        return self
