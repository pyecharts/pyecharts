# coding=utf8
"""
et = EChartsTranslator()
et.feed_event()
et.feed_options()
js_snippet = et.translate()

#
et.feed_options(options)
js_snippet = et.translate()
print(js_snippet.as_json_string())

"""

from __future__ import unicode_literals

import datetime
import json
import types
from collections import OrderedDict

from pyecharts.javascripthon.compat import TranslatorCompatAPI

__all__ = ['FunctionSnippet', 'JavascriptSnippet', 'EChartsTranslator']


class FunctionSnippet(OrderedDict):
    """
    A OrderedDict which stores translated function.
    {<func_name>:<func>}
    """

    def as_snippet(self):
        return ''.join(self.values())


class JavascriptSnippet(object):
    """
    A class presenting translated js code.
    """

    def __init__(self, function_snippet, option_snippet):
        self.function_snippet = function_snippet
        self.option_snippet = option_snippet

    def as_snippet(self):
        return self.function_snippet.as_snippet() + '\n' + self.option_snippet

    def as_json(self):
        if len(self.function_snippet) == 0:
            return self.option_snippet
        else:
            raise ValueError('Can not dump to a valid json string.')


class FunctionTranslator(object):
    def __init__(self):
        self.left_delimiter = '-=>'
        self.right_delimiter = '<=-'
        self.reference_str_format = ''.join(
            [self.left_delimiter, '{name}', self.right_delimiter]
        )
        self._shared_function_snippet = FunctionSnippet()

        # Tmp Data for a render process
        self._func_store = {}  # {<name>:<func>}
        self._replace_items = []

    def reset(self):
        self._func_store = {}
        self._replace_items = []

    def feed(self, func, name=None, reference=False):
        name = name or func.__name__
        self._func_store.update({name: func})
        if reference:
            ref_str = self.reference_str_format.format(name=name)
            self._replace_items.append((''.join(['"', ref_str, '"']), name))
            return ref_str

    def translate(self):
        fs = FunctionSnippet()
        for name, func in self._func_store.items():
            if name in self._shared_function_snippet:
                snippet = self._shared_function_snippet[name]
            else:
                snippet = TranslatorCompatAPI.translate_function(func)
                self._shared_function_snippet.update({name: snippet})
            fs.update({name: snippet})
        return fs

    def handle_options(self, options_snippet):
        for src, dest in self._replace_items:
            options_snippet = options_snippet.replace(src, dest)
        return options_snippet


class DefaultJsonEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        self._func_callback = kwargs.pop('func_callback', None)
        super(DefaultJsonEncoder, self).__init__(*args, **kwargs)

    def default(self, obj):
        if isinstance(obj, types.FunctionType) and self._func_callback:
            self._func_callback(obj)

        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if hasattr(obj, 'config'):
            return obj.config

        # Pandas and Numpy lists
        try:
            return obj.astype(float).tolist()

        except Exception:
            try:
                return obj.astype(str).tolist()

            except Exception:
                return super(DefaultJsonEncoder, self).default(obj)


class EChartsTranslator(object):
    def __init__(self):
        self.json_encoder = DefaultJsonEncoder(
            indent=4,
            func_callback=self._feed_func_in_options
        )
        self._function_translator = FunctionTranslator()
        self._cache = {}

    def reset(self):
        self._function_translator.reset()
        self._cache = {}

    def _feed_func_in_options(self, func):
        return self._function_translator.feed(func, reference=True)

    def feed_event(self, func, name=None):
        return self._function_translator.feed(func, name=name, reference=False)

    def feed_options(self, options):
        self._cache['options'] = options

    def translate(self):
        option_snippet = self.json_encoder.encode(self._cache['options'])
        function_snippet = self._function_translator.translate()
        option_snippet = self._function_translator.handle_options(
            option_snippet)
        return JavascriptSnippet(function_snippet, option_snippet)
