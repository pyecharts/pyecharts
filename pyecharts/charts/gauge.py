# coding=utf-8

from pyecharts.chart import Chart

DEFAULT_GAUGE_TOOLTIP_FORMATTER = "{a} <br/>{b} : {c}%"


class Gauge(Chart):
    """
    <<< 仪表盘 >>>
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Gauge, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self, name, attr, value, scale_range=None, angle_range=None, **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param scale_range:
            仪表盘数据范围。默认为 [0, 100]。
        :param angle_range:
            仪表盘角度范围。默认为 [225, -45]。
        :param kwargs:
        """
        kwargs.update(type="gauge")
        if "tooltip_formatter" not in kwargs:
            kwargs["tooltip_formatter"] = DEFAULT_GAUGE_TOOLTIP_FORMATTER
        _min, _max = 0, 100
        if scale_range:
            if len(scale_range) == 2:
                _min, _max = scale_range

        _start, _end = 225, -45
        if angle_range:
            if len(angle_range) == 2:
                _start, _end = angle_range

        self._option.get("legend")[0].get("data").append(name)

        self._option.get("series").append(
            {
                "type": "gauge",
                "detail": {"formatter": "{value}%"},
                "name": name,
                "min": _min,
                "max": _max,
                "startAngle": _start,
                "endAngle": _end,
                "data": [{"value": value, "name": attr}],
            }
        )
        self._config_components(**kwargs)
