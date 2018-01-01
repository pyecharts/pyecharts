# coding=utf-8
from __future__ import unicode_literals

import os
import json
import codecs

from pyecharts.utils import get_resource_dir
import pyecharts.constants as constants

PYECHARTS_DIR = '.pyecharts'
# Path constants for template dir

DEFAULT_TEMPLATE_DIR = get_resource_dir('templates')
DEFAULT_ECHARTS_REGISTRY = os.path.join(
    get_resource_dir('templates'), 'js', 'echarts', 'registry.json')
# Load js & map file index into a dictionary.

DEFAULT_JS_LIBRARIES = []
CITY_NAME_PINYIN_MAP = {}  # {<Chinese Name>:<Pinyin>}


def _get_pyecharts_dir():
    user_home = os.path.expanduser('~')
    package_home = os.path.join(user_home, PYECHARTS_DIR)
    return package_home


def read_a_map_registry(registry_json):
    with codecs.open(registry_json, 'r', 'utf-8') as f:
        content = f.read()
        return json.loads(content)


def read_all_registries(global_conf, pinyin_db):
    pyecharts_dir = _get_pyecharts_dir()
    registries = [DEFAULT_ECHARTS_REGISTRY]
    for adir in os.listdir(pyecharts_dir):
        registries.append(
            os.path.join(pyecharts_dir, adir, 'dist', 'config.json'))
    for registry_json in registries:
        config = read_a_map_registry(registry_json)
        config['LOCAL_PATH'] = os.path.dirname(registry_json)
        pinyin_db.update(config.pop('PINYIN_MAP'))
        global_conf.append(config)


read_all_registries(DEFAULT_JS_LIBRARIES, CITY_NAME_PINYIN_MAP)


class PyEchartsConfig(object):
    def __init__(self, echarts_template_dir='.', jshost=None,
                 force_js_embed=False):
        self.echarts_template_dir = echarts_template_dir
        self._jshost = remove_trailing_slashes(jshost)
        self.force_js_embed = force_js_embed
        self.hosted_on_github = False

    @property
    def js_embed(self):
        """ Determine whether to use embed code in <script> tag.
        """
        if self.force_js_embed:
            return True
        else:
            return self.jshost is None

    @property
    def jshost(self):
        return self._jshost

    @jshost.setter
    def jshost(self, jshost):
        self._jshost = remove_trailing_slashes(jshost)

    def get_js_library(self, pinyin):
        for library in DEFAULT_JS_LIBRARIES:
            file_map = library.get('FILE_MAP')
            return file_map.get(pinyin, pinyin)

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
            for library in DEFAULT_JS_LIBRARIES:
                file_map = library.get('FILE_MAP')
                filename = file_map.get(name)
                if filename:
                    path = os.path.join(library.get('LOCAL_PATH'),
                                        filename + '.js')
                    with open(path, 'rb') as f:
                        c = f.read()
                        contents.append(c.decode('utf8'))
        return contents

    def generate_js_link(self, js_names):
        links = []
        for name in js_names:
            for library in DEFAULT_JS_LIBRARIES:
                file_map = library.get('FILE_MAP')
                filename = file_map.get(name)
                if filename:
                    if self.jshost is None:
                        if self.hosted_on_github:
                            jshost = library['GITHUB_URL']
                        else:
                            jshost = library['JUPYTER_URL']
                    else:
                        jshost = self.jshost
                    link = '{}/{}.js'.format(jshost, filename)
                    links.append(link)
        return links

    def produce_require_configuration(self, dependencies):
        """

        :param dependencies:
        :param jshost:
        :return:
        """
        _d = _ensure_echarts_is_in_the_front(dependencies)
        # if no nick name register, we treat the location as location.js
        require_conf_items = []

        for name in _d:
            for library in DEFAULT_JS_LIBRARIES:
                file_map = library.get('FILE_MAP')
                filename = file_map.get(name)
                if filename:
                    if self.hosted_on_github:
                        jshost = library['GITHUB_URL']
                    else:
                        jshost = library['JUPYTER_URL']
                    item = "'%s': '%s/%s'" % (name,
                                              jshost,
                                              filename)
                    require_conf_items.append(item)
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


PYTHON_CONFIG = PyEchartsConfig()
JUPYTER_CONFIG = PyEchartsConfig(jshost=None)


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
        if jshost == constants.GITHUB_HOST:
            PYTHON_CONFIG.hosted_on_github = True
            JUPYTER_CONFIG.hosted_on_github = True
        else:
            PYTHON_CONFIG.jshost = jshost
            JUPYTER_CONFIG.jshost = jshost
    if echarts_template_dir:
        PYTHON_CONFIG.echarts_template_dir = echarts_template_dir
        JUPYTER_CONFIG.echarts_template_dir = echarts_template_dir
    if force_js_embed is not None:
        PYTHON_CONFIG.force_js_embed = force_js_embed


def online(host=constants.GITHUB_HOST):
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
