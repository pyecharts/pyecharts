#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base

class Gauge(Base):
    """
    <<< Gauge chart >>>
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Gauge, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value,
              scale_range=None,
              angle_range=None,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param attr:
            name of attribute
        :param value:
            value of attribute
        :param scale_range:
            data range of guage
        :param angle_range:
            angle range of guage
            The direct right side of circle center is 0 degree,
            the right above it is 90 degree, the direct left side of it is 180 degree.
        :param kwargs:
        """
        # default data range is [0, 100]
        _min, _max = 0, 100
        if scale_range:
            if len(scale_range) == 2:
                _min, _max = scale_range

        # defalut angle range is [225, -45]
        _start, _end = 225, -45
        if angle_range:
            if len(angle_range) == 2:
                _start, _end = angle_range

        self._option.get('legend')[0].get('data').append(name)
        self._option.get('series').append({
            "type": "gauge",
            "detail": {"formatter": '{value}%'},
            "name": name,
            "min": _min,
            "max": _max,
            "startAngle": _start,
            "endAngle": _end,
            "data": [{"value": value, "name": attr}]
        })
        self._option.update(tooltip={"formatter": "{a} <br/>{b} : {c}%"})
        self._legend_visualmap_colorlst(**kwargs)
