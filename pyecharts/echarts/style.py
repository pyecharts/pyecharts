# coding=utf-8

import warnings

from pyecharts.chart import Chart


class Style(Chart):
    """
    `Style`类可用于简化配置项编写，可用于在同一个图或者多个图内保持统一的风格
    """

    def __init__(self, title="", subtitle="", **kwargs):
        warnings.warn("The class Style is deprecated.", DeprecationWarning)
        super(Style, self).__init__(title, subtitle, **kwargs)
        self._add_style = None
        self.init_style = {k: v for k, v in kwargs.items() if v is not None}

    def add(self, **kwargs):
        self._add_style = {}
        return self.__add(**kwargs)

    def __add(self, **kwargs):
        self._add_style = {k: v for k, v in kwargs.items() if v is not None}
        return self._add_style
