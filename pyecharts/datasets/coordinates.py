# coding=utf8
"""
The Raw Data and Access Interface for builtin coordinates.
"""
from __future__ import unicode_literals

import json
from io import open

from lml.plugin import PluginManager, PluginInfo

import pyecharts.constants as constants
from pyecharts.utils import get_resource_dir


__all__ = [
    "search_coordinates_by_filter",
    "search_coordinates_by_keyword",
    "search_coordinates_by_country_and_keyword",
    "get_coordinate",
]


class GeoDataBank(PluginManager):
    def __init__(self):
        super(GeoDataBank, self).__init__(
            constants.GEO_DATA_PLUGIN_TYPE
            )
        self.geo_coordinates = {}

    def get_coordinate(self, city, country):
        coordinates = None
        if country not in self.geo_coordinates:
            self._load_data_into_memory(country)
        coordinates = self.geo_coordinates[country].get(city)
        return coordinates

    def search_in_country(self, country, *names):
        return self.search_in_country_by_filter(
            country,
            lambda name_in_db: any([name in name_in_db for name in names])
        )

    def search_in_country_by_filter(self, country, filter_function):
        if country not in self.geo_coordinates:
            self._load_data_into_memory(country)
        _cities_in_a_country = self.geo_coordinates.get(country)
        if _cities_in_a_country:
            for city_name, coordinates in _cities_in_a_country.items():
                if filter_function(city_name):
                    yield(city_name, coordinates)

    def _load_data_into_memory(self, country):
        self.geo_coordinates[country] = {}
        for pypkgs in self.registry.values():
            for data_bank in pypkgs:
                _data_bank = data_bank.cls()
                _cities_in_a_country = _data_bank.get_cities_in_country(
                    country)
                self.geo_coordinates[country].update(_cities_in_a_country)


@PluginInfo(constants.GEO_DATA_PLUGIN_TYPE, tags=['builtin'])
class DefaultChinaDataSet:

    def get_cities_in_country(self, country):
        if country != "CN":
            return {}

        _local_data_file = get_resource_dir(
            "datasets", "city_coordinates.json")
        with open(_local_data_file, encoding="utf8") as f:
            return json.load(f)


GEO_DATA_BANK = GeoDataBank()


def search_coordinates_by_filter(func, country="CN"):
    """
    Search coordinates by filter function
    :param func: The filter call for search
    :return: A dictionary like {<name>:[<longitude>, <latitude>]}
    """
    result = GEO_DATA_BANK.search_in_country_by_filter(country, func)
    if result:
        return dict(result)
    else:
        return None


def search_coordinates_by_country_and_keyword(country, *args):
    """
    Search coordinates by country and city name
    :param country: the country name
    :param args: The keywords for fuzzy search
    :return: A dictionary like {<name>:[<longitude>, <latitude>]}
    """
    result = GEO_DATA_BANK.search_in_country(country, *args)
    if result:
        return dict(result)
    else:
        return None


def search_coordinates_by_keyword(*args):
    """
    Search coordinates by city name
    :param args: The keywords for fuzzy search
    :return: A dictionary like {<name>:[<longitude>, <latitude>]}
    """
    return search_coordinates_by_country_and_keyword("CN", *args)


def get_coordinate(name, country="CN"):
    """
    Return coordinate for the city name.
    :param name: City name or any custom name string.
    :return: A list like [longitude, latitude] or None
    """
    return GEO_DATA_BANK.get_coordinate(name, country)
