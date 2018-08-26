# coding=utf-8
from __future__ import unicode_literals

from pyecharts.charts.geo import Geo
from pyecharts.constants import SYMBOL


class GeoLines(Geo):
    """
    <<< 地理坐标系线图 >>>

    用于带有起点和终点信息的线数据的绘制，主要用于地图上的航线，路线的可视化。
    """

    def __init__(self, *args, **kwargs):
        super(GeoLines, self).__init__(*args, **kwargs)
        self._zlevel = 1

    def add(
        self,
        name,
        data,
        maptype="china",
        coordinate_region="中国",
        symbol=None,
        symbol_size=12,
        border_color="#111",
        geo_normal_color="#323c48",
        geo_emphasis_color="#2a333d",
        geo_cities_coords=None,
        geo_effect_period=6,
        geo_effect_traillength=0,
        geo_effect_color="#fff",
        geo_effect_symbol="circle",
        geo_effect_symbolsize=5,
        is_geo_effect_show=True,
        is_roam=True,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param data:
            数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。每一行包含两个或
            三个数据，如 ["广州", "北京"] 或 ["广州", "北京"，100]，则指定从广州到北京。第
            三个值用于表示该 line 的数值，该值可省略。
        :param maptype:
            地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，
            全球国家等地图，具体请参考 [地图自定义篇](zh-cn/customize_map)
        :param coordinate_region:
            城市坐标所属国家。从 v0.5.7 引入，针对国际城市的地理位置的查找。默认为 `中国`。
            具体的国家/地区映射表参照 datasets/countries_regions_db.json。更多地理坐标
            信息可以参考 [数据集篇](/zh-cn/datasets)
        :param symbol:
            线两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。
        :param symbol_size:
            线两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
        :param border_color:
            地图边界颜色。
        :param geo_normal_color:
            正常状态下地图区域的颜色。
        :param geo_emphasis_color:
            高亮状态下地图区域的颜色。
        :param geo_cities_coords:
            用户自定义地区经纬度，类似如 {'阿城': [126.58, 45.32],} 这样的字典，当用
            于提供了该参数时，将会覆盖原有预存的区域坐标信息。
        :param geo_effect_period:
            特效动画的时间，单位为 s。
        :param geo_effect_traillength:
            特效尾迹的长度。取从 0 到 1 的值，数值越大尾迹越长。
        :param geo_effect_color:
            特效标记的颜色。
        :param geo_effect_symbol:
            特效图形的标记。有 'circle', 'rect', 'roundRect', 'triangle', 'diamond',
            'pin', 'arrow', 'plane' 可选。
        :param geo_effect_symbolsize:
            特效标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示高和宽，
            例如 [20, 10] 表示标记宽为20，高为 10。
        :param is_geo_effect_show:
            是否显示特效。
        :param is_roam:
            是否开启鼠标缩放和平移漫游。默认为 True。
            如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启。
        :param kwargs:
        """

        chart = self._get_all_options(**kwargs)
        self._zlevel += 1
        if geo_cities_coords:
            for city_name, city_coord in geo_cities_coords.items():
                self.add_coordinate(city_name, city_coord[0], city_coord[1])

        if geo_effect_symbol == "plane":
            geo_effect_symbol = SYMBOL["plane"]

        _data_lines, _data_scatter = [], []
        for element in data:
            assert len(element) >= 2
            _line_value = None

            if len(element) == 2:
                _from_name, _to_name = element
            else:
                _from_name, _to_name, _line_value = element

            _from_coordinate = self.get_coordinate(
                _from_name, coordinate_region, raise_exception=True
            )
            _to_coordinate = self.get_coordinate(
                _to_name, raise_exception=True
            )
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
                {
                    "name": _to_name,
                    "value": [_to_coordinate[0], _to_coordinate[1], 0],
                }
            )

        self._option.update(
            geo={
                "map": maptype,
                "roam": is_roam,
                "label": {
                    "emphasis": {"show": True, "textStyle": {"color": "#eee"}}
                },
                "itemStyle": {
                    "normal": {
                        "areaColor": geo_normal_color,
                        "borderColor": border_color,
                    },
                    "emphasis": {"areaColor": geo_emphasis_color},
                },
            }
        )
        self._option.get("legend")[0].get("data").append(name)
        self._option.get("series").append(
            {
                "type": "lines",
                "name": name,
                "zlevel": self._zlevel,
                "effect": {
                    "show": is_geo_effect_show,
                    "period": geo_effect_period,
                    "trailLength": geo_effect_traillength,
                    "color": geo_effect_color,
                    "symbol": geo_effect_symbol,
                    "symbolSize": geo_effect_symbolsize,
                },
                "symbol": symbol or ["none", "arrow"],
                "symbolSize": symbol_size,
                "data": _data_lines,
                "lineStyle": chart["line_style"],
            }
        )
        self._option.get("series").append(
            {
                "type": "scatter",
                "name": name,
                "zlevel": self._zlevel,
                "coordinateSystem": "geo",
                "symbolSize": 10,
                "data": _data_scatter,
                "label": chart["label"],
                "tooltip": {"formatter": "{b}"},
            }
        )

        self._add_chinese_map(maptype)
        self._config_components(**kwargs)
        return self
