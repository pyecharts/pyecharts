#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals


class PyEchartsConfig(object):
    echarts_template_dir = '.'
    jshost = None  # The ropit where the js file load.
    js_embed = False  # Render js nodes in embed mode or external link mode.

    def is_remote_or_local(self):
        return self.jshost.startswith('http://') or self.jshost.startswith('https://')


DEFAULT_CONFIG = PyEchartsConfig()

# jshost 远程/本地
# 是否嵌入 js_embed
# 合并echarts_js_dependencies[_embed]
