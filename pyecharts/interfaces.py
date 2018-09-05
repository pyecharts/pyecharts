# coding=utf8

"""Common interfaces.
"""


class JSONSerializableMixin(object):
    """A protocol for encode custom objects.
    Note: It may be a transitional design in violation of PEP8 .
    Use functools.singledispatch instead on python 3+.
    """

    def __json__(self):
        pass
