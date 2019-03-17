# coding=utf-8

from ...charts.chart import Chart
from ...options import *
from ...types import *


class Map(Chart):
    """
    <<< 地图 >>>

    地图主要用于地理区域数据的可视化。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        data_pair: ListTuple,
        maptype: str = "china",
        is_roam: bool = True,
        symbol: str = None,
        is_map_symbol_show: bool = True,
        name_map=None,
        label_opts: LabelOpts = LabelOpts(),
    ):
        data = [{"name": n, "value": v} for (n, v) in data_pair]
        self._append_legend(name)

        __option__ = {
            "type": "map",
            "name": name,
            "symbol": symbol,
            "label": label_opts.opts,
            "mapType": maptype,
            "data": data,
            "roam": is_roam,
            "showLegendSymbol": is_map_symbol_show,
        }
        if name_map:
            __option__["nameMap"] = name_map
        self.options.get("series").append(__option__)
