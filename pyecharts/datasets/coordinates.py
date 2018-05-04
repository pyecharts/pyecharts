# coding=utf8
"""
The Raw Data and Access Interface for builtin coordinates.
"""
from __future__ import unicode_literals

import json
from io import open
from pyecharts.utils import get_resource_dir
from pyecharts.utils.lazy import LazyObject

__all__ = [
    "search_coordinates_by_filter",
    "search_coordinates_by_keyword",
    "get_coordinate",
]


def search_coordinates_by_filter(func):
    """
    Search coordinates by filter function
    :param func: The filter call for search
    :return: A dictionary like {<name>:[<longitude>, <latitude>]}
    """
    return dict((k, v) for k, v in _COORDINATE_DATASET.items() if func(k))


def search_coordinates_by_keyword(*args):
    """
    Search coordinates by city name
    :param args: The keywords for fuzzy search
    :return: A dictionary like {<name>:[<longitude>, <latitude>]}
    """
    return search_coordinates_by_filter(
        func=lambda _name: any([k in _name for k in args])
    )


def get_coordinate(name):
    """
    Return coordinate for the city name.
    :param name: City name or any custom name string.
    :return: A list like [longitude, latitude] or None
    """
    return _COORDINATE_DATASET.get(name, None)


def _load_coordinates():
    """
    Load the coordinate dataset into the dictionary.
    :return:
    """
    with open(
        get_resource_dir("datasets", "city_coordinates.json"), encoding="utf8"
    ) as f:
        return json.load(f)


_COORDINATE_DATASET = LazyObject(_load_coordinates)
