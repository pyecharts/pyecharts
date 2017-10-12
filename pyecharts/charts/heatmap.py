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

    def __add(self, *args, **kwargs):
        """

        :param args:
            if kwargs has is_calendar_heatmap property:
                :param name:
                    Series name used for displaying in tooltip and filtering with legend,
                    or updating data and configuration with setOption.
                :param data:
                    data array of series, it is represented by a two-dimension array -> [[],[]]
            else:
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
        _is_calendar = kwargs.get('is_calendar_heatmap', None) is True
        if _is_calendar:
            name, data = args
        else:
            name, x_axis, y_axis, data = args

        chart = get_all_options(**kwargs)
        self._option.get('legend')[0].get('data').append(name)

        self._option.get('series').append({
            "type": "heatmap",
            "name": name,
            "data": data,
            "label": chart['label'],
            "seriesId": self._option.get('series_id'),
        })

        if _is_calendar:
            self._option.get('toolbox')['show'] = False
            self._option.get('series')[0].update(coordinateSystem='calendar')
            self._option.update(calendar=chart['calendar'])
        else:
            xaxis, yaxis = chart['xy_axis']
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('xAxis')[0].update(
                type='category', data=x_axis, splitArea={"show": True})
            self._option.get('yAxis')[0].update(
                type='category', data=y_axis, splitArea={"show": True})

        self._config_components(**kwargs)
