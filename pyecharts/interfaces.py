# coding=utf8
# flake8: noqa

"""Common interfaces.
"""


class JSONSerializableMixin(object):
    """A protocol for encode custom objects.
    Note: It may be a transitional design in violation of PEP8 .
    Use functools.singledispatch instead on python 3+.
    """

    def __json__(self):
        pass


class IPythonRichDisplayMixin(object):
    """A interface for rich display.
     See also https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display
    """

    def _repr_html_(self):
        pass

    def _repr_svg_(self):
        pass

    def _repr_png_(self):
        pass

    def _repr_jpeg_(self):
        pass
