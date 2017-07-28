#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Polar(Base):
    """
    <<< Polar component >>>
    Polar coordinate can be used in scatter and line chart. Every polar coordinate has an angleAxis and a radiusAxis.
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Polar, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data,
              angle_data=None,
              radius_data=None,
              type='line',
              symbol_size=4,
              start_angle=90,
              rotate_step=0,
              boundary_gap=True,
              clockwise=True,
              is_stack=False,
              axis_range=None,
              is_angleaxis_show=True,
              is_radiusaxis_show=True,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param data:
            data of polar, [Polar radius, Polar angle, [value]]
            it is represented by a two-dimension array -> [[],[]]
        :param angle_data:
            Category data for angle, available in type: 'category' axis.
        :param radius_data:
            Category data for radius, available in type: 'category' axis.
        :param type:
            chart type，it can be 'scatter', 'effectScatter', 'barAngle', 'barRadius'
        :param symbol_size:
            symbol size
        :param start_angle:
            Starting angle of axis. 90 degrees by default, standing for top position of center.
            0 degree stands for right position of center.
        :param rotate_step:
            Rotation degree of axis label, which is especially useful when there is no enough space for category axis.
            Rotation degree is from -90 to 90.
        :param boundary_gap:
            The boundary gap on both sides of a coordinate axis.
            The setting and behavior of category axes and non-category axes are different.
            The boundaryGap of category axis can be set to either true or false.
            Default value is set to be true, in which case axisTick is served only as a separation line,
            and labels and data appear only in the center part of two axis ticks, which is called band.
        :param clockwise:
            Whether the positive position of axis is in clockwise. True for clockwise by default.
        :param is_stack:
            It specifies whether to stack category axis.
        :param axis_range:
            axis scale range
        :param is_angleaxis_show:
            whether show angle axis.
        :param is_radiusaxis_show:
            whether show radius axis.
        :param kwargs:
        """
        chart = get_all_options(**kwargs)
        polar_type = 'value' if type == "line" else "category"
        is_stack = "stack" if is_stack else ""
        self._option.get('legend')[0].get('data').append(name)
        # By defalut, axis scale range is [None, None]
        _amin, _amax = None, None
        if axis_range:
            if len(axis_range) == 2:
                _amin, _amax = axis_range
        _area_style = {"normal": chart['area_style']}
        if kwargs.get('area_color', None) is None:
            _area_style = None
        if type in ("scatter", "line"):
            self._option.get('series').append({
                "type": type,
                "name": name,
                "coordinateSystem": 'polar',
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": data,
                "label": chart['label'],
                "areaStyle": _area_style
            })
        elif type == "effectScatter":
            self._option.get('series').append({
                "type": type,
                "name": name,
                "coordinateSystem": 'polar',
                "showEffectOn": "render",
                "rippleEffect": chart['effect'],
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": data,
                "label": chart['label'],
            })
        elif type == "barRadius":
            self._option.get('series').append({
                "type": "bar",
                "stack": is_stack,
                "name": name,
                "coordinateSystem": 'polar',
                "data": data,
            })
            self._option.update(angleAxis={})
            self._option.update(
                radiusAxis={
                    "type": polar_type,
                    "data": radius_data,
                    "z": 50,
                })
        elif type == "barAngle":
            self._option.get('series').append({
                "type": "bar",
                "stack": is_stack,
                "name": name,
                "coordinateSystem": 'polar',
                "data": data,
            })
            self._option.update(radiusAxis={})
            self._option.update(
                angleAxis={
                    "type": polar_type,
                    "data": radius_data,
                    "z": 50
                })
        if type not in ("barAngle", "barRadius"):
            self._option.update(
                angleAxis={
                    "show":is_angleaxis_show,
                    "type": polar_type,
                    "data": angle_data,
                    "clockwise": clockwise,
                    "startAngle": start_angle,
                    "boundaryGap": boundary_gap,
                    "splitLine": chart['split_line'],
                    "axisLine": chart['axis_line']
                }
            )
            self._option.update(
                radiusAxis={
                    "show": is_radiusaxis_show,
                    "type": polar_type,
                    "data": radius_data,
                    "min": _amin,
                    "max": _amax,
                    "axisLine": chart['axis_line'],
                    "axisLabel": {"rotate": rotate_step}
                }
            )
        self._option.update(polar={})
        self._legend_visualmap_colorlst(**kwargs)
