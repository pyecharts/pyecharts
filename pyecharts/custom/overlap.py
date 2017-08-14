#!/usr/bin/env python
# coding=utf-8


class Overlap(object):

    def __init__(self):
        self._chart = None

    def add(self, chart):
        """

        :param chart:
            chart instance
        :return:
        """
        if self._chart is None:
            self._chart = chart
        else:
            self.__custom(self.__get_series(chart))

    def __get_series(self, chart):
        """ Get chart series data

        :param chart:
            chart instance
        :return:
        """
        return (
            chart._option.get('legend')[0].get('data'),
            chart._option.get('series'),
        )

    def __custom(self, series):
        """ Appends the data for the series of the chart type

        :param series:
            series data
        """
        _name, _series = series
        for n in _name:
            self._chart._option.get('legend')[0].get('data').append(n)
        for s in _series:
            self._chart._option.get('series').append(s)

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
