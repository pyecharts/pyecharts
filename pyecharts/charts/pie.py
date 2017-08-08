#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Pie(Base):
    """
    <<< Pie chart >>>
    The pie chart is mainly used for showing proportion of different categories.
    Each arc length represents the proportion of data quantity.
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
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param attr:
            name of attribute
        :param value:
            value of attribute
        :param radius:
            Radius of Pie chart, the first of which is inner radius, and the second is outer radius.
            Percentage is supported. When set in percentage,
            it's relative to the smaller size between height and width of the container.
        :param center:
            Center position of Pie chart, the first of which is the horizontal position,
            and the second is the vertical position.
            Percentage is supported. When set in percentage, the item is relative to the container width,
            and the second item to the height.
        :param rosetype:
            Whether to show as Nightingale chart, which distinguishs data through radius. There are 2 optional modes:
            'radius' Use central angle to show the percentage of data, radius to show data size.
            'area' All the sectors will share the same central angle, the data size is shown only through radiuses.
        :param kwargs:
        """
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
            self._option.get('legend')[0].get('data').append(a)
        _dlst = self._option.get('legend')[0].get('data')
        _dset = list(set(_dlst))
        _dset.sort(key=_dlst.index)
        self._option.get('legend')[0].update(data=list(_dset))
        self._option.get('series').append({
            "type": "pie",
            "name": name,
            "data": _data,
            "radius": [_rmin, _rmax],
            "center": [_cmin, _cmax],
            "roseType": rosetype,
            "label": chart['label'],
            "indexflag": self._option.get('_index_flag')
        })
        self._legend_visualmap_colorlst(**kwargs)
