#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Pie(Base):
    """
    <<< 饼图 >>>
    饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Pie, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value,
              radius=None,
              center=None,
              rosetype=None,
              **kwargs):
        """

        :param name:
            图例名称
        :param attr:
            属性名称
        :param value:
            属性所对应的值
        :param radius:
            饼图的半径，数组的第一项是内半径，第二项是外半径
            默认设置成百分比，相对于容器高宽中较小的一项的一半
        :param center:
            饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
            默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
        :param rosetype:
            是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。默认为'radius'
            radius：扇区圆心角展现数据的百分比，半径展现数据的大小
            area：所有扇区圆心角相同，仅通过半径展现数据大小
        :param kwargs:
        """
        if isinstance(attr, list) and isinstance(value, list):
            kwargs.update(type="pie")
            chart = get_all_options(**kwargs)
            assert len(attr) == len(value)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                _data.append({"name": _name, "value": _value})

            _rmin, _rmax = "0%", "75%"
            if radius:
                if len(radius) == 2:
                    _rmin, _rmax = ["{}%".format(r) for r in radius]

            _cmin, _cmax = "50%", "50%"
            if center:
                if len(center) == 2:
                    _cmin, _cmax = ["{}%".format(c) for c in center]

            if rosetype:
                if rosetype not in ("radius", "area"):
                    rosetype = "radius"
            for a in attr:
                self._option.get('legend').get('data').append(a)
            self._option.get('series').append({
                "type": "pie",
                "name": name,
                "data": _data,
                "radius": [_rmin, _rmax],
                "center": [_cmin, _cmax],
                "roseType": rosetype,
                "label": chart['label'],
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("attr and value must be list")
