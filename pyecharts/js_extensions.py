import os
import json
import codecs

from lml.loader import scan_plugins
from lml.plugin import PluginManager

from pyecharts.utils import get_resource_dir

# here are all plugins from pyecharts team
OFFICIAL_PLUGINS = [
    "jupyter_echarts_pypkg",
    "echarts_china_cities_pypkg",
    "echarts_countries_pypkg"
]

JS_EXTENSION_REGISTRY = 'registry.json'
REGISTRY_JS_FOLDER = 'JS_FOLDER'
REGISTRY_FILE_MAP = 'FILE_MAP'
REGISTRY_GITHUB_URL = 'GITHUB_URL'
REGISTRY_JUPYTER_URL = 'JUPYTER_URL'
REGISTRY_PINYIN_MAP = 'PINYIN_MAP'


THIRD_PARTY_PLUGIN_PREFIX = "pyecharts_"
DEFAULT_TEMPLATE_DIR = get_resource_dir('templates')
DEFAULT_ECHARTS_LOCATION = os.path.join(
    get_resource_dir('templates'), 'js')


class JsExtension(object):
    def __init__(self, extension_installation_path):
        self.registry = read_a_map_registry(
            os.path.join(extension_installation_path, JS_EXTENSION_REGISTRY))
        self.home = os.path.join(
            extension_installation_path,
            self.registry[REGISTRY_JS_FOLDER])

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
        self.plugins = []

    def get_all_plugins(self):
        if len(self.plugins) == 0:
            for plugins in self.registry.values():
                for plugin in plugins:
                    self.plugins.append(plugin.cls())
        return self.plugins


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
