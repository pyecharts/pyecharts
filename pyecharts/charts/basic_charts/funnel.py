# coding=utf-8

from pyecharts.charts.chart import Chart
from ...options import *
from ...commons.types import *


class Funnel(Chart):
    """
    <<< 漏斗图 >>>
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name,
        attr,
        value,
        sort_: str = "descending",
        gap: Numeric = 0,
        label_opts: LabelOpts = LabelOpts(),
    ):
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append({"name": _name, "value": _value})
        for element in attr:
            self.options.get("legend")[0].get("data").append(element)
        _dset = set(self.options.get("legend")[0].get("data"))
        self.options.get("legend")[0].update(data=list(_dset))

        self.options.get("series").append(
            {
                "type": "funnel",
                "name": name,
                "data": _data,
                "sort": sort_,
                "gap": gap,
                "label": label_opts.opts,
            }
        )
