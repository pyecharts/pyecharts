# coding=utf-8
from __future__ import unicode_literals

import os
import json
import codecs

from pyecharts.utils import get_resource_dir
import pyecharts.constants as constants

SCRIPT_LOCAL_JSHOST = get_resource_dir('templates', 'js', 'echarts')
# Path constants for template dir

DEFAULT_TEMPLATE_DIR = get_resource_dir('templates')
DEFAULT_ECHARTS_REGISTRY = os.path.join(
    get_resource_dir('templates'), 'js', 'echarts', 'registry.json')
# Load js & map file index into a dictionary.


with codecs.open(DEFAULT_ECHARTS_REGISTRY, 'r', 'utf-8') as f:
    content = f.read()
    CONFIG = json.loads(content)

DEFAULT_JS_LIBRARIES = CONFIG['FILE_MAP']  # {<Pinyin>:<Js File Name>}
CITY_NAME_PINYIN_MAP = CONFIG['PINYIN_MAP']  # {<Chinese Name>:<Pinyin>}


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
            return self._jshost in (
                SCRIPT_LOCAL_JSHOST, constants.DEFAULT_HOST)

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
            return constants.JUPYTER_LOCAL_JSHOST
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

    def get_js_library(self, pinyin):
        return DEFAULT_JS_LIBRARIES.get(pinyin, pinyin)

    def chinese_to_pinyin(self, chinese):
        return CITY_NAME_PINYIN_MAP.get(chinese, chinese)

    @staticmethod
    def merge_js_dependencies(*args):
        """ Merge js dependencies to a list

        :param args:
        :return:
        """
        dependencies = []

        def _add(_x):
            if _x not in dependencies:
                dependencies.append(_x)

        for a in args:
            if hasattr(a, 'js_dependencies'):
                for d in a.js_dependencies:
                    _add(d)
            else:
                _add(a)
        if len(dependencies) > 1:
            dependencies.remove('echarts')
            dependencies = ['echarts'] + list(dependencies)
        return dependencies

    @staticmethod
    def read_file_contents_from_local(js_names):
        contents = []
        for name in js_names:
            path = os.path.join(SCRIPT_LOCAL_JSHOST, name + '.js')
            with open(path, 'rb') as f:
                c = f.read()
                contents.append(c.decode('utf8'))
        return contents

    @staticmethod
    def generate_js_link(jshost, js_names):
        return ['{}/{}.js'.format(jshost, x) for x in js_names]


CURRENT_CONFIG = PyEchartsConfig()
