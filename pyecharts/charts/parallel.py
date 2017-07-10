#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyecharts.base import Base

class Parallel(Base):
    """
    <<< 平行坐标系 >>>
    平行坐标系是一种常用的可视化高维数据的图表。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def config(self, schema=None, *, c_schema=None):
        """

        :param schema:
            默认平行坐标系的坐标轴信息
        :param c_schema:
            用户自定义平行坐标系的坐标轴信息
        :return:
        """
        if schema:
            _schema = [{"dim": i, "name": v} for i, v in enumerate(schema)]
            self._option.update(parallelAxis=_schema)
        if c_schema:
            self._option.update(parallelAxis=c_schema)

    def __add(self, name, data, **kwargs):
        """

        :param name:
            图例名称
        :param data:
            数据项，类型为包含列表的列表 [[]]。数据中，每一行是一个『数据项』，每一列属于一个『维度』
        :param kwargs:
        :return:
        """
        self._option.update(parallel={"left": "5%", "right": "13%", "bottom": "10%", "top": "20%"})
        self._option.get('legend').get('data').append(name)
        self._option.get('series').append({
            "type": "parallel",
            "coordinateSystem": "parallel",
            "name": name,
            "data": data
        })
        self._legend_visualmap_colorlst(**kwargs)
