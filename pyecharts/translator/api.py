# coding=utf8

"""
The api module for python-to-javascript translator
"""

from __future__ import unicode_literals

import datetime
import json
import types

from pyecharts.translator.compat import TranslatorCompatAPI


class FunctionSnippet(object):
    def __init__(self):
        self._function_names = []  # js function name,not python function name
        self._function_codes = []

    def add(self, function_code, function_name):
        if function_name not in self._function_names:
            self._function_codes.append(function_code)
            self._function_names.append(function_name)

    def as_snippet(self):
        return ''.join(self._function_codes)

    def __contains__(self, item):
        return item in self._function_names

    def get_snippet(self, func_names):
        try:
            index = self._function_names.index(func_names)
            return self._function_codes[index]
        except ValueError:
            pass


class JavascriptSnippet(object):
    def __init__(self, function_snippet, option_snippet):
        self.function_snippet = function_snippet
        self.option_snippet = option_snippet

    def as_snippet(self):
        return self.function_snippet + '\n' + self.option_snippet


class FunctionTranslator(object):
    def __init__(self):
        self.left_delimiter = '-=>'
        self.right_delimiter = '<=-'
        self.reference_str_format = ''.join([
            self.left_delimiter,
            '{name}',
            self.right_delimiter
        ])
        self._shared_function_snippet = FunctionSnippet()

        # Tmp Data for a render process
        self._func_store = {}  # {<name>:<func>}
        self._replace_items = []

    def reset(self):
        self._func_store = {}
        self._replace_items = []

    def feed(self, func, name=None):
        name = name or func.__name__
        self._func_store.update({name: func})
        ref_str = self.reference_str_format.format(name=name)
        self._replace_items.append((''.join(['"', ref_str, '"']), name))
        return ref_str

    def translate(self):
        fs = FunctionSnippet()
        for name, func in self._func_store.items():
            if name in self._shared_function_snippet:
                snippet = self._shared_function_snippet.get_snippet(name)
            else:
                snippet = TranslatorCompatAPI.translate_function(func)
                self._shared_function_snippet.add(snippet, name)
            fs.add(snippet, name)
        return fs

    def handle_options(self, options_snippet):
        for src, dest in self._replace_items:
            options_snippet = options_snippet.replace(src, dest)
        return options_snippet


_FUNCTION_TRANSLATOR = FunctionTranslator()


class DefaultJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, types.LambdaType):
            # Lambda expression is not supported
            return super(DefaultJsonEncoder, self).default(obj)
        if isinstance(obj, types.FunctionType):
            TranslatorCompatAPI.check_enabled(raise_exception=True)
            return _FUNCTION_TRANSLATOR.feed(obj)
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        # Pandas and Numpy lists
        try:
            return obj.astype(float).tolist()

        except Exception:
            try:
                return obj.astype(str).tolist()

            except Exception:
                return super(DefaultJsonEncoder, self).default(obj)


class EChartsTranslator(object):
    def __init__(self, json_encoder=DefaultJsonEncoder):
        self.json_encoder = json_encoder

    def translate(self, options):
        _FUNCTION_TRANSLATOR.reset()
        option_snippet = json.dumps(
            options,
            indent=4,
            cls=self.json_encoder
        )
        function_snippet = _FUNCTION_TRANSLATOR.translate()
        option_snippet = _FUNCTION_TRANSLATOR.handle_options(option_snippet)
        return JavascriptSnippet(function_snippet.as_snippet(), option_snippet)


TRANSLATOR = EChartsTranslator()
