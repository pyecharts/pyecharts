#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Kline(Base):
    """
    <<< Kline(Candlestick) chart >>>
    Kline chart use red to imply increasing with red and decreasing with blue
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Kline, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param x_axis:
            data of xAxis
        :param y_axis:
            data pf yAxis
            Data should be the two-dimensional array shown as follow. -> [[],[]]
            Every data item (each line in the example above) represents a box, which contains 4 values. They are:
            [open, close, lowest, highest]  (namely: [opening value, closing value, lowest value, highest value])
        :param kwargs:
        :return:
        """
        chart = get_all_options(**kwargs)
        self._option.update(
            xAxis=[{
                "type": "category",
                "data": x_axis,
                "scale": True,
                "boundaryGap": False
            }],
            yAxis=[{
                "scale": True,
                "splitArea": {"show": True}
            }])
        self._option.get('legend')[0].get('data').append(name)
        self._option.get('series').append({
            "type": "candlestick",
            "name": name,
            "data": y_axis,
            "markPoint": chart['mark_point'],
            "markLine": chart['mark_line'],
            "indexflag": self._option.get('_index_flag')
        })
        self._legend_visualmap_colorlst(**kwargs)
