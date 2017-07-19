#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Funnel(Base):
    """
    <<< 漏斗图 >>>
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Funnel, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value, **kwargs):
        """

        :param name:
            图例名称
        :param attr:
            属性名称
        :param value:
            属性所对应的值
        :param kwargs:
        """
        if isinstance(attr, list) and isinstance(value, list):
            assert len(attr) == len(value)
            chart = get_all_options(**kwargs)
            _data = []
            for data in zip(attr, value):
                _name, _value = data
                _data.append({"name": _name, "value": _value})
            for a in attr:
                self._option.get('legend').get('data').append(a)
            _dset = set(self._option.get('legend').get('data'))
            self._option.get('legend').update(data=list(_dset))
            self._option.get('series').append({
                "type": "funnel",
                "name": name,
                "data": _data,
                "label": chart['label'],
            })
            self._legend_visualmap_colorlst(**kwargs)
        else:
            raise TypeError("attr and value must be list")
