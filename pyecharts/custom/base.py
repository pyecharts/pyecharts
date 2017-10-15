#!/usr/bin/env python
# coding=utf-8

from pyecharts import template


class BaseCustom(object):

    def __init__(self, *args, **kwargs):
        self._chart = None
        self._js_dependencies = set()

    def render(self, path="render.html"):
        """

        :param path:
        :return:
        """
        self._chart.render(path)

    def show_config(self):
        """

        :return:
        """
        self._chart.show_config()

    def render_embed(self):
        """

        :return:
        """
        return self._chart.render_embed()

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
