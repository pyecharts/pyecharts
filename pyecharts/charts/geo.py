# coding=utf-8

import copy

from pyecharts.chart import Chart
from pyecharts.option import get_all_options
from pyecharts.constants import CITY_GEO_COORDS


class Geo(Chart):
    """
    <<< 地理坐标系 >>>

    地理坐标系组件用于地图的绘制，支持在地理坐标系上绘制散点图，线集。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Geo, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value,
              type="scatter",
              maptype='china',
              symbol_size=12,
              border_color="#111",
              geo_normal_color="#323c48",
              geo_emphasis_color="#2a333d",
              geo_cities_coords=None,
              is_roam=True,
              **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param type:
            图例类型，有'scatter', 'effectscatter', 'heatmap'可选。
        :param maptype:
            地图类型。 支持 china、world、安徽、澳门、北京、重庆、福建、福建、甘肃、
            广东，广西、广州、海南、河北、黑龙江、河南、湖北、湖南、江苏、江西、吉林、
            辽宁、内蒙古、宁夏、青海、山东、上海、陕西、山西、四川、台湾、天津、香港、
            新疆、西藏、云南、浙江，以及 [363个二线城市](https://github.com/chfw/
            echarts-china-cities-js#featuring-citiesor-for-single-download]地图。
            提醒：
                在画市级地图的时候，城市名字后面的‘市’要省去了，比如，石家庄市的
                ‘市’不要提，即‘石家庄’就可以了。
        :param symbol_size:
            标记图形大小。
        :param border_color:
            地图边界颜色。
        :param geo_normal_color:
            正常状态下地图区域的颜色。
        :param geo_emphasis_color:
            高亮状态下地图区域的颜色。
        :param geo_cities_coords:
            用户自定义地区经纬度，类似如 {'阿城': [126.58, 45.32],} 这样的字典，当用
            于提供了该参数时，将会覆盖原有预存的区域坐标信息。
        :param is_roam:
            是否开启鼠标缩放和平移漫游。默认为 True。
            如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启。
        :param kwargs:
        """
        assert len(attr) == len(value)
        kwargs.update(type="geo")
        chart = get_all_options(**kwargs)

        if geo_cities_coords:
            _geo_cities_coords = copy.deepcopy(geo_cities_coords)
        else:
            _geo_cities_coords = copy.deepcopy(CITY_GEO_COORDS)

        _data = []
        for _name, _value in zip(attr, value):
            if _name in _geo_cities_coords:
                city_coordinate = _geo_cities_coords.get(_name)
                city_coordinate.append(_value)
                _data.append({"name": _name, "value": city_coordinate})
            else:
                print("%s coordinates is not found" % _name)
        self._option.update(
            geo={
                "map": maptype,
                "roam": is_roam,
                "label": {
                    "emphasis": {
                        "show": True,
                        "textStyle": {
                            "color": "#eee"
                        }
                    }},
                "itemStyle": {
                    "normal": {
                        "areaColor": geo_normal_color,
                        "borderColor": border_color
                    },
                    "emphasis": {
                        "areaColor": geo_emphasis_color
                    }}
            })
        self._option.get('legend')[0].get('data').append(name)

        if type == "scatter":
            self._option.get('series').append({
                "type": type,
                "name": name,
                "coordinateSystem": 'geo',
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": _data,
                "label": chart['label'],
            })

        elif type == "effectScatter":
            self._option.get('series').append({
                "type": type,
                "name": name,
                "coordinateSystem": 'geo',
                "showEffectOn": "render",
                "rippleEffect": chart['effect'],
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": _data,
                "label": chart['label'],
            })

        elif type == "heatmap":
            self._option.get('series').append({
                "type": type,
                "name": name,
                "coordinateSystem": 'geo',
                "data": _data,
            })

        self._add_chinese_map(maptype)
        self._config_components(**kwargs)
