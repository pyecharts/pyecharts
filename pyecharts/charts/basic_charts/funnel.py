# coding=utf-8

from ...charts.chart import Chart
from ...options import InitOpts, LabelOpts
from ...types import ListTuple, Numeric, Union


class Funnel(Chart):
    """
    <<< 漏斗图 >>>
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        data_pair: ListTuple,
        sort_: str = "descending",
        gap: Numeric = 0,
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        data = [{"name": n, "value": v} for (n, v) in data_pair]
        for (a, _) in data_pair:
            self._append_legend(a)

        _dset = set(self.options.get("legend")[0].get("data"))
        self.options.get("legend")[0].update(data=list(_dset))

        self.options.get("series").append(
            {
                "type": "funnel",
                "name": name,
                "data": data,
                "sort": sort_,
                "gap": gap,
                "label": label_opts,
            }
        )
        return self
