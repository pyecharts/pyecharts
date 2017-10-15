#!/usr/bin/env python
# coding=utf-8

from pyecharts.constants import PAGE_TITLE
from pyecharts.custom.base import BaseCustom


class Overlap(BaseCustom):

    def __init__(self, page_title=PAGE_TITLE):
        super(Overlap, self).__init__()
        self._page_title = page_title

    def add(self, chart,
            xaxis_index=0,
            yaxis_index=0,
            is_add_xaxis=False,
            is_add_yaxis=False):
        """

        :param chart:
            chart instance
        :param xaxis_index:
            xAxis index
        :param yaxis_index:
            yAxis index
        :param is_add_xaxis:
            whether to add a new xaxis
        :param is_add_yaxis:
            whether to add a new yaxis
        :return:
        """
        if self._chart is None:
            self._chart = chart
            self._series_id = chart._option.get('series')[0].get('seriesId')
            self._js_dependencies = chart._js_dependencies
        else:
            _series = (
                chart._option.get('legend')[0].get('data'),
                chart._option.get('series'),
                chart._option.get('xAxis')[0],
                chart._option.get('yAxis')[0],
                is_add_xaxis,
                is_add_yaxis,
                xaxis_index,
                yaxis_index
            )
            self.__custom(_series)
            self._js_dependencies = self._js_dependencies.union(chart._js_dependencies)
        self._option = self._chart._option

    def __custom(self, series):
        """ Appends the data for the series of the chart type

        :param series:
            series data
        """
        (_name, _series, _xaxis, _yaxis, is_add_xaxis, is_add_yaxis,
         _xaxis_index, _yaxis_index) = series
        for n in _name:
            self._chart._option.get('legend')[0].get('data').append(n)
        for s in _series:
            s.update(xAxisIndex=_xaxis_index, yAxisIndex=_yaxis_index,
                     seriesId=self._series_id)
            self._chart._option.get('series').append(s)

        if is_add_xaxis:
            self._chart._option.get('xAxis').append(_xaxis)
        if is_add_yaxis:
            self._chart._option.get('yAxis').append(_yaxis)
