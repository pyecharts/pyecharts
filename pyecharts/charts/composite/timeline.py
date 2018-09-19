# coding=utf-8

import copy

from pyecharts.base import Base
from pyecharts.constants import PAGE_TITLE
from pyecharts.utils import merge_js_dependencies


class Timeline(Base):
    """
    <<< 时间线轮播多张图 >>>
    """

    def __init__(
        self,
        page_title=PAGE_TITLE,
        width=800,
        height=400,
        is_auto_play=False,
        is_loop_play=True,
        is_rewind_play=False,
        is_timeline_show=True,
        timeline_play_interval=2000,
        timeline_symbol="emptyCircle",
        timeline_symbol_size=10,
        timeline_left="auto",
        timeline_right="auto",
        timeline_top="auto",
        timeline_bottom="atuo",
    ):
        """

        :param is_auto_play:
            是否自动播放，默认为 Flase
        :param is_loop_play:
            是否循环播放，默认为 True
        :param is_rewind_play:
            是否方向播放，默认为 Flase
        :param is_timeline_show:
            是否显示 timeline 组件。默认为 True，如果设置为false，不会显示，但是功能还存在。
        :param timeline_play_interval:
            播放的速度（跳动的间隔），单位毫秒（ms）。
        :param timeline_symbol:
            标记的图形。有'circle', 'rect', 'roundRect', 'triangle', 'diamond',
            'pin', 'arrow'可选
        :param timeline_symbol_size:
            标记的图形大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示
            宽和高，例如 [20, 10] 表示标记宽为 20，高为 10。
        :param timeline_left:
            timeline 组件离容器左侧的距离。
            left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
            也可以是 'left', 'center', 'right'。如果 left 的值为'left', 'center',
            'right'，组件会根据相应的位置自动对齐。
        :param timeline_right:
            timeline 组件离容器右侧的距离。同 left
        :param timeline_top:
            timeline 组件离容器顶侧的距离。同 left
        :param timeline_bottom:
            timeline 组件离容器底侧的距离。同 left
        """

        super(Timeline, self).__init__(width=width, height=height)
        self._page_title = page_title
        self._time_points = []
        self._option = {
            "baseOption": {
                "timeline": {
                    "axisType": "category",
                    "autoPlay": is_auto_play,
                    "loop": is_loop_play,
                    "rewind": is_rewind_play,
                    "show": is_timeline_show,
                    "symbol": timeline_symbol,
                    "symbolSize": timeline_symbol_size,
                    "playInterval": timeline_play_interval,
                    "left": timeline_left,
                    "right": timeline_right,
                    "top": timeline_top,
                    "bottom": timeline_bottom,
                },
                "series": [],
            },
            "options": [],
        }

    def add(self, chart, time_point):
        """

        :param chart:
            图形实例
        :param time_point:
            指定时间点
        """
        chart_options = chart.get_options(remove_none=False)
        self._js_dependencies = merge_js_dependencies(
            self._js_dependencies, chart.js_dependencies
        )
        self.__check_components(chart)
        self._time_points.append(time_point)
        self._option.get("baseOption").update(
            backgroundColor=chart_options.get("backgroundColor")
        )
        self._option.get("baseOption").get("timeline").update(
            data=self._time_points
        )
        self._option.get("options").append(
            {
                "color": chart_options.get("color"),
                "legend": chart_options.get("legend"),
                "series": chart_options.get("series"),
                "title": chart_options.get("title"),
                "tooltip": chart_options.get("tooltip"),
            }
        )
        _tmp_series = copy.deepcopy(chart_options.get("series"))
        for _s in _tmp_series:
            if _s.get("type") == "map":
                _s.pop("data", None)
                self._option.get("baseOption").get("series").append(_s)
        return self

    def __check_components(self, chart):
        """

        :param chart:
            图形实例
        """
        chart_options = chart.get_options(remove_none=False)
        _compoents = [
            "grid",
            "xAxis",
            "yAxis",
            "polar",
            "radiusAxis",
            "geo",
            "angleAxis",
            "radar",
            "visualMap",
            "dataZoom",
            "parallelAxis",
        ]

        for component in _compoents:
            _c = chart_options.get(component, None)
            if _c is not None:
                self._option.get("baseOption").update({component: _c})
