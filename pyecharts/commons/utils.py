import re

from pyecharts.datasets import EXTRA, FILENAMES


class JsCode:
    def __init__(self, js_code: str):
        self.js_code = "--x_x--0_0--" + js_code + "--x_x--0_0--"

    def replace(self, pattern: str, repl: str):
        self.js_code = re.sub(pattern, repl, self.js_code)
        return self


class OrderedSet:
    def __init__(self, *args):
        self._values = dict()
        self.items = []
        for a in args:
            self.add(a)

    def add(self, *items):
        for item in items:
            if not self._values.get(item, False):
                self._values.update({item: True})
                self.items.append(item)


def produce_require_dict(js_dependencies, js_host) -> dict:
    confs, libraries = [], []
    for name in js_dependencies.items:
        if name.startswith("http://api.map.baidu.com"):
            confs.append("'baidu_map_api{}':'{}'".format(len(name), name))
            libraries.append("'baidu_map_api{}'".format(len(name)))
        if name in FILENAMES:
            f, _ = FILENAMES[name]
            confs.append("'{}':'{}{}'".format(name, js_host, f))
            libraries.append("'{}'".format(name))
        else:
            for url, files in EXTRA.items():
                if name in files:
                    f, _ = files[name]
                    confs.append("'{}':'{}{}'".format(name, url, f))
                    libraries.append("'{}'".format(name))
                    break
    return dict(config_items=confs, libraries=libraries)


def write_utf8_html_file(file_name, html_content):
    with open(file_name, "w+", encoding="utf-8") as html_file:
        html_file.write(html_content)


def _flat(obj):
    if hasattr(obj, "js_dependencies"):
        return list(obj.js_dependencies)

    if isinstance(obj, (list, tuple, set)):
        return obj

    return (obj,)  # tuple


def _expand(dict_generator):
    return dict(list(dict_generator))


def _clean_dict(mydict):
    for key, value in mydict.items():
        if value is not None:
            if isinstance(value, dict):
                value = _expand(_clean_dict(value))

            elif isinstance(value, (list, tuple, set)):
                value = list(_clean_array(value))

            elif isinstance(value, str) and not value:
                # delete key with empty string
                continue

            yield (key, value)


def _clean_array(myarray):
    for value in myarray:
        if isinstance(value, dict):
            yield _expand(_clean_dict(value))

        elif isinstance(value, (list, tuple, set)):
            yield list(_clean_array(value))

        else:
            yield value


def remove_key_with_none_value(incoming_dict):
    if isinstance(incoming_dict, dict):
        return _expand(_clean_dict(incoming_dict))
    elif incoming_dict:
        return incoming_dict
    else:
        return None
