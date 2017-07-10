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
              effect_brushtype="stroke",
              effect_scale=2.5,
              effect_period=4, **kwargs):
        """

        :param name:
            图例名称
        :param x_axis:
            x 坐标轴数据
        :param y_axis:
            y 坐标轴数据
        :param symbol_size:
            标记图形大小
        :param effect_brushtype:
            波纹绘制方式，有 stroke/fill 可选
        :param effect_scale:
            动画中波纹的最大缩放比例
        :param effect_period:
            动画的时间
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
                "rippleEffect":{
                    "brushType": effect_brushtype,
                    "scale": effect_scale,
                    "period":effect_period
                },
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": [list(z) for z in zip(x_value, y_value)],
                "label": chart['label'],
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("x_axis and y_axis must be list")
