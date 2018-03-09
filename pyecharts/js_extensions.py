# coding=utf-8

import os
import json
import codecs

from lml.loader import scan_plugins
from lml.plugin import PluginManager

import pyecharts.exceptions as exceptions

# here are all plugins from pyecharts team
OFFICIAL_PLUGINS = [
    "jupyter_echarts_pypkg"
]
THIRD_PARTY_PLUGIN_PREFIX = "echarts_"

JS_EXTENSION_REGISTRY = 'registry.json'
REGISTRY_JS_FOLDER = 'JS_FOLDER'
REGISTRY_FILE_MAP = 'FILE_MAP'
REGISTRY_GITHUB_URL = 'GITHUB_URL'
REGISTRY_JUPYTER_URL = 'JUPYTER_URL'
REGISTRY_PINYIN_MAP = 'PINYIN_MAP'


class JsExtension(object):
    def __init__(self, extension_home, registry_content):
        self.registry = registry_content
        self.home = os.path.join(extension_home,
                                 self.registry[REGISTRY_JS_FOLDER])

    @classmethod
    def from_registry_path(cls, extension_installation_path):
        __registry_json__ = os.path.join(
            extension_installation_path, JS_EXTENSION_REGISTRY)
        __registry__ = read_a_map_registry(__registry_json__)
        _validate_registry(__registry__)
        return cls(extension_installation_path, __registry__)

    def get_js_library(self, pinyin):
        file_map = self.registry.get(REGISTRY_FILE_MAP)
        return file_map.get(pinyin)

    def read_js_library(self, pinyin):
        filename = self.get_js_library(pinyin)
        if filename:
            abs_path = os.path.join(self.home, filename + '.js')
            with codecs.open(abs_path, 'r', encoding='utf-8') as pf:
                return pf.read()
        else:
            return None

    def get_js_link(self, pinyin, jshost=None):
        filename = self.get_js_library(pinyin)
        if filename:
            if jshost is None:
                jshost = self.home
            return '%s/%s.js' % (jshost, filename)
        else:
            return None

    def produce_require_config_syntax(
            self, pinyin, jshost=None, use_github=False):
        filename = self.get_js_library(pinyin)
        if filename:
            jshost = self._resolve_jshost(jshost, use_github)
            return "'%s': '%s/%s'" % (pinyin, jshost, filename)
        else:
            return None

    def chinese_to_pinyin(self, chinese):
        __PINYIN_MAP__ = self.registry.get(REGISTRY_PINYIN_MAP, {})
        return __PINYIN_MAP__.get(chinese)

    def _resolve_jshost(self, jshost, use_github=False):
        __jshost__ = jshost
        if jshost is None:
            if use_github:
                __jshost__ = self.registry[REGISTRY_GITHUB_URL]
            else:
                __jshost__ = self.registry[REGISTRY_JUPYTER_URL]
        return __jshost__


class JsExtensionManager(PluginManager):
    def __init__(self):
        super(JsExtensionManager, self).__init__('pyecharts_js_extension')
        self.js_extensions = []

    def get_all_extensions(self):
        if len(self.js_extensions) == 0:
            for pypkgs in self.registry.values():
                for pypkg_info in pypkgs:
                    __pypkg__ = pypkg_info.cls()
                    __js_extension__ = JsExtension.from_registry_path(
                        __pypkg__.js_extension_path)
                    self.js_extensions.append(__js_extension__)
        return self.js_extensions

    def get_a_extension(self, name):
        if len(self.js_extensions) == 0:
            self.get_all_extensions()
        for __extension__ in self.js_extensions:
            if __extension__.registry['JS_FOLDER'] == name:
                return __extension__
        return None


EXTENSION_MANAGER = JsExtensionManager()
# Load js & map file index into a dictionary.
scan_plugins(
    THIRD_PARTY_PLUGIN_PREFIX,
    "pyecharts",  # <- useful for pyinstaller only
    white_list=OFFICIAL_PLUGINS)


def read_a_map_registry(registry_json):
    with codecs.open(registry_json, 'r', 'utf-8') as f:
        content = f.read()
        return json.loads(content)


def _validate_registry(registry):
    __registry_keys__ = [
        REGISTRY_JS_FOLDER,
        REGISTRY_FILE_MAP,
        REGISTRY_GITHUB_URL,
        REGISTRY_JUPYTER_URL,
        REGISTRY_PINYIN_MAP
    ]
    for key in __registry_keys__:
        if key not in registry:
            raise exceptions.InvalidRegistry("%s is missing" % key)
