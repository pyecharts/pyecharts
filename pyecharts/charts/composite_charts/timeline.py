# coding=utf-8

import copy

from ...charts.base import Base
from ...consts import PAGE_TITLE

# from pyecharts.commons.utils import merge_js_dependencies


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
        play_interval=2000,
        symbol="emptyCircle",
        symbol_size=10,
        pos_left="auto",
        pos_right="auto",
        pos_top="auto",
        pos_bottom="atuo",
    ):
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
                    "symbol": symbol,
                    "symbolSize": symbol_size,
                    "playInterval": play_interval,
                    "left": pos_left,
                    "right": pos_right,
                    "top": pos_top,
                    "bottom": pos_bottom,
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
        # self._js_dependencies = merge_js_dependencies(
        #     self._js_dependencies, chart.js_dependencies
        # )
        self.__check_components(chart)
        self._time_points.append(time_point)
        self._option.get("baseOption").update(
            backgroundColor=chart_options.get("backgroundColor")
        )
        self._option.get("baseOption").get("timeline").update(data=self._time_points)
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
