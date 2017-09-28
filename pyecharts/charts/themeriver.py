#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options


class ThemeRiver(Base):
    """
    <<< Theme river >>>

    It is a special flow graph which is mainly used to present the
    changes of an event or theme during a period.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(ThemeRiver, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data, **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updating data and configuration with setOption.It must be a list.
        :param data:
            data array of series, it is represented by a two-dimension array -> [[],[]]
            every data item need three value, for example
            ['2015/11/08',10,'DQ'] -> [time, value, legend(category)]
        :param kwargs:
        :return:
        """
        chart = get_all_options(**kwargs)
        self._option.get('legend')[0].get('data').extend(name)

        self._option.get('series').append({
            "type": "themeRiver",
            "name": name,
            "data": data,
            "label": chart['label'],
            "seriesId": self._option.get('series_id'),
        })

        self._option.update(singleAxis={"type": "time"})
        self._config_components(**kwargs)
        self._option.get('tooltip').update(trigger='axis')
