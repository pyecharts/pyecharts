#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Geo(Base):
    """
    <<< Geo component >>>
    Geographic coorinate system component.
    Geographic coorinate system component is used to draw maps, which also supports scatter series, and line series.
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
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param attr:
            name of attribute
        :param value:
            value of attribute
        :param type:
            chart type, it can be 'scatter', 'effectscatter', 'heatmap'
        :param maptype:
            type of map, it only supports 'china' temporarily.
        :param symbol_size:
            symbol size
        :param border_color:
            color of map border
        :param geo_normal_color:
            The color of the map area in normal state
        :param geo_emphasis_color:
            The color of the map area in emphasis state
        :param kwargs:
        """
        assert len(attr) == len(value)
        chart = get_all_options(**kwargs)
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            if _name in self._geo_cities:
                _v = self._geo_cities.get(_name)
                _v.append(_value)
                _value = list(_v)
            _data.append({"name": _name, "value": _value})
        self._option.update(
            geo={
                "map": maptype,
                "label": {},
                "itemStyle": {"normal": {
                    "areaColor": geo_normal_color,
                    "borderColor": border_color},
                    "emphasis":{"areaColor": geo_emphasis_color}}
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
        self._legend_visualmap_colorlst(**kwargs)

