# coding=utf-8

from pyecharts.chart import Chart


class Polar(Chart):
    """
    <<< 极坐标系 >>>

    可以用于散点图和折线图。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Polar, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(
        self,
        name,
        data,
        angle_data=None,
        radius_data=None,
        type="line",
        symbol_size=4,
        start_angle=90,
        rotate_step=0,
        boundary_gap=True,
        is_clockwise=True,
        is_stack=False,
        axis_range=None,
        is_angleaxis_show=True,
        is_radiusaxis_show=True,
        radiusaxis_z_index=50,
        angleaxis_z_index=50,
        render_item=None,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param data:
            数据项 [极径，极角 [数据值]]。
        :param angle_data:
            角度类目数据。
        :param radius_data:
            半径类目数据。
        :param type:
            图例类型，有'line', 'scatter', 'effectScatter', 'barAngle', 'barRadius'
            可选。默认为 'line'。
        :param symbol_size:
            标记图形大小，默认为 4。
        :param start_angle:
            起始刻度的角度，默认为 90 度，即圆心的正上方。0 度为圆心的正右方。
        :param rotate_step:
            刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠
            旋转的角度从 -90 度到 90 度。默认为 0
        :param boundary_gap:
            坐标轴两边留白策略
            默认为 True，这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)中间。
        :param is_clockwise:
            刻度增长是否按顺时针，默认 True
        :param is_stack:
            数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置。
        :param axis_range:
            坐标轴刻度范围。默认值为 [None, None]。
        :param is_angleaxis_show:
            是否显示极坐标系的角度轴，默认为 True。
        :param is_radiusaxis_show:
            是否显示极坐标系的径向轴，默认为 True。
        :param radiusaxis_z_index:
            radius 轴的 z 指数，默认为 50
        :param angleaxis_z_index:
            angel 轴的 z 指数，默认为 50
        :param render_item:
            开发者自己提供图形渲染的逻辑
        :param kwargs:
        """
        chart = self._get_all_options(**kwargs)
        polar_type = "value" if type == "line" else "category"
        is_stack = "stack" if is_stack else ""
        self._option.get("legend")[0].get("data").append(name)

        _amin, _amax = None, None
        if axis_range:
            if len(axis_range) == 2:
                _amin, _amax = axis_range

        _area_style = chart["area_style"]
        if kwargs.get("area_color", None) is None:
            _area_style = None

        if type in ("scatter", "line"):
            self._option.get("series").append(
                {
                    "type": type,
                    "name": name,
                    "coordinateSystem": "polar",
                    "symbol": chart["symbol"],
                    "symbolSize": symbol_size,
                    "data": data,
                    "label": chart["label"],
                    "areaStyle": _area_style,
                }
            )

        elif type == "effectScatter":
            self._option.get("series").append(
                {
                    "type": type,
                    "name": name,
                    "coordinateSystem": "polar",
                    "showEffectOn": "render",
                    "rippleEffect": chart["effect"],
                    "symbol": chart["symbol"],
                    "symbolSize": symbol_size,
                    "data": data,
                    "label": chart["label"],
                }
            )

        elif type == "barRadius":
            self._option.get("series").append(
                {
                    "type": "bar",
                    "stack": is_stack,
                    "name": name,
                    "coordinateSystem": "polar",
                    "data": data,
                }
            )
            self._option.update(angleAxis={})
            self._option.update(
                radiusAxis={
                    "type": polar_type,
                    "data": radius_data,
                    "z": radiusaxis_z_index,
                }
            )

        elif type == "barAngle":
            self._option.get("series").append(
                {
                    "type": "bar",
                    "stack": is_stack,
                    "name": name,
                    "coordinateSystem": "polar",
                    "data": data,
                }
            )
            self._option.update(radiusAxis={"show": is_radiusaxis_show})
            self._option.update(
                angleAxis={
                    "show": is_angleaxis_show,
                    "type": polar_type,
                    "data": radius_data,
                    "z": angleaxis_z_index,
                    "startAngle": start_angle,
                    "splitLine": chart["split_line"],
                }
            )

        elif type == "custom":
            assert render_item is not None
            self._option.get("series").append(
                {
                    "type": "custom",
                    "name": name,
                    "coordinateSystem": "polar",
                    "data": data,
                    "renderItem": render_item,
                }
            )

        if type not in ("barAngle", "barRadius"):
            self._option.update(
                angleAxis={
                    "show": is_angleaxis_show,
                    "type": polar_type,
                    "data": angle_data,
                    "clockwise": is_clockwise,
                    "startAngle": start_angle,
                    "boundaryGap": boundary_gap,
                    "splitLine": chart["split_line"],
                    "axisLine": chart["axis_line"],
                }
            )
            self._option.update(
                radiusAxis={
                    "show": is_radiusaxis_show,
                    "type": polar_type,
                    "data": radius_data,
                    "min": _amin,
                    "max": _amax,
                    "axisLine": chart["axis_line"],
                    "axisLabel": {"rotate": rotate_step},
                    "z": radiusaxis_z_index,
                }
            )
        self._option.update(polar={})
        self._config_components(**kwargs)
