import sys

PY35_ABOVE = sys.version_info[:2] >= (3, 5)

if PY35_ABOVE:
    from pyecharts.javascripthon.compiler import Python2Javascript
else:
    from pyecharts.javascripthon.client import Python2Javascript


class TranslatorCompatAPI(object):
    @staticmethod
    def translate_function(func):
        """
        Translate python function.
        :param func:
        :return: A multi-line unicode string
        """
        return Python2Javascript.translate(func)
