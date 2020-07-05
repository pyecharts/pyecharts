from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Pie(Chart):
    """
    <<< Pie >>>

    The pie chart is mainly used to represent the proportion of data of
    different categories in the total. Each radian represents the ratio of
    the number of data points.
    """

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence[types.Union[types.Sequence, opts.PieItem, dict]],
        *,
        color: types.Optional[str] = None,
        radius: types.Optional[types.Sequence] = None,
        center: types.Optional[types.Sequence] = None,
        rosetype: types.Optional[str] = None,
        is_clockwise: bool = True,
        label_opts: types.Label = opts.LabelOpts(),
        label_line_opts: types.PieLabelLine = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        if self.options.get("dataset") is not None:
            data = None
            self.options.get("legend")[0].update(
                data=[d[0] for d in self.options.get("dataset").get("source")][1:]
            )
        elif isinstance(data_pair[0], opts.PieItem):
            data = data_pair
        else:
            data = [{"name": n, "value": v} for n, v in data_pair]

            for a, _ in data_pair:
                self.options.get("legend")[0].get("data").append(a)

            _dlst = self.options.get("legend")[0].get("data")
            _dset = list(set(_dlst))
            _dset.sort(key=_dlst.index)
            self.options.get("legend")[0].update(data=list(_dset))

        if not radius:
            radius = ["0%", "75%"]
        if not center:
            center = ["50%", "50%"]

        self._append_color(color)
        self.options.get("series").append(
            {
                "type": ChartType.PIE,
                "name": series_name,
                "clockwise": is_clockwise,
                "data": data,
                "radius": radius,
                "center": center,
                "roseType": rosetype,
                "label": label_opts,
                "labelLine": label_line_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
