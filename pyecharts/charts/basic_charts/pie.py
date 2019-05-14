from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Optional, Sequence, Union
from ...globals import ChartType


class Pie(Chart):
    """
    <<< Pie >>>

    The pie chart is mainly used to represent the proportion of data of
    different categories in the total. Each radian represents the ratio of
    the number of data points.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        data_pair: Sequence,
        *,
        color: Optional[str] = None,
        radius: Optional[Sequence] = None,
        center: Optional[Sequence] = None,
        rosetype: Optional[str] = None,
        is_clockwise: bool = True,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        data = [{"name": n, "value": v} for n, v in data_pair]

        if not radius:
            radius = ["0%", "75%"]
        if not center:
            center = ["50%", "50%"]

        self._append_color(color)
        for a, _ in data_pair:
            self.options.get("legend")[0].get("data").append(a)

        _dlst = self.options.get("legend")[0].get("data")
        _dset = list(set(_dlst))
        _dset.sort(key=_dlst.index)
        self.options.get("legend")[0].update(data=list(_dset))

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
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
