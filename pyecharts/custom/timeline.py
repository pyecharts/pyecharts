import pprint

class Timeline(object):

    def __init__(self, is_auto_play=False,
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
            Icon types provided by ECharts includes 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
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

        self._chart = None
        self._time_points = []
        self._timeline_options = {
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
            }},
            "options": []
        }

    def add(self, chart, time_point):
        """

        :param chart:
        :param time_point:
        :return:
        """
        self._chart = chart
        self.__check_components(chart)
        self._time_points.append(time_point)
        self._timeline_options.get('baseOption').update(
            legend=chart._option.get('legend'),
            backgroundColor=chart._option.get('backgroundColor')
        )
        self._timeline_options.get('baseOption').get('timeline').update(
            data=self._time_points
        )
        self._timeline_options.get('options').append({
            "series": chart._option.get('series'),
            "title": chart._option.get('title')
        })

    def show_config(self):
        """

        :return:
        """
        pprint.pprint(self._timeline_options)

    def render(self, path="render.html"):
        """

        :param path:
        :return:
        """
        self._chart._option = self._timeline_options
        self._chart.render(path)

    def render_embed(self):
        """

        :return:
        """
        self._chart._option = self._timeline_options
        return self._chart.render_embed()

    @property
    def chart(self):
        """

        :return:
        """
        return self._chart

    def _repr_html_(self):
        """

        :return:
        """
        return self._chart._repr_html_()

    def __check_components(self, chart):
        """

        :param chart:
        :return:
        """
        _grid = chart._option.get('grid', None)
        if _grid is not None:
            self._timeline_options.get('baseOption').update(grid=_grid)

        _xaxis = chart._option.get('xAxis', None)
        if _xaxis is not None:
            self._timeline_options.get('baseOption').update(xAxis=_xaxis)

        _yaxis = chart._option.get('yAxis', None)
        if _yaxis is not None:
            self._timeline_options.get('baseOption').update(yAxis=_yaxis)

        _polar = chart._option.get('polar', None)
        if _polar is not None:
            self._timeline_options.get('baseOption').update(polar=_polar)

        _radiusAxis = chart._option.get('radiusAxis', None)
        if _radiusAxis is not None:
            self._timeline_options.get('baseOption').update(radiusAxis=_radiusAxis)

        _angleAxis = chart._option.get('angleAxis', None)
        if _angleAxis is not None:
            self._timeline_options.get('baseOption').update(angleAxis=_angleAxis)

        _radar = chart._option.get('radar', None)
        if _radar is not None:
            self._timeline_options.get('baseOption').update(radar=_radar)

        _visualMap = chart._option.get('visualMap', None)
        if _visualMap is not None:
            self._timeline_options.get('baseOption').update(visualMap=_visualMap)

        _geo = chart._option.get('geo', None)
        if _geo is not None:
            self._timeline_options.get('baseOption').update(geo=_geo)

        _datazoom = chart._option.get('dataZoom', None)
        if _geo is not None:
            self._timeline_options.get('baseOption').update(dataZoom=_datazoom)

        _parallelAxis = chart._option.get('parallelAxis', None)
        if _parallelAxis is not None:
            self._timeline_options.get('baseOption').update(parallelAxis=_parallelAxis)
