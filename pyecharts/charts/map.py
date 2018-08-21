# coding=utf-8
from pyecharts.chart import Chart


class Map(Chart):
    """
    <<< 地图 >>>

    地图主要用于地理区域数据的可视化。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Map, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        attr,
        value,
        maptype="china",
        is_roam=True,
        is_map_symbol_show=True,
        name_map=None,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param maptype:
            地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，
            全球国家等地图，具体请参考 [地图自定义篇](zh-cn/customize_map)
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
        chart = self._get_all_options(**kwargs)
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append({"name": _name, "value": _value})
        self._option.get("legend")[0].get("data").append(name)

        __option__ = {
            "type": "map",
            "name": name,
            "symbol": chart["symbol"],
            "label": chart["label"],
            "mapType": maptype,
            "data": _data,
            "roam": is_roam,
            "showLegendSymbol": is_map_symbol_show,
        }
        if name_map:
            __option__["nameMap"] = name_map
        self._option.get("series").append(__option__)
        self._add_chinese_map(maptype)
        self._config_components(**kwargs)
