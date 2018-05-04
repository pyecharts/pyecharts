# coding=utf8

from __future__ import unicode_literals
import sys
import operator

__all__ = ["LazyObject"]

PY2 = sys.version_info[0] == 2

EMPTY = object()  # Used for that proxy has not executed.


def proxy_method(func):

    def inner(self, *args):
        if self._wrapped is EMPTY:
            self._setup()
        return func(self._wrapped, *args)

    return inner


class LazyObject(object):
    _wrapped = None

    def __init__(self, func):
        self.__dict__["_setupfunc"] = func
        self._wrapped = EMPTY

    def _setup(self):
        self._wrapped = self._setupfunc()

    __getattr__ = proxy_method(getattr)

    def __setattr__(self, key, value):
        if key == "_wrapped":
            self.__dict__["_wrapped"] = value
        else:
            if self._wrapped is EMPTY:
                self._setup()
            setattr(self._wrapped, key, value)

    def __delattr__(self, name):
        if name == "_wrapped":
            raise TypeError("can't delete _wrapped.")

        if self._wrapped is EMPTY:
            self._setup()
        delattr(self._wrapped, name)

    __getitem__ = proxy_method(operator.getitem)
    __class__ = property(proxy_method(operator.attrgetter("__class__")))
    __eq__ = proxy_method(operator.eq)
    __ne__ = proxy_method(operator.ne)
    __hash__ = proxy_method(hash)

    if PY2:
        __str__ = proxy_method(str)
        __unicode__ = proxy_method(unicode)  # NOQA: unicode undefined on PY3
        __nonzero__ = proxy_method(bool)
    else:
        __bytes__ = proxy_method(bytes)
        __str__ = proxy_method(str)
        __bool__ = proxy_method(bool)
