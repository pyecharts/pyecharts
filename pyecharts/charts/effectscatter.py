#!/usr/bin/env python
#coding=utf-8

from pyecharts.charts.scatter import Scatter
from pyecharts.option import get_all_options

class EffectScatter(Scatter):
    """
    <<< EffectScatter chart >>>
    The scatter graph with ripple animation. The special animation effect can visually highlights some data.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(EffectScatter, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_value, y_value,
              symbol_size=10,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param x_axis:
            data of xAxis
        :param y_axis:
            data of yAxis
        :param symbol_size:
            symbol size
        :param kwargs:
        """
        assert len(x_value) == len(y_value)
        kwargs.update(type="scatter")
        chart = get_all_options(**kwargs)
        xaxis, yaxis = chart['xy_axis']
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get('legend')[0].get('data').append(name)
        self._option.get('series').append({
            "type": "effectScatter",
            "name": name,
            "showEffectOn":"render",
            "rippleEffect": chart['effect'],
            "symbol": chart['symbol'],
            "symbolSize": symbol_size,
            "data": [list(z) for z in zip(x_value, y_value)],
            "label": chart['label'],
            "indexflag": self._option.get('_index_flag')
        })
        self._legend_visualmap_colorlst(**kwargs)
