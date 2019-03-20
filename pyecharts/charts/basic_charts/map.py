# coding=utf-8

from ...charts.chart import Chart
from ...options import InitOpts, LabelOpts
from ...types import ListTuple, Union


class Map(Chart):
    """
    <<< 地图 >>>

    地图主要用于地理区域数据的可视化。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        data_pair: ListTuple,
        maptype: str = "china",
        *,
        is_roam: bool = True,
        symbol: str = None,
        is_map_symbol_show: bool = True,
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        self.js_dependencies.add(maptype)
        data = [{"name": n, "value": v} for (n, v) in data_pair]
        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "map",
                "name": name,
                "symbol": symbol,
                "label": label_opts,
                "mapType": maptype,
                "data": data,
                "roam": is_roam,
                "showLegendSymbol": is_map_symbol_show,
            }
        )
        return self
