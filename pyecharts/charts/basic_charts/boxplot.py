from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Boxplot(RectChart):
    """
    <<< Boxplot >>>

    A box-plot is a statistical chart used to show a set of data dispersion data.
    It displays the maximum, minimum, median, lower quartile, and upper quartile
    of a set of data.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Sequence[types.Union[opts.BoxplotItem, dict]],
        *,
        is_selected: bool = True,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(),
        markpoint_opts: types.MarkPoint = opts.MarkPointOpts(),
        markline_opts: types.MarkLine = opts.MarkLineOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.BOXPLOT,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "data": y_axis,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self

    @staticmethod
    def prepare_data(items):
        data = []
        for item in items:
            try:
                d, res = sorted(item), []
                for i in range(1, 4):
                    n = i * (len(d) + 1) / 4
                    k = int(n)
                    m = n - k
                    if m == 0:
                        res.append(d[k - 1])
                    elif m == 1 / 4:
                        res.append(d[k - 1] * 0.75 + d[k] * 0.25)
                    elif m == 1 / 2:
                        res.append(d[k - 1] * 0.50 + d[k] * 0.50)
                    elif m == 3 / 4:
                        res.append(d[k - 1] * 0.25 + d[k] * 0.75)
                data.append([d[0]] + res + [d[-1]])
            except Exception:
                pass
        return data
