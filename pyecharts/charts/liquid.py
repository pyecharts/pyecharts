#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base

class Liquid(Base):
    """
    <<< Liquid chart >>>
    Liquid chart is usually used to represent data in percentage.
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
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param data:
            data of liquid,
            [0.6, 0.5, 0.4, 0.3] -> This creates a chart wit waves at position of 60%, 50%, 40%, and 30%.
        :param shape:
            Shape of water fill chart.
            It can be one of the default symbols: 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
        :param liquid_color:
            To set colors for liquid fill chart series, set color to be an array of colors.
        :param is_liquid_animation:
            Whether disable animation.
        :param is_liquid_outline_show:
            whether hide the outline
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
