#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Radar(Base):
    """
    <<< 雷达图 >>>
    雷达图主要用于表现多变量的数据。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Radar, self).__init__(title, subtitle, **kwargs)

    def config(self, schema=None,
               c_schema=None,
               shape="",
               rader_text_color="#000",
               **kwargs):
        """ 配置 rader 组件选项

        :param schema:
            默认雷达图的指示器，用来指定雷达图中的多个维度，会对数据处理成 {name:xx, value:xx} 的字典
        :param c_schema:
            用户自定义雷达图的指示器，用来指定雷达图中的多个维度
            name: 指示器名称
            min: 指示器最小值
            max: 指示器最大值
        :param shape:
            雷达图绘制类型，支持 polygon（多边形） 和 circle
        :param rader_text_color:
            雷达图数据项字体颜色
        :param kwargs:
        """
        chart = get_all_options(**kwargs)
        indicator = []
        if schema:
            for s in schema:
                _name, _max = s
                indicator.append({"name": _name, "max": _max})
        if c_schema:
            indicator = c_schema
        self._option.update(
            radar={
                "indicator": indicator,
                "shape": shape,
                "name": {"textStyle": {"color": rader_text_color}},
                "splitLine": chart['split_line'],
                "splitArea": chart['split_area'],
                "axisLine": chart['axis_line']}
        )

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, value, item_color=None, **kwargs):
        """

        :param name:
            图例名称
        :param value:
            数据项，类型为包含列表的列表 [[]]。数据中，每一行是一个『数据项』，每一列属于一个『维度』
        :param item_color:
            指定单图例颜色
        :param kwargs:
        """
        kwargs.update(flag=True, type='radar')
        chart = get_all_options(**kwargs)
        self._option.get('legend').get('data').append(name)
        self._option.get('series').append({
            "type": "radar",
            "name": name,
            "data": value,
            "symbol": chart['symbol'],
            "itemStyle": {"normal": {"color": item_color}},
            "lineStyle": chart['line_style'],
            "areaStyle": {"normal": chart['area_style']}
        })
        self._legend_visualmap_colorlst(**kwargs)
