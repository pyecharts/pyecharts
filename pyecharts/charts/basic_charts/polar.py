# coding=utf-8

from ...charts.chart import Chart
from ...options import (
    AreaStyleOpts,
    AxisLineOpts,
    EffectOpts,
    InitOpts,
    LabelOpts,
    SplitLineOpts,
)
from ...types import *


class Polar(Chart):
    """
    <<< 极坐标系 >>>

    可以用于散点图和折线图。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        data: ListTuple,
        angle_data=None,
        radius_data=None,
        type_="line",
        symbol_size=4,
        start_angle=90,
        boundary_gap=True,
        is_clockwise=True,
        is_stack=False,
        axis_range=None,
        is_angleaxis_show=True,
        is_radiusaxis_show=True,
        radiusaxis_z_index=50,
        angleaxis_z_index=50,
        render_item=None,
        symbol=None,
        label_opts: LabelOpts = LabelOpts(),
        areastyle_opts: AreaStyleOpts = AreaStyleOpts(),
        axisline_opts: AxisLineOpts = AxisLineOpts(),
        splitline_opts: SplitLineOpts = SplitLineOpts(),
        effect_opts: EffectOpts = EffectOpts(),
        axislabel_opts: LabelOpts = LabelOpts(),
    ):

        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(areastyle_opts, AreaStyleOpts):
            areastyle_opts = areastyle_opts.opts
        if isinstance(axisline_opts, AxisLineOpts):
            axisline_opts = axisline_opts.opts
        if isinstance(splitline_opts, SplitLineOpts):
            splitline_opts = splitline_opts.opts
        if isinstance(effect_opts, EffectOpts):
            effect_opts = effect_opts.opts
        if isinstance(axislabel_opts, LabelOpts):
            axislabel_opts = axislabel_opts.opts

        polar_type = "value" if type == "line" else "category"
        is_stack = "stack" if is_stack else ""
        self._append_legend(name)

        _amin, _amax = None, None
        if axis_range:
            if len(axis_range) == 2:
                _amin, _amax = axis_range

        # _area_style = chart["area_style"]
        if kwargs.get("area_color", None) is None:
            _area_style = None

        _bar_type_series = {
            "type": "bar",
            "coordinateSystem": "polar",
            "stack": is_stack,
            "name": name,
            "data": data,
        }

        _radius_axis_opt = {
            "show": is_radiusaxis_show,
            "type": polar_type,
            "data": radius_data,
            "min": _amin,
            "max": _amax,
            "axisLine": axisline_opts,
            "axisLabel": axislabel_opts,
            "z": radiusaxis_z_index,
        }

        _angle_axis_opt = {
            "show": is_angleaxis_show,
            "type": polar_type,
            "data": angle_data,
            "clockwise": is_clockwise,
            "startAngle": start_angle,
            "boundaryGap": boundary_gap,
            "splitLine": splitline_opts,
            "axisLine": axisline_opts,
            "axisLabel": axislabel_opts,
            "z": angleaxis_z_index,
        }

        if type in ("scatter", "line"):
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": name,
                    "coordinateSystem": "polar",
                    "symbol": symbol,
                    "symbolSize": symbol_size,
                    "data": data,
                    "label": label_opts,
                    "areaStyle": areastyle_opts,
                }
            )

        elif type == "effectScatter":
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": name,
                    "coordinateSystem": "polar",
                    "showEffectOn": "render",
                    "rippleEffect": effect_opts,
                    "symbol": symbol,
                    "symbolSize": symbol_size,
                    "data": data,
                    "label": label_opts,
                }
            )

        elif type == "barRadius":
            self.options.get("series").append(_bar_type_series)
            self.options.update(angleAxis={})
            self.options.update(radiusAxis=_radius_axis_opt)

        elif type == "barAngle":
            self.options.get("series").append(_bar_type_series)
            self.options.update(radiusAxis={"show": is_radiusaxis_show})
            self.options.update(angleAxis=_angle_axis_opt)

        elif type == "custom":
            assert render_item is not None
            self.options.get("series").append(
                {
                    "type": "custom",
                    "name": name,
                    "coordinateSystem": "polar",
                    "data": data,
                    "renderItem": render_item,
                }
            )

        if type not in ("barAngle", "barRadius"):
            self.options.update(angleAxis=_angle_axis_opt)
            self.options.update(radiusAxis=_radius_axis_opt)
        self.options.update(polar={})
