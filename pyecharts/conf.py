# coding=utf-8
from __future__ import unicode_literals

import os
import json
import codecs

from pyecharts.utils import get_resource_dir
import pyecharts.constants as constants

SCRIPT_FILE_PATH = get_resource_dir('templates', 'js', 'echarts')
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
    def __init__(self, echarts_template_dir='.', jshost=SCRIPT_FILE_PATH,
                 force_js_embed=False):
        self.echarts_template_dir = echarts_template_dir
        self._jshost = remove_trailing_slashes(jshost)
        self.force_js_embed = force_js_embed

    @property
    def js_embed(self):
        """ Determine whether to use embed code in <script> tag.
        """
        if self.force_js_embed:
            return True
        else:
            return self._jshost in (
                SCRIPT_FILE_PATH, constants.DEFAULT_JUPYTER_GITHUB_URL)

    @property
    def jshost(self):
        return self._jshost

    @jshost.setter
    def jshost(self, jshost):
        self._jshost = remove_trailing_slashes(jshost)

    def get_js_library(self, pinyin):
        return DEFAULT_JS_LIBRARIES.get(pinyin, pinyin)

    def chinese_to_pinyin(self, chinese):
        return CITY_NAME_PINYIN_MAP.get(chinese, chinese)

    @staticmethod
    def read_file_contents_from_local(js_names):
        contents = []
        for name in js_names:
            path = os.path.join(SCRIPT_FILE_PATH, name + '.js')
            with codecs.open(path, 'r', encoding='utf-8') as pf:
                c = pf.read()
                contents.append(c)
        return contents

    @staticmethod
    def generate_js_link(jshost, js_names):
        return ['{}/{}.js'.format(jshost, x) for x in js_names]

    def produce_require_configuration(self, dependencies):
        """

        :param dependencies:
        :param jshost:
        :return:
        """
        _d = _ensure_echarts_is_in_the_front(dependencies)
        # if no nick name register, we treat the location as location.js
        require_conf_items = [
            "'%s': '%s/%s'" % (key,
                               self.jshost,
                               self.get_js_library(key))
            for key in _d]
        require_libraries = ["'%s'" % key for key in _d]
        return dict(
            config_items=require_conf_items,
            libraries=require_libraries
        )

    def produce_html_script_list(self, dependencies):
        """

        :param dependencies:
        :return:
        """
        _d = _ensure_echarts_is_in_the_front(dependencies)
        script_list = [
            '%s' % self.get_js_library(key)
            for key in _d]
        return script_list


def remove_trailing_slashes(jshost):
    """ Delete the end separator character if exists.

    :param jshost:
    """
    if jshost and jshost[-1] in ('/', '\\'):
        return jshost[:-1]
    else:
        return jshost


PYTHON_CONFIG = PyEchartsConfig(jshost=SCRIPT_FILE_PATH)
JUPYTER_CONFIG = PyEchartsConfig(jshost=constants.JUPYTER_LOCALHOST_URL)


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
        PYTHON_CONFIG.jshost = jshost
        JUPYTER_CONFIG.jshost = jshost
    if echarts_template_dir:
        PYTHON_CONFIG.echarts_template_dir = echarts_template_dir
        JUPYTER_CONFIG.echarts_template_dir = echarts_template_dir
    if force_js_embed is not None:
        PYTHON_CONFIG.force_js_embed = force_js_embed


def online(host=constants.DEFAULT_JUPYTER_GITHUB_URL):
    """ Set the jshost

    :param host:
    """
    configure(jshost=host)


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
