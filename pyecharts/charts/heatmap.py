#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class HeatMap(Base):
    """
    <<< HeatMap chart >>>
    Heat map mainly use colors to represent values, which must be used along with visualMap component.
    It can be used in either rectangular coordinate or geographic coordinate.
    But the behaviour on them are quite different. Rectangular coordinate must have two catagories to use it.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(HeatMap, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, data, **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param x_axis:
            data of xAxis, it must be catagory axis.
        :param y_axis:
            data of yAxis, it must be catagory axis.
        :param data:
            data array of series, it is represented by a two-dimension array -> [[],[]]
        :param kwargs:
        :return:
        """
        chart = get_all_options(**kwargs)
        self._option.get('legend')[0].get('data').append(name)
        self._option.update(
            xAxis=[{
                "type": "category",
                "data": x_axis,
                "splitArea": {"show": True},
            }],
            yAxis=[{
                "type": "category",
                "data": y_axis,
                "splitArea": {"show": True}
            }])
        self._option.get('series').append({
            "type": "heatmap",
            "name": name,
            "data": data,
            "label": chart['label'],
            "indexflag": self._option.get('_index_flag')
        })
        self._legend_visualmap_colorlst(**kwargs)
