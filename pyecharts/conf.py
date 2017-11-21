#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts.constants import SCRIPT_LOCAL_JSHOST, JUPYTER_LOCAL_JSHOST, \
    DEFAULT_HOST


class PyEchartsConfig(object):

    def __init__(self, echarts_template_dir='.', jshost=None,
                 force_js_embed=False):
        self.echarts_template_dir = echarts_template_dir
        jshost = jshost or SCRIPT_LOCAL_JSHOST
        self._jshost = PyEchartsConfig.convert_jshost_string(jshost)
        self.force_js_embed = force_js_embed

    @property
    def js_embed(self):
        """ Determine whether to use embed code in <script> tag.
        """
        if self.force_js_embed:
            return True
        else:
            return self._jshost in (SCRIPT_LOCAL_JSHOST, DEFAULT_HOST)

    @property
    def jshost(self):
        return self._jshost

    @jshost.setter
    def jshost(self, jshost):
        self._jshost = PyEchartsConfig.convert_jshost_string(jshost)

    def get_current_jshost_for_script(self, jshost=None):
        """
        :param jshost:
        """
        if jshost:
            return jshost
        else:
            return self.jshost

    def get_current_jshost_for_jupyter(self, jshost=None):
        """ Get actual jshost in jupyter.

        :param jshost:
        """
        jshost = jshost or self.jshost
        if jshost == SCRIPT_LOCAL_JSHOST:
            return JUPYTER_LOCAL_JSHOST
        else:
            return jshost

    @staticmethod
    def convert_jshost_string(jshost):
        """ Delete the end separator character if exists.

        :param jshost:
        """
        jshost = jshost or ''
        if jshost[-1:] in ('/', '\\'):
            jshost = jshost[:-1]
        return jshost
