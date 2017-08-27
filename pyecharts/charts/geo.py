#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options
from pyecharts.constants import CITY_GEO_COORDS


class Geo(Base):
    """
    Geographic coorinate system component.

    It is used to draw maps, which also supports scatter series, and line
    series.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Geo, self).__init__(title, subtitle, **kwargs)
        self._js_dependencies.add('china')

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
            Series name used for displaying in tooltip and filtering with
            legend, or updaing data and configuration with setOption.
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
        kwargs.update(type="geo")
        chart = get_all_options(**kwargs)

        _data = []
        for name, value in zip(attr, value):
            if name in CITY_GEO_COORDS:
                city_coordinate = CITY_GEO_COORDS.get(name)
                city_coordinate.append(value)
                _data.append({"name": name, "value": city_coordinate})
            else:
                print("%s coordinates is not found" % name)
        self._option.update(
            geo={
                "map": maptype,
                "label": {},
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
        self._legend_visualmap_colorlst(**kwargs)
