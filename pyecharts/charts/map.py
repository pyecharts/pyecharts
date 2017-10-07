#!/usr/bin/env python
# coding=utf-8
import sys

from pyecharts.base import Base
from pyecharts.option import get_all_options
from pyecharts.constants import CITY_NAME_PINYIN_MAP

PY2 = sys.version_info[0] == 2


class Map(Base):
    """
    <<< Map chart >>>

    Map is mainly used in the visualization of geographic area data,which
    can be used with visualMap component to visualize the data such as
    population distribution density in different areas.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Map, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value,
              is_roam=True,
              maptype='china',
              is_map_symbol_show=True,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with
            legend, or updating data and configuration with setOption.
        :param attr:
            name of attribute
        :param value:
            value of attribute
        :param is_roam:
            Whether to enable mouse zooming and translating. false by default.
            If either zooming or translating is wanted,
            it can be set to 'scale' or 'move'. Otherwise, set it to be true
            to enable both.
        :param is_map_symbol_show:
            Show or hide legend symbol in the map. Default to show a red dot.
            False to hide it.
        :param maptype:
            type of map, it supports
            china、world、...
        :param kwargs:
        """
        assert len(attr) == len(value)
        chart = get_all_options(**kwargs)
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append({"name": _name, "value": _value})
        self._option.get('legend')[0].get('data').append(name)

        self._option.get('series').append({
            "type": "map",
            "name": name,
            "symbol": chart['symbol'],
            "label": chart['label'],
            "mapType": maptype,
            "data": _data,
            "roam": is_roam,
            "showLegendSymbol": is_map_symbol_show
        })
        name_in_pinyin = CITY_NAME_PINYIN_MAP.get(maptype, maptype)
        self._js_dependencies.add(name_in_pinyin)
        self._config_components(**kwargs)
