#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts.utils import get_resource_dir


class PyEchartsConfig(object):
    def __init__(self, echarts_template_dir='.', jshost=None, force_js_embed=False):
        self.echarts_template_dir = echarts_template_dir
        jshost = jshost or get_resource_dir('templates', 'js', 'echarts')
        if jshost[-1:] in ('/', '\\'):
            jshost = jshost[:-1]
        self._jshost = jshost.rstrip('/')
        self.force_js_embed = force_js_embed

    def is_remote_or_local(self):
        return self._jshost.startswith('http://') or self._jshost.startswith('https://')

    @property
    def js_embed(self):
        if self.force_js_embed:
            return True
        else:
            return not self.is_remote_or_local()

    @property
    def jshost(self):
        return self._jshost

    @jshost.setter
    def jshost(self, jshost):
        jshost = jshost or ''
        if jshost[-1:] in ('/', '\\'):
            jshost = jshost[:-1]
        self._jshost = jshost.rstrip('/')

    def generate_js_link(self, names):
        return ['{}/{}.js'.format(self._jshost, x) for x in names]


CURRENT_CONFIG = PyEchartsConfig()
