#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Radar(Base):
    """
    <<< Radar chart >>>
    Radar chart is mainly used to show multi-variable data,
    such as the analysis of a football player's varied attributes. It relies radar component.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Radar, self).__init__(title, subtitle, **kwargs)

    def config(self, schema=None,
               c_schema=None,
               shape="",
               rader_text_color="#000",
               **kwargs):
        """ config rader component options

        :param schema:
            The default radar map indicator, used to specify multiple dimensions in the radar map,
            will process the data into a dictionary of {name: xx, value: xx}
        :param c_schema:
            Indicator of radar chart, which is used to assign multiple variables(dimensions) in radar chart.
            name: Indicator's name.
            min: The maximum value of indicator. It is an optional configuration, but we recommend to set it manually.
            max: The maximum value of indicator. It is an optional configuration, but we recommend to set it manually.
        :param shape:
            Radar render type, in which 'polygon' and 'circle' are supported.
        :param rader_text_color:
            Radar chart data item font color
        :param kwargs:
        """
        chart = get_all_options(**kwargs)
        indicator = []
        if schema:
            for s in schema:
                _name, _max = s
                indicator.append({"name": _name, "max": _max})
        if c_schema:
            indicator = c_schema
        self._option.update(
            radar={
                "indicator": indicator,
                "shape": shape,
                "name": {"textStyle": {"color": rader_text_color}},
                "splitLine": chart['split_line'],
                "splitArea": chart['split_area'],
                "axisLine": chart['axis_line']}
        )

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, value, item_color=None, **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param value:
            data array of series, it is represented by a two-dimension array -> [[],[]]
        :param item_color:
            Specify a single legend color
        :param kwargs:
        """
        kwargs.update(flag=True, type='radar')
        chart = get_all_options(**kwargs)
        self._option.get('legend')[0].get('data').append(name)
        self._option.get('series').append({
            "type": "radar",
            "name": name,
            "data": value,
            "symbol": chart['symbol'],
            "itemStyle": {"normal": {"color": item_color}},
            "lineStyle": chart['line_style'],
            "areaStyle": {"normal": chart['area_style']},
        })
        self._legend_visualmap_colorlst(**kwargs)
