# coding=utf-8
from __future__ import unicode_literals

import os
import json
import codecs
import warnings

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
        if jshost is None or jshost == SCRIPT_LOCAL_JSHOST:
            # Replace the path in site-packages with the path in nbextension.
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

    @staticmethod
    def produce_require_configuration(dependencies, jshost):
        """

        :param dependencies:
        :param jshost:
        :return:
        """
        _d = _ensure_echarts_is_in_the_front(dependencies)
        # if no nick name register, we treat the location as location.js
        require_conf_items = [
            "'%s': '%s/%s'" % (key,
                               jshost,
                               CURRENT_CONFIG.get_js_library(key))
            for key in _d]
        require_libraries = ["'%s'" % key for key in _d]
        return dict(
            config_items=require_conf_items,
            libraries=require_libraries
        )

    @staticmethod
    def produce_html_script_list(dependencies):
        """

        :param dependencies:
        :return:
        """
        _d = _ensure_echarts_is_in_the_front(dependencies)
        script_list = [
            '%s' % CURRENT_CONFIG.get_js_library(key)
            for key in _d]
        return script_list


CURRENT_CONFIG = PyEchartsConfig()


def configure(jshost=None,
              echarts_template_dir=None,
              force_js_embed=None,
              **kwargs):
    """ Config all items for pyecharts when use chart.render()
    or page.render().

    :param jshost:
    :param echarts_template_dir:
    :param force_js_embed:
    :param kwargs:
    """
    if jshost:
        CURRENT_CONFIG.jshost = jshost
    if echarts_template_dir:
        CURRENT_CONFIG.echarts_template_dir = echarts_template_dir
    if force_js_embed is not None:
        CURRENT_CONFIG.force_js_embed = force_js_embed


def online(host=constants.DEFAULT_HOST):
    """ Set the jshost

    :param host:
    """
    warnings.warn(
        "Deprecated since 0.3.0! Please use pyecharts.configure() instead.")
    CURRENT_CONFIG.jshost = host


def _ensure_echarts_is_in_the_front(dependencies):
    """ make sure echarts is the item in the list
    require(['echarts'....], function(ec) {..}) need it to
    be first but dependencies is a set so has no sequence

    :param dependencies:
    :return:
    """
    if len(dependencies) > 1:
        dependencies.remove('echarts')
        dependencies = ['echarts'] + list(dependencies)
    elif len(dependencies) == 1:
        # make a new list
        dependencies = list(dependencies)
    else:
        raise Exception("No js library found. Nothing works!")
    return dependencies
