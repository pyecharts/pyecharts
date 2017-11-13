#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts.constants import SCRIPT_LOCAL_JSHOST, JUPYTER_LOCAL_JSHOST, DEFAULT_HOST


class PyEchartsConfig(object):
    def __init__(self, echarts_template_dir='.', jshost=None, force_js_embed=False):
        self.echarts_template_dir = echarts_template_dir
        jshost = jshost or SCRIPT_LOCAL_JSHOST
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
            return self._jshost in (SCRIPT_LOCAL_JSHOST, DEFAULT_HOST)

    @property
    def jshost(self):
        return self._jshost

    @jshost.setter
    def jshost(self, jshost):
        jshost = jshost or ''
        if jshost[-1:] in ('/', '\\'):
            jshost = jshost[:-1]
        self._jshost = jshost.rstrip('/')

    def get_current_jshost_for_script(self, jshost=None):
        if jshost:
            return jshost
        else:
            return self.jshost

    def get_current_jshost_for_jupyter(self, jshost=None):
        if jshost:
            return jshost
        else:
            if self.jshost == SCRIPT_LOCAL_JSHOST:
                return JUPYTER_LOCAL_JSHOST
            else:
                return self.jshost


CURRENT_CONFIG = PyEchartsConfig()
