# coding=utf-8

from pyecharts.constants import PAGE_TITLE
from pyecharts.base import Base


class Timeline(Base):

    def __init__(self, page_title=PAGE_TITLE,
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
                 timeline_bottom="atuo"):
        """

        :param is_auto_play:
            Whether to play automatically.
        :param is_loop_play:
            Whether to loop playing.
        :param is_rewind_play:
            Whether supports playing reversely.
        :param is_timeline_show:
            Whether to show the timeline component.
            It would not show with a setting of false, but its functions still remain.
        :param timeline_play_interval:
            Indicates play speed (gap time between two state), whose unit is millisecond.
        :param timeline_symbol:
            Symbol of timeline.
            Icon types provided by ECharts includes 'circle', 'rect', 'roundRect', 'triangle',
            'diamond', 'pin', 'arrow'
        :param timeline_symbol_size:
            timeline symbol size.
            It can be set to single numbers like 10, or use an array to represent width and height.
            For example, [20, 10] means symbol width is 20, and height is10.
        :param timeline_left:
            Distance between timeline component and the left side of the container.
        :param timeline_right:
            Distance between timeline component and the right side of the container.
        :param timeline_top:
            Distance between timeline component and the top side of the container.
        :param timeline_bottom:
            Distance between timeline component and the bottom side of the container.
        """

        super(Timeline, self).__init__(
            width=width, height=height
        )
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
                    "bottom": timeline_bottom
                }
            },
            "options": []
        }

    def add(self, chart, time_point):
        """

        :param chart:
        :param time_point:
        :return:
        """
        self._js_dependencies = self._js_dependencies.union(
            chart.get_js_dependencies())
        self.__check_components(chart)
        self._time_points.append(time_point)
        self._option.get('baseOption').update(
            legend=chart.options.get('legend'),
            backgroundColor=chart.options.get('backgroundColor')
        )
        self._option.get('baseOption').get('timeline').update(
            data=self._time_points
        )
        self._option.get('options').append({
            "series": chart.options.get('series'),
            "title": chart.options.get('title')
        })

    def __check_components(self, chart):
        """

        :param chart:
        :return:
        """
        _compoents = [
            'gird', 'xAxis', 'yAxis', 'polar', 'radiusAxis', 'geo'
            'angleAxis', 'radar', 'visualMap', 'dataZoom', 'parallelAxis'
        ]

        for component in _compoents:
            _c = chart.options.get(component, None)
            if _c is not None:
                self._option.get('baseOption').update({component: _c})
