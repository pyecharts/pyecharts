#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Polar(Base):
    """
    <<< 极坐标系 >>>
    可以用于散点图和折线图。
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
              **kwargs):
        """

        :param name:
            图例名称
        :param data:
            数据项 [极径，极角 [数据值]]
        :param angle_data:
            角度类目数据
        :param radius_data:
            半径类目数据
        :param type:
            图例类型，有'scatter', 'effectScatter', 'barAngle', 'barRadius'可选
        :param symbol_size:
            标记图形大小
        :param start_angle:
            起始刻度的角度，默认为 90 度，即圆心的正上方。0 度为圆心的正右方
        :param rotate_step:
            刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠
            旋转的角度从 -90 度到 90 度
        :param boundary_gap:
            坐标轴两边留白策略
            类目轴中 boundaryGap 可以配置为 True 和 False
            默认为 true，这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)中间
        :param clockwise:
            刻度增长是否按顺时针，默认顺时针
        :param is_stack:
            数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置
        :param axis_range:
            坐标轴刻度范围。
        :param kwargs:
        """
        chart = get_all_options(**kwargs)
        polar_type = 'value' if type == "line" else "category"
        is_stack = "stack" if is_stack else ""
        self._option.get('legend').get('data').append(name)
        # 坐标轴刻度范围默认为 [None, None]
        _amin, _amax = None, None
        if axis_range:
            if len(axis_range) == 2:
                _amin, _amax = axis_range
        if type in ("scatter", "line"):
            self._option.get('series').append({
                "type": type,
                "name": name,
                "coordinateSystem": 'polar',
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": data,
                "label": chart['label'],
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
