# coding=utf-8
import sys

from pyecharts.chart import Chart
from pyecharts.option import get_all_options


PY2 = sys.version_info[0] == 2


class Map(Chart):
    """
    <<< 地图 >>>

    地图主要用于地理区域数据的可视化。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Map, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value,
              maptype="china",
              is_roam=True,
              is_map_symbol_show=True,
              name_map=None,
              **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param maptype:
            地图类型。 支持 china、world、安徽、澳门、北京、重庆、福建、福建、甘肃、广东，
            广西、广州、海南、河北、黑龙江、河南、湖北、湖南、江苏、江西、吉林、辽宁、
            内蒙古、宁夏、青海、山东、上海、陕西、山西、四川、台湾、天津、香港、新疆、
            西藏、云南、浙江，以及 [363个二线城市地图](https://github.com/chfw/echarts-
            china-cities-js#featuring-citiesor-for-single-download)。
            提醒：
                在画市级地图的时候，城市名字后面的‘市’要省去了，比如，石家庄市的‘市’不要提，
                即‘石家庄’就可以了。地图提供了自定义模式 [用户如何自定义地图](https://github.com/
                chenjiandongx/pyecharts/blob/master/docs/zh-cn/user-customize-map.md)
        :param is_roam:
            是否开启鼠标缩放和平移漫游。默认为 True
            如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启。
        :param is_map_symbol_show:
            是否显示地图标记红点，默认为 True。
        :param name_map:
            用自定义的地图名称。默认为 None，也就是用地图自带地名。
        :param kwargs:
        """
        assert len(attr) == len(value)
        chart = get_all_options(**kwargs)
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append({"name": _name, "value": _value})
        self._option.get('legend')[0].get('data').append(name)

        __option__ = {
            "type": "map",
            "name": name,
            "symbol": chart['symbol'],
            "label": chart['label'],
            "mapType": maptype,
            "data": _data,
            "roam": is_roam,
            "showLegendSymbol": is_map_symbol_show
        }
        if name_map:
            __option__['nameMap'] = name_map
        self._option.get('series').append(__option__)
        self._add_chinese_map(maptype)
        self._config_components(**kwargs)
