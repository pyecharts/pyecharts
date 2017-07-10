#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyecharts.charts.scatter import Scatter
from pyecharts.option import get_all_options

class EffectScatter(Scatter):
    """
    <<< 带有涟漪特效动画的散点图 >>>
    利用动画特效可以将某些想要突出的数据进行视觉突出。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_value, y_value, *,
              symbol_size=10,
              **kwargs):
        """

        :param name:
            图例名称
        :param x_axis:
            x 坐标轴数据
        :param y_axis:
            y 坐标轴数据
        :param symbol_size:
            标记图形大小
        :param kwargs:
        """
        if isinstance(x_value, list) and isinstance(y_value, list):
            assert len(x_value) == len(y_value)
            kwargs.update(type="scatter")
            chart = get_all_options(**kwargs)
            xaxis, yaxis = chart['xy_axis']
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "type": "effectScatter",
                "name": name,
                "showEffectOn":"render",
                "rippleEffect": chart['effect'],
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": [list(z) for z in zip(x_value, y_value)],
                "label": chart['label'],
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("x_axis and y_axis must be list")
