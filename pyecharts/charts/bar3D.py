#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options


class Bar3D(Base):
    """
    <<< Bar3D chart >>>
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Bar3D, self).__init__(title, subtitle, **kwargs)
        self._js_dependencies.add('echartsgl')

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, data,
              grid3d_opacity=1,
              grid3d_shading='color',
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param x_axis:
            xAxis data
        :param y_axis:
            yAxis data
        :param data:
            zAxis data
        :param grid3d_opacity:
            opacity of gird3D item
        :param grid3d_shading:
            3D graphics coloring effect
            'color':
                Only show color, not affected by lighting and other factors.
            'lambert':
                Through the classic lambert coloring to show the light and shade.
            'realistic':
                ealistic rendering.
        :param kwargs:
        :return:
        """
        kwargs.update(xaxis3d_type='category',
                      yaxis3d_type='category',
                      zaxis3d_type='value')
        chart = get_all_options(**kwargs)

        self._option.get('legend')[0].get('data').append(name)
        self._option.update(
            xAxis3D=chart['xaxis3D'],
            yAxis3D=chart['yaxis3D'],
            zAxis3D=chart['zaxis3D'],
            grid3D=chart['grid3D']
        )
        self._option.get('xAxis3D').update(data=x_axis)
        self._option.get('yAxis3D').update(data=y_axis)

        self._option.get('series').append({
            "type": "bar3D",
            "name": name,
            "data": data,
            "label": chart['label'],
            "shading": grid3d_shading,
            "itemStyle": {"opacity": grid3d_opacity}
        })
        self._legend_visualmap_colorlst(**kwargs)
