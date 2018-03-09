# coding=utf-8

from pyecharts.chart import Chart
from pyecharts.option import get_all_options
import pyecharts.constants as constants


class Line3D(Chart):
    """
    <<< 3D 折线图 >>>
    """

    def __init__(self, title="", subtitle="", **kwargs):
        kwargs['renderer'] = constants.CANVAS_RENDERER
        super(Line3D, self).__init__(title, subtitle, **kwargs)
        self._js_dependencies.add('echartsgl')

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data,
              grid3d_opacity=1,
              **kwargs):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param data:
            数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。
        :param grid3d_opacity:
            3D 笛卡尔坐标系组的透明度（线的透明度），默认为 1，完全不透明。
        :param kwargs:
        """
        kwargs.update(xaxis3d_type='value',
                      yaxis3d_type='value',
                      zaxis3d_type='value')
        chart = get_all_options(**kwargs)

        self._option.get('legend')[0].get('data').append(name)
        self._option.update(
            xAxis3D=chart['xaxis3D'],
            yAxis3D=chart['yaxis3D'],
            zAxis3D=chart['zaxis3D'],
            grid3D=chart['grid3D']
        )

        self._option.get('series').append({
            "type": "line3D",
            "name": name,
            "data": data,
            "label": chart['label'],
            "itemStyle": {"opacity": grid3d_opacity}
        })
        self._config_components(**kwargs)
