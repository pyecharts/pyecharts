# coding=utf-8
from __future__ import unicode_literals

from contextlib import contextmanager

import pyecharts.constants as constants
from pyecharts.js_extensions import EXTENSION_MANAGER

ONLINE_ASSETS_JS = "https://pyecharts.github.io/assets/js/"


class PyEchartsConfig(object):
    def __init__(
        self, echarts_template_dir=".", jshost=None, force_js_embed=False
    ):
        self.echarts_template_dir = echarts_template_dir
        self._jshost = remove_trailing_slashes(jshost)
        self.force_js_embed = force_js_embed
        self.hosted_on_github = False
        self.jupyter_presentation = constants.DEFAULT_HTML
        self.theme = constants.LIGHT_THEME

    @property
    def js_embed(self):
        """
        Determine whether to use embed code in <script> tag.
        """
        if self.force_js_embed:
            return True
        if self.hosted_on_github:
            return False
        else:
            return self.jshost is None

    @property
    def jshost(self):
        return self._jshost

    @jshost.setter
    def jshost(self, jshost):
        self._jshost = remove_trailing_slashes(jshost)

    def get_js_library(self, pinyin):
        for extension in EXTENSION_MANAGER.get_all_extensions():
            library = extension.get_js_library(pinyin)
            if library is not None:
                return library

        return None

    def chinese_to_pinyin(self, chinese):
        for extension in EXTENSION_MANAGER.get_all_extensions():
            __pinyin__ = extension.chinese_to_pinyin(chinese)
            if __pinyin__:
                return __pinyin__

        else:
            # no match found, i.e. 'world'
            return chinese

    @staticmethod
    def read_file_contents_from_local(js_names):
        contents = []
        for name in js_names:
            for extension in EXTENSION_MANAGER.get_all_extensions():
                filecontent = extension.read_js_library(name)
                if filecontent:
                    contents.append(filecontent)
                    break

        return contents

    def generate_js_link(self, js_names):
        # self.jshost 为 None 时应该使用远程 js
        # "https://pyecharts.github.io/assets/js"
        if not self.jshost:
            self.jshost = ONLINE_ASSETS_JS
        links = []
        for name in js_names:
            for extension in EXTENSION_MANAGER.get_all_extensions():
                js_link = extension.get_js_link(name, jshost=self.jshost)
                if js_link:
                    links.append(js_link)
                    break

        return links

    def produce_require_configuration(self, dependencies):
        __dependencies__ = _ensure_echarts_is_in_the_front(dependencies)
        # if no nick name register, we treat the location as location.js
        require_conf_items = []

        for name in __dependencies__:
            for extension in EXTENSION_MANAGER.get_all_extensions():
                config_item = extension.produce_require_config_syntax(
                    name, jshost=self.jshost, use_github=self.hosted_on_github
                )
                if config_item:
                    require_conf_items.append(config_item)
        require_libraries = ["'%s'" % key for key in __dependencies__]
        return dict(
            config_items=require_conf_items, libraries=require_libraries
        )

    def produce_html_script_list(self, dependencies):
        __dependencies__ = _ensure_echarts_is_in_the_front(dependencies)
        script_list = [
            "%s" % self.get_js_library(key) for key in __dependencies__
        ]
        return script_list


def remove_trailing_slashes(jshost):
    """
    Delete the end separator character if exists.
    """
    if jshost and jshost[-1] in ("/", "\\"):
        return jshost[:-1]

    else:
        return jshost


CURRENT_CONFIG = PyEchartsConfig()


def configure(
    jshost=None,
    hosted_on_github=None,
    echarts_template_dir=None,
    force_js_embed=None,
    output_image=None,
    global_theme=None,
):
    """
    Config all items for pyecharts when use chart.render() or page.render().

    :param jshost: the host for echarts related javascript libraries
    :param echarts_template_dir: the directory for custom html templates
    :param force_js_embed: embed javascript in html file or not
    :param output_image: Non None value asks pyecharts to use
                         pyecharts-snapshots to render as image directly.
                         Values such as 'svg', 'jpeg', 'png' changes
                         chart presentation in jupyter notebook to those image
                         formats, instead of 'html' format.
    """
    if jshost:
        CURRENT_CONFIG.jshost = jshost
    elif hosted_on_github is True:
        CURRENT_CONFIG.hosted_on_github = True
    if echarts_template_dir:
        CURRENT_CONFIG.echarts_template_dir = echarts_template_dir
    if force_js_embed is not None:
        CURRENT_CONFIG.force_js_embed = force_js_embed
    if output_image in constants.JUPYTER_PRESENTATIONS:
        CURRENT_CONFIG.jupyter_presentation = output_image
    if global_theme is not None:
        CURRENT_CONFIG.theme = global_theme


def online(host=None):
    """
    Set the jshost

    :param host: remote js host
    """
    if host is None:
        configure(hosted_on_github=True)
    else:
        configure(jshost=host)


def enable_nteract(host=None):
    # self.jshost 为 None 时应该使用远程 js
    # "https://pyecharts.github.io/assets/js"
    _host = ONLINE_ASSETS_JS
    if host:
        _host = host
    configure(
        output_image=constants.NTERACT, jshost=remove_trailing_slashes(_host)
    )


@contextmanager
def jupyter_image(jupyter_presentation):
    """
    Temporarily change jupyter's default presentation
    """
    previous_presentation = CURRENT_CONFIG.jupyter_presentation
    try:
        CURRENT_CONFIG.jupyter_presentation = jupyter_presentation
        yield

    finally:
        CURRENT_CONFIG.jupyter_presentation = previous_presentation


def _ensure_echarts_is_in_the_front(dependencies):
    """
    make sure echarts is the item in the list
    require(['echarts'....], function(ec) {..}) need it to
    be first but dependencies is a set so has no sequence
    """
    if len(dependencies) > 1:
        dependencies.remove("echarts")
        dependencies = ["echarts"] + list(dependencies)
    elif len(dependencies) == 1:
        # make a new list
        dependencies = list(dependencies)
    else:
        raise Exception("No js library found. Nothing works!")

    return dependencies
