from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Funnel(Chart):
    """
    <<< Funnel >>>

    Funnel diagram is suitable for one-way analysis of single process
    with standardized business process, long cycle and multiple links.
    Through comparison of business data of each link in the funnel,
    the link where the potential problems can be found intuitively,
    and then decisions can be made.
    """

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence,
        *,
        is_selected: bool = True,
        color: types.Optional[str] = None,
        sort_: str = "descending",
        gap: types.Numeric = 0,
        label_opts: types.Label = opts.LabelOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_color(color)
        if all([isinstance(d, opts.FunnelItem) for d in data_pair]):
            data = data_pair
            for a in data_pair:
                self._append_legend(a.opts.get("name"), is_selected)
        else:
            data = [{"name": n, "value": v} for n, v in data_pair]
            for a, _ in data_pair:
                self._append_legend(a, is_selected)

        _dset = set(self.options.get("legend")[0].get("data"))
        self.options.get("legend")[0].update(data=list(_dset))

        self.options.get("series").append(
            {
                "type": ChartType.FUNNEL,
                "name": series_name,
                "data": data,
                "sort": sort_,
                "gap": gap,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
