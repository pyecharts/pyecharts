#!/usr/bin/env python
# coding=utf-8

from pyecharts.chart import Chart
from pyecharts.option import get_all_options
from pyecharts.constants import (CITY_GEO_COORDS,
                                 CITY_NAME_PINYIN_MAP, SYMBOL)


class GeoLines(Chart):
    """
    Geographic coordinate system component.

    It is used to draw maps, which also supports lines.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(GeoLines, self).__init__(title, subtitle, **kwargs)
        self._zlevel = 1

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data,
              maptype='china',
              symbol=None,
              symbol_size=12,
              border_color="#111",
              geo_normal_color="#323c48",
              geo_emphasis_color="#2a333d",
              geo_cities_coords=None,
              geo_effect_period=6,
              geo_effect_traillength=0,
              geo_effect_color='#fff',
              geo_effect_symbol='circle',
              geo_effect_symbolsize=5,
              is_geo_effect_show=True,
              is_roam=True,
              **kwargs):
        """

        :param name:
        :param data:
        :param maptype:
        :param symbol:
        :param symbol_size:
        :param border_color:
        :param geo_normal_color:
        :param geo_emphasis_color:
        :param geo_cities_coords:
        :param geo_effect_period:
        :param geo_effect_traillength:
        :param geo_effect_color:
        :param geo_effect_symbol:
        :param geo_effect_symbolsize:
        :param is_geo_effect_show:
        :param is_roam:
        :param kwargs:
        :return:
        """

        chart = get_all_options(**kwargs)
        self._zlevel += 1
        if geo_cities_coords:
            _geo_cities_coords = geo_cities_coords
        else:
            _geo_cities_coords = CITY_GEO_COORDS

        if geo_effect_symbol == "plane":
            geo_effect_symbol = SYMBOL['plane']

        _data_lines, _data_scatter = [], []
        for d in data:
            _from_name, _to_name = d
            _data_lines.append({
                "fromName": _from_name,
                "toName": _to_name,
                "coords": [
                    _geo_cities_coords.get(_from_name, []),
                    _geo_cities_coords.get(_to_name, [])
                ]
            })
            _from_v = _geo_cities_coords.get(_from_name, []).copy()
            _data_scatter.append({
                "name": _from_name,
                "value": _from_v + [0]
            })
            _to_v = _geo_cities_coords.get(_to_name, []).copy()
            _data_scatter.append({
                "name": _to_name,
                "value": _to_v + [0]
            })

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
        self._option.get('series').append({
            "type": "lines",
            "name": name,
            "zlevel": self._zlevel,
            "effect": {
                "show": is_geo_effect_show,
                "period": geo_effect_period,
                "trailLength": geo_effect_traillength,
                "color": geo_effect_color,
                "symbol": geo_effect_symbol,
                "symbolSize": geo_effect_symbolsize
            },
            "symbol": symbol or ["none", "arrow"],
            "symbolSize": symbol_size,
            "data": _data_lines,
            "lineStyle": chart['line_style']
        })
        self._option.get('series').append({
            "type": "scatter",
            "name": name,
            "zlevel": self._zlevel,
            "coordinateSystem": 'geo',
            "symbolSize": 10,
            "data": _data_scatter,
            "label": chart['label'],
        })

        name_in_pinyin = CITY_NAME_PINYIN_MAP.get(maptype, maptype)
        self._js_dependencies.add(name_in_pinyin)
        self._config_components(**kwargs)
