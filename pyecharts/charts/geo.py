#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options
from pyecharts.constants import CITY_GEO_COORDS
from pyecharts.constants import CITY_NAME_PINYIN_MAP


class Geo(Base):
    """
    Geographic coordinate system component.

    It is used to draw maps, which also supports scatter series, and line
    series.
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
            Series name used for displaying in tooltip and filtering with
            legend, or updating data and configuration with setOption.
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
        :param geo_cities_coords:
            User define cities coords
        :param is_roam:
            Whether to enable mouse zooming and translating. false by default.
            If either zooming or translating is wanted,
            it can be set to 'scale' or 'move'. Otherwise, set it to be true
            to enable both.
        :param kwargs:
        """
        assert len(attr) == len(value)
        kwargs.update(type="geo")
        chart = get_all_options(**kwargs)

        if geo_cities_coords:
            _geo_cities_coords = geo_cities_coords
        else:
            _geo_cities_coords = CITY_GEO_COORDS

        _data = []
        for name, value in zip(attr, value):
            if name in _geo_cities_coords:
                city_coordinate = _geo_cities_coords.get(name)
                city_coordinate.append(value)
                _data.append({"name": name, "value": city_coordinate})
            else:
                print("%s coordinates is not found" % name)
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
        name_in_pinyin = CITY_NAME_PINYIN_MAP.get(maptype, maptype)
        self._js_dependencies.add(name_in_pinyin)
        self._config_components(**kwargs)
