#!/usr/bin/env python
# coding=utf-8

from pyecharts.chart import Chart
from pyecharts.option import get_all_options


class Kline(Chart):
    """
    <<< K 线图 >>>

    红涨蓝跌
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Kline, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param x_axis:
            x 坐标轴数据。
        :param y_axis:
            y 坐标轴数据。数据中，每一行是一个『数据项』，每一列属于一个『维度』。
            数据项具体为 [open, close, lowest, highest] （即：[开盘值, 收盘值,
             最低值, 最高值]）。
        :param kwargs:
        """
        kwargs.update(type="candlestick", x_axis=x_axis)
        chart = get_all_options(**kwargs)

        xaxis, yaxis = chart['xy_axis']
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get('xAxis')[0].update(scale=True)
        self._option.get('yAxis')[0].update(
            scale=True, splitArea={"show": True})

        self._option.get('legend')[0].get('data').append(name)

        self._option.get('series').append({
            "type": "candlestick",
            "name": name,
            "data": y_axis,
            "markPoint": chart['mark_point'],
            "markLine": chart['mark_line'],
            "seriesId": self._option.get('series_id'),
        })
        self._config_components(**kwargs)
