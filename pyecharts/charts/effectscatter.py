# coding=utf-8

from pyecharts.charts.scatter import Scatter
from pyecharts.option import get_all_options


class EffectScatter(Scatter):
    """
    <<< 带有涟漪特效动画的散点图 >>>

    利用动画特效可以将某些想要突出的数据进行视觉突出。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(EffectScatter, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis,
              symbol_size=10,
              **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param x_axis:
            x 坐标轴数据。
        :param y_axis:
            y 坐标轴数据。
        :param symbol_size:
            标记图形大小。
        :param kwargs:
        """
        assert len(x_axis) == len(y_axis)
        kwargs.update(type="scatter")
        chart = get_all_options(**kwargs)

        xaxis, yaxis = chart['xy_axis']
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get('legend')[0].get('data').append(name)

        self._option.get('series').append({
            "type": "effectScatter",
            "name": name,
            "showEffectOn": "render",
            "rippleEffect": chart['effect'],
            "symbol": chart['symbol'],
            "symbolSize": symbol_size,
            "data": [list(z) for z in zip(x_axis, y_axis)],
            "label": chart['label'],
            "seriesId": self._option.get('series_id'),
        })
        self._config_components(**kwargs)
