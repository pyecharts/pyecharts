#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Kline(Base):
    """
    <<< K线图 >>>
    红涨蓝跌。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Kline, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, **kwargs):
        """

        :param name:
            图例名称
        :param x_axis:
            x 坐标轴数据
        :param y_axis:
            y 坐标轴数据，类型为包含列表的列表 [[]]。数据中，每一行是一个『数据项』，每一列属于一个『维度』。
            数据项具体为 [open, close, lowest, highest] （即：[开盘值, 收盘值, 最低值, 最高值]）
        :param kwargs:
        :return:
        """
        chart = get_all_options(**kwargs)
        self._option.update(
            xAxis={
                "type": "category",
                "data": x_axis,
                "scale": True,
                "boundaryGap": False
            },
            yAxis={
                "scale": True,
                "splitArea": {"show": True}
            })
        self._option.get('legend').get('data').append(name)
        self._option.get('series').append({
            "type": "candlestick",
            "name": name,
            "data": y_axis,
            "markPoint": chart['mark_point'],
            "markLine": chart['mark_line']
        })
        self._legend_visualmap_colorlst(**kwargs)
