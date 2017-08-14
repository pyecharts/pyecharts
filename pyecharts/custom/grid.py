#!/usr/bin/env python
# coding=utf-8

from pyecharts.option import grid

class Grid(object):

    def __init__(self):
        self._chart = None

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

            _grid = grid(grid_width, grid_height, grid_top, grid_bottom, grid_left, grid_right)
            if _grid:
                for _ in range(len(self._chart._option.get('series'))):
                    self._chart._option.get('grid').append(_grid)
        else:
            _index, _index_once, _xaxis, _yaxis, _legned, _title = self.__custom(self.__get_series(chart))
            self._chart._option.get('legend').append(_legned)
            self._chart._option.get('title').append(_title)
            if _xaxis and _yaxis is not None:
                try:
                    _xaxis[0].update(gridIndex=_index - 1)
                    _yaxis[0].update(gridIndex=_index - 1)
                    self._chart._option.get('xAxis').append(_xaxis[0])
                    self._chart._option.get('yAxis').append(_yaxis[0])
                except:
                    pass

                # indexflag is only identify for every series
                _flag = self._chart._option.get('series')[0].get('indexflag')
                _series_index = 0
                for s in self._chart._option.get('series'):
                    if _flag == s.get('indexflag'):
                        s.update(xAxisIndex=_series_index, yAxisIndex=_series_index)
                    else:
                        _series_index += 1
                        s.update(xAxisIndex=_series_index, yAxisIndex=_series_index)
                    _flag = s.get('indexflag')
            _grid = grid(grid_width, grid_height, grid_top, grid_bottom, grid_left, grid_right)
            for _ in range(_index_once):
                self._chart._option.get('grid').append(_grid)

    def __get_series(self, chart):
        """ Get chart series data """
        return (
            chart._option.get('legend')[0].get('data'),
            chart._option.get('series'),
            chart._option.get('xAxis', None),
            chart._option.get('yAxis', None),
            chart._option.get('legend')[0],
            chart._option.get('title')[0]
        )

    def __custom(self, series):
        """

        :param series:
            series data
        :return:
        """
        _name, _series, _xaxis, _yaxis, _legend, _title = series
        for s in _series:
            self._chart._option.get('series').append(s)
        return len(self._chart._option.get('series')), len(_series), _xaxis, _yaxis, _legend, _title

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
        import pprint
        return pprint.pprint(self._chart._option)

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
