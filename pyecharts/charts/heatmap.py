#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options


class HeatMap(Base):
    """
    <<< HeatMap chart >>>

    Heat map mainly use colors to represent values， which must be used along
    with visualMap component.
    It can be used in either rectangular coordinate or geographic coordinate.
    But the behaviour on them are quite different. Rectangular coordinate
    must have two categories to use it.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(HeatMap, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, data, **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updating data and configuration with setOption.
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

        xaxis, yaxis = chart['xy_axis']
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get('xAxis')[0].update(
            type='category', data=x_axis, splitArea={"show": True})
        self._option.get('yAxis')[0].update(
            type='category', data=y_axis, splitArea={"show": True})

        self._option.get('series').append({
            "type": "heatmap",
            "name": name,
            "data": data,
            "label": chart['label'],
            "seriesId": self._option.get('series_id'),
        })
        self._config_components(**kwargs)
