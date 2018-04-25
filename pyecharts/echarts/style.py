# coding=utf-8

from pyecharts.chart import Chart


class Style(Chart):
    """
    `Style`类可用于简化配置项编写，可用于在同一个图或者多个图内保持统一的风格
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Style, self).__init__(title, subtitle, **kwargs)
        self._add_style = None
        self.init_style = {}
        for key in kwargs:
            value = kwargs.get(key)
            if value is not None:
                self.init_style.update({key: value})

    def add(self, **kwargs):
        self._add_style = {}
        return self.__add(**kwargs)

    def __add(self, **kwargs):
        for key in kwargs:
            value = kwargs.get(key)
            if value is not None:
                self._add_style.update({key: value})
        return self._add_style
