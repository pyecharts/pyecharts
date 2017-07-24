#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class HeatMap(Base):
    """
    <<< 热力图>>>
    热力图主要通过颜色去表现数值的大小，必须要配合 visualMap 组件使用。直角坐标系上必须要使用两个类目轴。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(HeatMap, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis, data, **kwargs):
        """

        :param name:
            图例名称
        :param x_axis:
            x 坐标轴数据。需为类目轴，也就是不能是数值。
        :param y_axis:
            y 坐标轴数据。需为类目轴，也就是不能是数值。
        :param data:
            数据项，类型为包含列表的列表 [[]]。数据中，每一行是一个『数据项』，每一列属于一个『维度』
        :param kwargs:
        :return:
        """
        chart = get_all_options(**kwargs)
        self._option.get('legend').get('data').append(name)
        self._option.update(
            grid={
                "left": '15%',
                "bottom": '20%'
            },
            xAxis={
                "type": "category",
                "data": x_axis,
                "splitArea": {"show": True},
            },
            yAxis={
                "type": "category",
                "data": y_axis,
                "splitArea": {"show": True}
            })
        self._option.get('series').append({
            "type": "heatmap",
            "name": name,
            "data": data,
            "label": chart['label'],
        })
        self._legend_visualmap_colorlst(**kwargs)
