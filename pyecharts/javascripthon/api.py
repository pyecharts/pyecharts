# coding=utf8
"""
A core api for python-to-javascript translator.
"""

from __future__ import unicode_literals

import datetime
import json
import types
from collections import OrderedDict
from contextlib import contextmanager

from pyecharts.javascripthon.compat import TranslatorCompatAPI

__all__ = ["EChartsTranslator"]


class FunctionStore(OrderedDict):
    """
    A OrderedDict which stores translated function.
    {<func_name>:<func>}
    """

    def to_js_snippet(self):
        return "".join(self.values())


class TranslateResult(object):
    def __init__(self, options, options_snippet, function_store):
        self._options = options
        self._options_snippet = options_snippet
        self._function_store = function_store

    @property
    def options_snippet(self):
        return self._options_snippet

    @property
    def function_snippet(self):
        return self._function_store.to_js_snippet()

    @property
    def has_function(self):
        return len(self._function_store) > 0

    def to_js_snippet(self):
        return "\n".join([self.function_snippet, self._options_snippet])


class MyJSONEncoder(json.JSONEncoder):
    """My custom JsonEncoder.
    1. Support datetime/date/numpy.ndarray object
    2. Support Function object
    3. My Json Encoder Protocol: __json__
    """

    def __init__(self, *args, **kwargs):
        """
        :param enable_func : enable encode function obj or not
        :param post_encode_func : The callback after encoding a function, ()
        """
        self._enable_func = kwargs.pop("enable_func", False)
        self._post_encode_func = kwargs.pop("post_encode_func", None)
        super(MyJSONEncoder, self).__init__(*args, **kwargs)

    def default(self, obj):
        if isinstance(obj, types.FunctionType) and self._enable_func:
            encoded_value = JSONTranslator.encode_func(obj)
            if self._post_encode_func:
                self._post_encode_func(obj, encoded_value)
            return encoded_value

        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        # Pandas and Numpy lists
        if obj.__class__.__name__ in ("ndarray", "Series", "DataFrame"):
            try:
                return obj.astype(float).tolist()
            except ValueError:
                pass
            try:
                return obj.astype(str).tolist()
            except ValueError:
                raise

        if hasattr(obj, "__json__"):
            return obj.__json__()
        return super(MyJSONEncoder, self).default(obj)


class TranslatorMixin(object):
    """A Interface for state-machine translator
    """

    @contextmanager
    def new_task(self):
        try:
            self.reset()
            yield
        finally:
            self.reset()

    def reset(self):
        pass

    def translate(self):
        """Main process
        """
        pass


class FunctionTranslator(TranslatorMixin):
    """A translator for function,a FunctionStore object will be generated.
    """

    def __init__(self):
        self._shared_function_snippet = FunctionStore()

        # Tmp Data for a render process
        self._func_store = {}  # {<name>:<func>}

    def reset(self):
        self._func_store = {}

    def feed(self, func, name=None):
        name = name or func.__name__
        self._func_store.update({name: func})
        return self

    def translate(self):
        fs = FunctionStore()
        for name, func in self._func_store.items():
            if name in self._shared_function_snippet:
                snippet = self._shared_function_snippet[name]
            else:
                snippet = TranslatorCompatAPI.translate_function(func)
                self._shared_function_snippet.update({name: snippet})
            fs.update({name: snippet})
        return fs


class JSONTranslator(TranslatorMixin):
    def __init__(self, post_encode_func=None):
        self._data_store = {}
        self._replace_items = []
        self._post_encode_func = post_encode_func

        self._encoder = MyJSONEncoder(
            enable_func=True, post_encode_func=self._my_post_encode_func
        )

    def feed(self, options):
        self._data_store["options"] = options

    def translate(self):
        options_snippet = self._encoder.encode(self._data_store["options"])
        for src, dest in self._replace_items:
            options_snippet = options_snippet.replace(src, dest)
        return options_snippet

    def _my_post_encode_func(self, func, func_encoded):
        replaced_str = '"{}"'.format(func_encoded)
        self._replace_items.append((replaced_str, func.__name__))
        self._post_encode_func(func, func_encoded)

    @staticmethod
    def encode_func(func, func_name=None):
        if func:
            func_name = func.__name__
        else:
            func_name = func_name
        return "-=>{}<=-".format(func_name)


class EChartsTranslator(TranslatorMixin):
    def __init__(self):
        self._json_translator = JSONTranslator(
            post_encode_func=self.func_encode_bridge
        )
        self._function_translator = FunctionTranslator()
        self._cache = {}

    def reset(self):
        self._function_translator.reset()
        self._cache = {}

    def func_encode_bridge(self, func, func_encoded):
        """
        <<JSONTranslator>> --> <<EChartsTranslator>> --> <<FunctionTranslator>>
        :param func:
        :param func_encoded:
        :return:
        """
        return self._function_translator.feed(func)

    # ------ Public API - Translator -----

    def feed_event(self, func, name=None):
        """Add a event function
        :param func: Event function object
        :param name: The name of function
        :return: None
        """
        return self._function_translator.feed(func, name=name)

    def feed_options(self, options):
        """Add options dict
        :param options: A dictionary for options
        :return:
        """
        self._json_translator.feed(options)
        return self

    def translate(self):
        """Translate a options,a TranslateResult object is returned
        :return: a TranslateResult
        """
        option_snippet = self._json_translator.translate()
        function_store = self._function_translator.translate()
        return TranslateResult(
            options=self._json_translator._data_store["options"],
            options_snippet=option_snippet,
            function_store=function_store,
        )

    # ------ Tools ------

    @staticmethod
    def dumps(obj, enable_func=False, post_encode_func=None, **kwargs):
        """A simple wrapper for json.dumps
        :param obj:
        :param enable_func:
        :param post_encode_func
        :param kwargs:
        :return:
        """
        encoder = MyJSONEncoder(
            enable_func=enable_func,
            post_encode_func=post_encode_func,
            **kwargs
        )
        return encoder.encode(obj)
