#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Line3D(Base):
    """
    <<< Line3D chart >>>
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Line3D, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data,
              grid3D_opacity=1,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param data:
            data of line3D
        :param grid3D_opacity:
            opacity of gird3D item
        :param kwargs:
        :return:
        """
        chart = get_all_options(**kwargs)
        self._option.get('legend')[0].get('data').append(name)
        self._option.update(
            xAxis3D={
                "type": 'value',
            },
            yAxis3D={
                "type": "value",
            },
            zAxis3D={"type": "value"},
            grid3D=chart['grid3D']
        )
        self._option.get('series').append({
            "type": "line3D",
            "name": name,
            "data": data,
            "label": chart['label'],
            "itemStyle": {"opacity": grid3D_opacity}
        })
        self._legend_visualmap_colorlst(**kwargs)
