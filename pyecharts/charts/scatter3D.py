#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options


class Scatter3D(Base):
    """
    <<< Scatter3D chart >>>
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Scatter3D, self).__init__(title, subtitle, **kwargs)
        self._js_dependencies.add('echartsgl')

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data,
              grid3d_opacity=1,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering
            with legend, or updaing data and configuration with setOption.
        :param data:
            data of Scatter3D
        :param grid3d_opacity:
            opacity of gird3D item
        :param kwargs:
        :return:
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
            "type": "scatter3D",
            "name": name,
            "data": data,
            "label": chart['label'],
            "itemStyle": {
                "opacity": grid3d_opacity
            }
        })
        self._legend_visualmap_colorlst(**kwargs)
