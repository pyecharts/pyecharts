#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base

class Liquid(Base):
    """
    <<< 水球图 >>>
    主要用来突出数据的百分比
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Liquid, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data,
              shape='circle',
              liquid_color=None,
              is_liquid_animation=True,
              is_liquid_outline_show=True,
              **kwargs):
        """

        :param name:
            图例名称
        :param data:
            数据项
        :param shape:
            水球外形，有'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选
        :param liquid_color:
            波浪颜色
        :param is_liquid_animation:
            是否显示波浪动画
        :param is_liquid_outline_show:
            是否显示边框
        :param kwargs:
        :return:
        """
        _animation_dur, _animation_dur_update = 2000, 1000
        if not is_liquid_animation:
            _animation_dur, _animation_dur_update = 0, 0

        _color = ['#294D99', '#156ACF', '#1598ED', '#45BDFF']
        if liquid_color:
            _color = liquid_color

        _shape = 'circle'
        if shape in ('circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'):
            _shape = shape

        self._option.get('series').append({
            "type": "liquidFill",
            "name": name,
            "data": data,
            "waveAnimation": is_liquid_animation,
            "animationDuration": _animation_dur,
            "animationDurationUpdate": _animation_dur_update,
            "color": _color,
            "shape": _shape,
            "outline": {"show": is_liquid_outline_show}
        })
