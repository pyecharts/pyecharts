#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options


class Boxplot(Base):
    """
    <<< Boxplot chart >>>

    Boxplot is a convenient way of graphically depicting groups of numerical
    data through their quartiles.
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Boxplot, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param x_axis:
            data of xAixs
        :param y_axis:
            data of yAxis
        :param kwargs:
        :return:
        """
        assert len(x_axis) == len(y_axis)
        kwargs.update(x_axis=x_axis)
        chart = get_all_options(**kwargs)

        xaxis, yaxis = chart['xy_axis']
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get('legend')[0].get('data').append(name)
        self._option.get('series').append({
            "type": "boxplot",
            "name": name,
            "data": y_axis,
            "label": chart['label'],
            "markPoint": chart['mark_point'],
            "markLine": chart['mark_line'],
            "indexflag": self._option.get('_index_flag')
        })
        self._legend_visualmap_colorlst(**kwargs)

    @staticmethod
    def prepare_data(data):
        """

        :param data:
        :return:
        """
        _data = []
        for d in data:
            try:
                _d, _result = sorted(d), []
                for i in range(1, 4):
                    n = i * (len(_d) + 1) / 4
                    m = n - int(n)
                    if m == 0:
                        _result.append(_d[int(n) - 1])
                    elif m == 1 / 4:
                        _result.append(_d[int(n) - 1] * 0.75 + _d[int(n)] * 0.25)
                    elif m == 1 / 2:
                        _result.append(_d[int(n) - 1] * 0.5 + _d[int(n)] * 0.5)
                    elif m == 3 / 4:
                        _result.append(_d[int(n) - 1] * 0.25 + _d[int(n)] * 0.75)
                _result.insert(0, _d[0])    # min
                _result.append(_d[-1])      # max
                _data.append(_result)
            except Exception:
                pass
        return _data
