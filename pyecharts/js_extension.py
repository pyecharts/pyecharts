import os
import json
import codecs

from pyecharts.utils import get_resource_dir

PYECHARTS_DIR = '.pyecharts'
JS_EXTENSION_REGISTRY = 'registry.json'

DEFAULT_TEMPLATE_DIR = get_resource_dir('templates')
DEFAULT_ECHARTS_LOCATION = os.path.join(
    get_resource_dir('templates'), 'js')


class JsExtension(object):
    def __init__(self, extension_installation_path):
        self.home = extension_installation_path
        self.registry = read_a_map_registry(
            os.path.join(self.home, JS_EXTENSION_REGISTRY))

    def get_js_library(self, pinyin):
        file_map = self.registry.get('FILE_MAP')
        return file_map.get(pinyin)

    def read_js_library(self, pinyin):
        filename = self.get_js_library(pinyin)
        if filename:
            abs_path = os.path.join(self.home, filename + '.js')
            with codecs.open(abs_path, 'r', encoding='utf-8') as pf:
                return pf.read()
        else:
            return None

    def get_js_link(self, pinyin, jshost=None, use_github=False):
        filename = self.get_js_library(pinyin)
        if filename:
            jshost = self._resolve_jshost(jshost, use_github)
            return '%s/%s.js' % (jshost, filename)
        else:
            return None

    def produce_require_config_syntax(self,
                                      pinyin, jshost=None, use_github=False):
        filename = self.get_js_library(pinyin)
        if filename:
            jshost = self._resolve_jshost(jshost, use_github)
            return "'%s': '%s/%s'" % (pinyin, jshost, filename)
        else:
            return None

    def _resolve_jshost(self, jshost, use_github=False):
        __jshost__ = jshost
        if jshost is None:
            if use_github:
                __jshost__ = self.registry['GITHUB_URL']
            else:
                __jshost__ = self.registry['JUPYTER_URL']
        return __jshost__


def load_all_extensions():
    pyecharts_dir = _get_pyecharts_dir()
    extensions = [JsExtension(DEFAULT_ECHARTS_LOCATION)]
    pinyin_db = {}
    if os.path.exists(pyecharts_dir):
        for adir in os.listdir(pyecharts_dir):
            extensions.append(
                JsExtension(os.path.join(pyecharts_dir, adir)))

    for extension in extensions:
        pinyin_db.update(extension.registry.get('PINYIN_MAP'))
    return extensions, pinyin_db


def read_a_map_registry(registry_json):
    with codecs.open(registry_json, 'r', 'utf-8') as f:
        content = f.read()
        return json.loads(content)


def _get_pyecharts_dir():
    user_home = os.path.expanduser('~')
    package_home = os.path.join(user_home, PYECHARTS_DIR)
    return package_home
