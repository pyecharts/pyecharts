# coding=utf8

from __future__ import unicode_literals

import sys

from pyecharts_javascripthon import Python2Javascript

JAVASCRIPTHON_ENABLED = True


class FunctionTranslatorDisabled(Exception):
    pass


class TranslatorCompatAPI(object):

    @staticmethod
    def check_enabled(raise_exception=False):
        return True

    @staticmethod
    def translate_function(func):
        """
        Translate python function.
        :param func:
        :return: A multi-line unicode string
        """
        return Python2Javascript.translate(func)
