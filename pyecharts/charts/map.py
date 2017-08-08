#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Map(Base):
    """
    <<< Map chart >>>
    Map is maily used in the visulization of geographic area data,
    which can be used with visualMap component to visualize the datas such as population distribution
    density in diffrent areas.
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
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param attr:
            name of attribute
        :param value:
            value of attribute
        :param is_roam:
            Whether to enable mouse zooming and translating. false by default.
            If either zooming or translating is wanted,
            it can be set to 'scale' or 'move'. Otherwise, set it to be true to enable both.
        :param maptype:
            type of map, it supports
            china、world、...
        :param kwargs:
        """
        chart = get_all_options(**kwargs)
        assert len(attr) == len(value)
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append({"name": _name, "value": _value})
        self._option.get('legend')[0].get('data').append(name)
        self._option.get('series').append({
            "type": "map",
            "name": name,
            "symbol": chart['symbol'],
            "mapType": maptype,
            "data": _data,
            "roam": is_roam
        })
        self._legend_visualmap_colorlst(**kwargs)
