# coding=utf-8

from pyecharts.charts.chart import Chart
from pyecharts.options import *


class Map(Chart):
    """
    <<< 地图 >>>

    地图主要用于地理区域数据的可视化。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name,
        data_pair=None,
        maptype="china",
        is_roam=True,
        symbol=None,
        is_map_symbol_show=True,
        name_map=None,
        label_opts: LabelOpts = LabelOpts(),
    ):
        _data = []
        for (_name, _value) in data_pair:
            _data.append({"name": _name, "value": _value})
        self.options.get("legend")[0].get("data").append(name)

        __option__ = {
            "type": "map",
            "name": name,
            "symbol": symbol,
            "label": label_opts.opts,
            "mapType": maptype,
            "data": _data,
            "roam": is_roam,
            "showLegendSymbol": is_map_symbol_show,
        }
        if name_map:
            __option__["nameMap"] = name_map
        self.options.get("series").append(__option__)
