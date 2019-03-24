# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import ListTuple, Numeric, Union, Optional
from ...consts import ChartType


class Funnel(Chart):
    """
    <<< 漏斗图 >>>
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        data_pair: ListTuple,
        color: Optional[str] = None,
        sort_: str = "descending",
        gap: Numeric = 0,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts

        self._append_color(color)
        data = [{"name": n, "value": v} for n, v in data_pair]
        for (a, _) in data_pair:
            self._append_legend(a)

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
            }
        )
        return self
