#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options


class Bar(Base):
    """
    <<< Bar chart >>>

    Bar chart shows different data through the height of a bar, which is used in
    rectangular coordinate with at least 1 category axis.
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Bar, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis,
              is_stack=False,
              bar_category_gap="20%",
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updating data and configuration with setOption.
        :param x_axis:
            data of xAixs
        :param y_axis:
            data of yAxis
        :param is_stack:
            It specifies whether to stack category axis.
        :param kwargs:
        """
        assert len(x_axis) == len(y_axis)
        kwargs.update(x_axis=x_axis)
        chart = get_all_options(**kwargs)

        is_stack = "stack_" + str(self._option['series_id']) if is_stack else ""
        xaxis, yaxis = chart['xy_axis']
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get('legend')[0].get('data').append(name)

        self._option.get('series').append({
            "type": "bar",
            "name": name,
            "data": y_axis,
            "stack": is_stack,
            "barCategoryGap": bar_category_gap,
            "label": chart['label'],
            "markPoint": chart['mark_point'],
            "markLine": chart['mark_line'],
            "seriesId": self._option.get('series_id'),
        })
        self._config_components(**kwargs)
