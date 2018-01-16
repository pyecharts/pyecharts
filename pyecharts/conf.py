# coding=utf-8
from __future__ import unicode_literals

from pyecharts.js_extension import load_all_extensions
from pyecharts.utils import get_resource_dir

# Path constants for template dir
DEFAULT_TEMPLATE_DIR = get_resource_dir('templates')

# Load js & map file index into a dictionary.

# JS_EXTENSIONS = [JsExtension..]
# CITY_NAME_PINYIN_MAP = {<Chinese Name>:<Pinyin>}
JS_EXTENSIONS, CITY_NAME_PINYIN_MAP = load_all_extensions()


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
        for extension in JS_EXTENSIONS:
            library = extension.get_js_library(pinyin)
            if library is not None:
                return library
        return None

    def chinese_to_pinyin(self, chinese):
        return CITY_NAME_PINYIN_MAP.get(chinese, chinese)

    @staticmethod
    def read_file_contents_from_local(js_names):
        contents = []
        for name in js_names:
            for extension in JS_EXTENSIONS:
                filecontent = extension.read_js_library(name)
                if filecontent:
                    contents.append(filecontent)
                    break
        return contents

    def generate_js_link(self, js_names):
        links = []
        for name in js_names:
            for extension in JS_EXTENSIONS:
                js_link = extension.get_js_link(
                    name, jshost=self.jshost)
                if js_link:
                    links.append(js_link)
                    break
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
            for extension in JS_EXTENSIONS:
                config_item = extension.produce_require_config_syntax(
                    name,
                    jshost=self.jshost,
                    use_github=self.hosted_on_github)
                if config_item:
                    require_conf_items.append(config_item)
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
              hosted_on_github=None,
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
    elif hosted_on_github is True:
        PYTHON_CONFIG.hosted_on_github = True
        JUPYTER_CONFIG.hosted_on_github = True
    if echarts_template_dir:
        PYTHON_CONFIG.echarts_template_dir = echarts_template_dir
        JUPYTER_CONFIG.echarts_template_dir = echarts_template_dir
    if force_js_embed is not None:
        PYTHON_CONFIG.force_js_embed = force_js_embed


def online(host=None):
    """ Set the jshost

    :param host:
    """
    if host is None:
        configure(hosted_on_github=True)
    else:
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
