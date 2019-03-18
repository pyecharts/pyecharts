# coding=utf-8

from ...charts import Geo
from ...options import EffectOpts, InitOpts, LabelOpts, LineStyleOpts
from ...types import *


class GeoLines(Geo):
    """
    <<< 地理坐标系线图 >>>

    用于带有起点和终点信息的线数据的绘制，主要用于地图上的航线，路线的可视化。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)
        self._zlevel = 1

    def add(
        self,
        name: str,
        data,
        maptype="china",
        coordinate_region="中国",
        symbol=None,
        symbol_size=12,
        border_color="#111",
        normal_color="#323c48",
        emphasis_color="#2a333d",
        region_coords=None,
        effect_opts: Union[EffectOpts, dict] = EffectOpts(),
        linestyle_opts: Union[LineStyleOpts, dict] = LineStyleOpts(),
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
        is_roam=True,
    ):

        if isinstance(effect_opts, EffectOpts):
            effect_opts = effect_opts.opts
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        self._zlevel += 1
        if region_coords:
            for city_name, city_coord in region_coords.items():
                self.add_coordinate(city_name, city_coord[0], city_coord[1])

        if effect_symbol == "plane":
            geo_effect_symbol = SYMBOL["plane"]

        _data_lines, _data_scatter = [], []
        for element in data:
            assert len(element) >= 2
            _line_value = None

            if len(element) == 2:
                _from_name, _to_name = element
            else:
                _from_name, _to_name, _line_value = element

            _from_coordinate = self.get_coordinate(_from_name)
            _to_coordinate = self.get_coordinate(_to_name)
            _data_lines.append(
                {
                    "fromName": _from_name,
                    "toName": _to_name,
                    "value": _line_value,
                    "coords": [_from_coordinate, _to_coordinate],
                }
            )
            _data_scatter.append(
                {
                    "name": _from_name,
                    "value": [_from_coordinate[0], _from_coordinate[1], 0],
                }
            )
            _data_scatter.append(
                {"name": _to_name, "value": [_to_coordinate[0], _to_coordinate[1], 0]}
            )

        self.options.update(
            geo={
                "map": maptype,
                "roam": is_roam,
                "label": {"emphasis": {"show": True, "textStyle": {"color": "#eee"}}},
                "itemStyle": {
                    "normal": {"areaColor": normal_color, "borderColor": border_color},
                    "emphasis": {"areaColor": emphasis_color},
                },
            }
        )
        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "lines",
                "name": name,
                "zlevel": self._zlevel,
                "effect": effect_opts,
                "symbol": symbol or ["none", "arrow"],
                "symbolSize": symbol_size,
                "data": _data_lines,
                "lineStyle": linestyle_opts,
            }
        )
        self.options.get("series").append(
            {
                "type": "scatter",
                "name": name,
                "zlevel": self._zlevel,
                "coordinateSystem": "geo",
                "symbolSize": 10,
                "data": _data_scatter,
                "label": label_opts,
                "tooltip": {"formatter": "{b}"},
            }
        )
        return self
