# coding=utf-8

from pyecharts.chart import Chart


class Liquid(Chart):
    """
    <<< 水球图 >>>

    主要用来突出数据的百分比。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Liquid, self).__init__(title, subtitle, **kwargs)
        self._js_dependencies.add("liquidfill")

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        data,
        shape="circle",
        liquid_color=None,
        is_liquid_animation=True,
        is_liquid_outline_show=True,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param data:
            数据项, 如：[0.6, 0.5, 0.4, 0.3]: 表示水波的高度分别在 60%,
            50%, 40%, 和 30% 处。
        :param shape:
            水球外形，有'circle', 'rect', 'roundRect', 'triangle', 'diamond',
            'pin', 'arrow'可选。默认'circle'。
        :param liquid_color:
            波浪颜色，默认的颜色列表为['#294D99', '#156ACF', '#1598ED', '#45BDFF']。
        :param is_liquid_animation:
            是否显示波浪动画，默认为 True。
        :param is_liquid_outline_show:
            是否显示边框，默认为 True。
        """
        _animation_dur, _animation_dur_update = 2000, 1000
        if not is_liquid_animation:
            _animation_dur, _animation_dur_update = 0, 0

        _color = ["#294D99", "#156ACF", "#1598ED", "#45BDFF"]
        if liquid_color:
            _color = liquid_color

        self._option.get("series").append(
            {
                "type": "liquidFill",
                "name": name,
                "data": data,
                "waveAnimation": is_liquid_animation,
                "animationDuration": _animation_dur,
                "animationDurationUpdate": _animation_dur_update,
                "color": _color,
                "shape": shape,
                "outline": {"show": is_liquid_outline_show},
            }
        )
        self._config_components(**kwargs)
