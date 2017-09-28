#!/usr/bin/env python
# coding=utf-8

from pyecharts.option import grid
from pyecharts import template
from pyecharts.constants import PAGE_TITLE


class Grid(object):

    def __init__(self, page_title=PAGE_TITLE):
        self._chart = None
        self._js_dependencies = set()
        self._page_title = page_title

    def add(self, chart,
            grid_width=None,
            grid_height=None,
            grid_top=None,
            grid_bottom=None,
            grid_left=None,
            grid_right=None):
        """

        :param chart:
            chart instance
        :param grid_width:
            Width of grid component. Adaptive by default.
        :param grid_height:
            Height of grid component. Adaptive by default.
        :param grid_top:
            Distance between grid component and the top side of the container.
        :param grid_bottom:
            Distance between grid component and the bottom side of the container.
        :param grid_left:
            Distance between grid component and the left side of the container.
        :param grid_right:
            Distance between grid component and the right side of the container.
        :return:
        """
        if self._chart is None:
            self._chart = chart
            self._chart._option.update(grid=[])
            self._js_dependencies = chart._js_dependencies

            _grid = grid(
                grid_width, grid_height, grid_top, grid_bottom, grid_left, grid_right)
            if _grid:
                for _ in range(len(self._chart._option.get('series'))):
                    self._chart._option.get('grid').append(_grid)
        else:
            _series = (
                chart._option.get('series'),
                chart._option.get('xAxis', None),
                chart._option.get('yAxis', None),
                chart._option.get('legend')[0],
                chart._option.get('title')[0]
            )
            _index, _index_once, _xaxis, _yaxis, _legend, _title = self.__custom(_series)
            self._chart._option.get('legend').append(_legend)
            self._chart._option.get('title').append(_title)

            if _xaxis and _yaxis is not None:
                for _x in _xaxis:
                    _x.update(gridIndex=_index - 1)
                    self._chart._option.get('xAxis').append(_x)
                for _y in _yaxis:
                    _y.update(gridIndex=_index - 1)
                    self._chart._option.get('yAxis').append(_y)

                # series id is the only identify for every series
                _flag = self._chart._option.get('series')[0].get('seriesId')
                _series_index = 0
                for s in self._chart._option.get('series'):
                    if _flag == s.get('seriesId'):
                        s.update(xAxisIndex=_series_index, yAxisIndex=_series_index)
                    else:
                        _series_index += 1
                        s.update(xAxisIndex=_series_index, yAxisIndex=_series_index)
                    _flag = s.get('seriesId')

            _grid = grid(
                grid_width, grid_height, grid_top,grid_bottom, grid_left, grid_right)
            for _ in range(_index_once):
                self._chart._option.get('grid').append(_grid)
            self._js_dependencies = self._js_dependencies.union(chart._js_dependencies)

    def __custom(self, series):
        """

        :param series:
            series data
        :return:
        """
        _series, _xaxis, _yaxis, _legend, _title = series
        for s in _series:
            self._chart._option.get('series').append(s)
        return len(self._chart._option.get('series')), len(_series), \
               _xaxis, _yaxis, _legend, _title

    def render(self, path="render.html"):
        """

        :param path:
        :return:
        """
        self._chart.render(path)

    def render_embed(self):
        """

        :return:
        """
        return self._chart.render_embed()

    def show_config(self):
        """

        :return:
        """
        self._chart.show_config()

    @property
    def chart(self):
        """

        :return:
        """
        return self._chart

    @property
    def options(self):
        """

        :return:
        """
        return self._chart._option

    def _repr_html_(self):
        """

        :return:
        """
        return self._chart._repr_html_()

    def get_js_dependencies(self):
        """
        Declare its javascript dependencies for embedding purpose
        """
        return template.produce_html_script_list(self._js_dependencies)
