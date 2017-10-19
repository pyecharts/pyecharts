# coding=utf-8

from pyecharts.chart import Chart


class Style(Chart):

    def __init__(self, **kwargs):
        super(Style, self).__init__(title="", subtitle="", **kwargs)
        self._style = None

    def add(self, **kwargs):
        self._style = {}
        return self.__add(**kwargs)

    def __add(self, **kwargs):
        for key in kwargs:
            value = kwargs.get(key)
            if value is not None:
                self._style.update({key: value})
        return self._style
