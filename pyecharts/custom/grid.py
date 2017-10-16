#!/usr/bin/env python
# coding=utf-8
import copy

from pyecharts.option import grid
from pyecharts.constants import PAGE_TITLE
from pyecharts.base import Base


class Grid(Base):

    def __init__(self, page_title=PAGE_TITLE):
        super(Grid, self).__init__()
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
            Distance between grid component and the top of the container.
        :param grid_bottom:
            Distance between grid component and the bottom of the container.
        :param grid_left:
            Distance between grid component and the left side of the container.
        :param grid_right:
            Distance between grid component and the right of the container.
        :return:
        """
        if not self._option:
            self._option = copy.deepcopy(chart.options)
            self._option.update(grid=[])
            self._js_dependencies = chart.js_dependencies

            _grid = grid(
                grid_width, grid_height,
                grid_top, grid_bottom, grid_left, grid_right)
            if _grid:
                for _ in range(len(self._option.get('series'))):
                    self._option.get('grid').append(_grid)
        else:
            _series = (
                chart._option.get('series'),
                chart._option.get('xAxis', None),
                chart._option.get('yAxis', None),
                chart._option.get('legend')[0],
                chart._option.get('title')[0]
            )
            (_index, _index_once, _xaxis,
             _yaxis, _legend, _title) = self.__custom(_series)
            self._option.get('legend').append(_legend)
            self._option.get('title').append(_title)

            if _xaxis and _yaxis is not None:
                for _x in _xaxis:
                    _x.update(gridIndex=_index - 1)
                    self._option.get('xAxis').append(_x)
                for _y in _yaxis:
                    _y.update(gridIndex=_index - 1)
                    self._option.get('yAxis').append(_y)

                # series id is the only identify for every series
                _flag = self._option.get('series')[0].get('seriesId')
                _series_index = 0
                for s in self._option.get('series'):
                    if _flag == s.get('seriesId'):
                        s.update(xAxisIndex=_series_index,
                                 yAxisIndex=_series_index)
                    else:
                        _series_index += 1
                        s.update(xAxisIndex=_series_index,
                                 yAxisIndex=_series_index)
                    _flag = s.get('seriesId')

            _grid = grid(
                grid_width, grid_height,
                grid_top, grid_bottom, grid_left, grid_right)
            for _ in range(_index_once):
                self._option.get('grid').append(_grid)
            self._js_dependencies = self._js_dependencies.union(
                chart.js_dependencies)

    def __custom(self, series):
        """

        :param series:
            series data
        :return:
        """
        _series, _xaxis, _yaxis, _legend, _title = series
        for s in _series:
            self._option.get('series').append(s)
        return len(self._option.get('series')), len(_series), \
               _xaxis, _yaxis, _legend, _title
