#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Map(Base):
    """
    <<< 地图 >>>
    地图主要用于地理区域数据的可视化。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Map, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value,
              is_roam=True,
              maptype='china',
              **kwargs):
        """

        :param name:
            图例名称
        :param attr:
            属性名称
        :param value:
            属性所对应的值
        :param is_roam:
            是否开启鼠标缩放和平移漫游。默认不开启
            如果只想要开启缩放或者平移，可以设置成 scale 或者 move。设置成 true 为都开启
        :param maptype:
            地图类型，支持 china, world, 广东，福建，山东等...
        :param kwargs:
        """
        if isinstance(attr, list) and isinstance(value, list):
            chart = get_all_options(**kwargs)
            assert len(attr) == len(value)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                _data.append({"name": _name, "value": _value})
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "type": "map",
                "name": name,
                "symbol": chart['symbol'],
                "mapType": maptype,
                "data": _data,
                "roam": is_roam
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("attr and value must be list")
