# coding=utf-8

from ...charts.chart import Chart
from ...options import InitOpts, LabelOpts
from ...types import *


class Pie(Chart):
    """
    <<< 饼图 >>>

    饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        data_pair: ListTuple,
        radius: Optional[ListTuple] = None,
        center: Optional[ListTuple] = None,
        rosetype: str = "radius",
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        data = [{"name": n, "value": v} for (n, v) in data_pair]

        if not radius:
            radius = ["0%", "75%"]
        if not center:
            center = ["50%", "50%"]

        for (a, _) in data_pair:
            self.options.get("legend")[0].get("data").append(a)

        _dlst = self.options.get("legend")[0].get("data")
        _dset = list(set(_dlst))
        _dset.sort(key=_dlst.index)
        self.options.get("legend")[0].update(data=list(_dset))

        self.options.get("series").append(
            {
                "type": "pie",
                "name": name,
                "data": data,
                "radius": radius,
                "center": center,
                "roseType": rosetype,
                "label": label_opts,
            }
        )
