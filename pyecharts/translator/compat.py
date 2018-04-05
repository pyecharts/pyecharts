# coding=utf8

from __future__ import unicode_literals

import sys
import inspect

try:
    from metapensiero.pj.api import translates

    JAVASCRIPTHON_ENABLED = True
except ImportError:
    def translates(_lines):
        return ''


    JAVASCRIPTHON_ENABLED = False


class FunctionTranslatorNotSupported(Exception):
    pass


class TranslatorCompatAPI(object):
    @staticmethod
    def check_supported(raise_exception=False):
        PY35 = sys.version_info[:2] >= (3, 5)
        is_supported = PY35 and JAVASCRIPTHON_ENABLED
        if not is_supported and raise_exception:
            if not PY35:
                msg = "Python 3.5+ is required for function translator."

            else:
                msg = "javascripthon library isn't installed. see more on document"
            raise FunctionTranslatorNotSupported(msg)
        else:
            return PY35 and JAVASCRIPTHON_ENABLED

    @staticmethod
    def translate_function(func):
        """
        Translate python function.
        :param func:
        :return: A multi-line unicode string
        """
        source_lines, _ = inspect.getsourcelines(func)
        result = translates(source_lines)
        return result[0]
