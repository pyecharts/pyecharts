# coding=utf-8

from pyecharts.charts.chart import Chart
from ...commons.types import *
from ...options import *


class Pie(Chart):
    """
    <<< 饼图 >>>

    饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(self, name, data_pair, radius=None, center=None, rosetype=None, **kwargs):

        _data = []
        for (_name, _value) in data_pair:
            _data.append({"name": _name, "value": _value})

        _rmin, _rmax = "0%", "75%"
        if radius:
            if len(radius) == 2:
                _rmin, _rmax = ["{}%".format(r) for r in radius]

        _cmin, _cmax = "50%", "50%"
        if center:
            if len(center) == 2:
                _cmin, _cmax = ["{}%".format(c) for c in center]

        if rosetype:
            if rosetype not in ("radius", "area"):
                rosetype = "radius"

        for a in attr:
            self._option.get("legend")[0].get("data").append(a)

        _dlst = self._option.get("legend")[0].get("data")
        _dset = list(set(_dlst))
        _dset.sort(key=_dlst.index)
        self._option.get("legend")[0].update(data=list(_dset))

        self.options.get("series").append(
            {
                "type": "pie",
                "name": name,
                "data": _data,
                "radius": [_rmin, _rmax],
                "center": [_cmin, _cmax],
                "roseType": rosetype,
                "label": chart["label"],
                "seriesId": self._option.get("series_id"),
            }
        )
