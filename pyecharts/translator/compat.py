# coding=utf8

from __future__ import unicode_literals

import sys

try:
    from pyecharts_javascripthon import Python2Javascript

    JAVASCRIPTHON_ENABLED = True
except ImportError:

    class Python2Javascript:
        @staticmethod
        def translate(_lines):
            return ''

    JAVASCRIPTHON_ENABLED = False


class FunctionTranslatorDisabled(Exception):
    pass


class TranslatorCompatAPI(object):

    @staticmethod
    def check_enabled(raise_exception=False):
        PY35 = sys.version_info[:2] >= (3, 5)
        enabled = PY35 and JAVASCRIPTHON_ENABLED
        if not enabled and raise_exception:
            # Don't check the order because of python version's precedence.
            if not PY35:
                msg = "Python 3.5+ is required for function translator."
            else:
                msg = "javascripthon library isn't installed."
            raise FunctionTranslatorDisabled(msg)
        return enabled

    @staticmethod
    def translate_function(func):
        """
        Translate python function.
        :param func:
        :return: A multi-line unicode string
        """
        return Python2Javascript.translate(func)
