#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import gen_color

class WordCloud(Base):
    """
    <<< WordCloud chart >>>
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(WordCloud, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value,
              shape="circle",
              word_gap=20,
              word_size_range=None,
              rotate_step=45):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param attr:
            name of attribute
        :param value:
            value of attribute
        :param shape:
            shape of wordcloud
            It can be 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'
        :param word_gap:
            Gap of word
            size of the grid in pixels for marking the availability of the canvas
            the larger the grid size, the bigger the gap between words.
        :param word_size_range:
            Text size range which the value in data will be mapped to.
            Default to have minimum 12px and maximum 60px size.
        :param rotate_step:
            Text rotation range and step in degree. Text will be rotated randomly in range [-90, 90] by rotationStep 45
        """
        assert len(attr) == len(value)
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append({
                "name": _name,
                "value": _value,
                "textStyle": {
                    "normal": {"color": gen_color()}}
            })
        _min, _max = 12, 60
        if word_size_range is not None:
            if len(word_size_range) == 2:
                _min, _max = word_size_range

        _rmin, _rmax = -90, 90
        # make sure shape valid, need to set ratated range [-90, 90]
        if shape in ("cardioid", "diamond", "triangle-forward", "triangle", "pentagon", "star"):
            _rmin = _rmax = 0
        else:
            shape = "circle"
        self._option.get('series').append({
            "type": "wordCloud",
            "name": name,
            "shape": shape,
            "rotationRange": [_rmin, _rmax],
            "rotationStep": rotate_step,
            "girdSize": word_gap,
            "sizeRange": [_min, _max],
            "data": _data
        })
