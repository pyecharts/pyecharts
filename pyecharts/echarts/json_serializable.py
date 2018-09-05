# coding=utf8

from pyecharts.interfaces import JSONSerializableMixin
from pyecharts.utils import remove_key_with_none_value


class JsonSerializable(JSONSerializableMixin):
    def __init__(self):
        self._config = {}

    def __setitem__(self, key, value):
        self._config[key] = value

    def __getitem__(self, key):
        return self._config.get(key)

    def update(self, **kwargs):
        self._config.update(**kwargs)

    def __json__(self):
        return remove_key_with_none_value(self._config)
