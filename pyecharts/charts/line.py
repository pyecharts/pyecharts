#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Line(Base):
    """
    <<< Broken Line >>>
    Broken line chart relates all the data points symbol by broken lines,
    which is used to show the trend of data changing.
    It could be used in both rectangular coordinate and polar coordinate.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Line, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, x_axis, y_axis,
              is_symbol_show=True,
              is_smooth=False,
              is_stack=False,
              is_step=False,
              is_fill=False,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param x_axis:
            data of xAxis
        :param y_axis:
            data of yAxis
        :param is_symbol_show:
            It specifies whether to show the symbol.
        :param is_smooth:
            Whether to show as smooth curve.
        :param is_stack:
            It specifies whether to stack category axis.
        :param is_step:
            Whether to show as a step line. It can be true, false. Or 'start', 'middle', 'end'.
            Which will configure the turn point of step line.
        :param is_fill:
            Whether to fill area.
        :param kwargs:
        """
        assert len(x_axis) == len(y_axis)
        kwargs.update(x_axis=x_axis, type="line")
        chart = get_all_options(**kwargs)
        xaxis, yaxis = chart['xy_axis']
        is_stack = "stack" if is_stack else ""
        _area_style = {"normal": chart['area_style']} if is_fill else {}
        self._option.update(xAxis=xaxis, yAxis=yaxis)
        self._option.get('legend')[0].get('data').append(name)
        self._option.get('series').append({
            "type": "line",
            "name": name,
            "symbol": chart['symbol'],
            "smooth": is_smooth,
            "step": is_step,
            "stack": is_stack,
            "showSymbol": is_symbol_show,
            "data": y_axis,
            "label": chart['label'],
            "lineStyle": chart['line_style'],
            "areaStyle": _area_style,
            "markPoint": chart['mark_point'],
            "markLine": chart['mark_line'],
            "indexflag": self._option.get('_index_flag')
        })
        self._legend_visualmap_colorlst(**kwargs)
