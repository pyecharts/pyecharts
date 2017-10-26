#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals


class PyEchartsConfig(object):
    echarts_template_dir = '.'
    jshost = None

    def is_remote_or_local(self):
        return self.jshost.startswith('http://') or self.jshost.startswith('https://')


DEFAULT_CONFIG = PyEchartsConfig()
