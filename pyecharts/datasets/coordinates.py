# coding=utf8
"""
The Raw Data and Access Interface for builtin coordinates.
"""
from __future__ import unicode_literals

import codecs
import json

from lml.plugin import PluginInfo, PluginManager

import pyecharts.constants as constants
import pyecharts.exceptions as exceptions
from pyecharts.utils import get_resource_dir, is_ascii

__all__ = [
    "search_coordinates_by_filter",
    "search_coordinates_by_keyword",
    "search_coordinates_by_region_and_keyword",
    "get_coordinate",
]

REGION_DB = "countries_regions_db.json"


class GeoDataBank(PluginManager):
    def __init__(self):
        super(GeoDataBank, self).__init__(constants.GEO_DATA_PLUGIN_TYPE)
        self.geo_coordinates = {}
        self.region_dict = {}

    def get_coordinate(self, city, region):
        region = self.ensure_two_digit_iso_code(region)
        if region not in self.geo_coordinates:
            self._load_data_into_memory(region)
        coordinates = self.geo_coordinates[region].get(city)
        return coordinates

    def search_in_region(self, region, *names):
        region = self.ensure_two_digit_iso_code(region)
        return self.search_in_region_by_filter(
            region,
            lambda name_in_db: any([name in name_in_db for name in names]),
        )

    def search_in_region_by_filter(self, region, filter_function):
        region = self.ensure_two_digit_iso_code(region)
        if region not in self.geo_coordinates:
            self._load_data_into_memory(region)
        _cities_in_a_region = self.geo_coordinates.get(region)
        if _cities_in_a_region:
            for city_name, coordinates in _cities_in_a_region.items():
                if filter_function(city_name):
                    yield (city_name, coordinates)

    def ensure_two_digit_iso_code(self, region):
        two_digit_code = region
        if region is not None:
            if is_ascii(region) and len(region) == 2:
                pass
            else:
                two_digit_code = self._translate_region(region)
        return two_digit_code

    def _load_data_into_memory(self, region):
        self.geo_coordinates[region] = {}
        for pypkgs in self.registry.values():
            for data_bank in pypkgs:
                _data_bank = data_bank.cls()
                _cities_in_a_region = _data_bank.get_cities_in_region(region)
                if _cities_in_a_region:
                    self.geo_coordinates[region].update(_cities_in_a_region)

    def _translate_region(self, region):
        if not self.region_dict:
            self._load_countries_into_memory()
        two_digit_code = self.region_dict.get(region)
        if two_digit_code is None:
            raise exceptions.RegionNotFound(
                "Pyecharts have no knowledge of {}".format(region)
            )
        return two_digit_code

    def _load_countries_into_memory(self):
        _region_dict = get_resource_dir("datasets", REGION_DB)
        with codecs.open(_region_dict, encoding="utf-8") as file_handle:
            self.region_dict = json.load(file_handle)


@PluginInfo(constants.GEO_DATA_PLUGIN_TYPE, tags=["builtin"])
class DefaultChinaDataBank:
    def get_cities_in_region(self, region):

        if region != "CN":
            return {}

        _local_data_file = get_resource_dir(
            "datasets", "city_coordinates.json"
        )
        with codecs.open(_local_data_file, encoding="utf8") as f:
            return json.load(f)


GEO_DATA_BANK = GeoDataBank()


def search_coordinates_by_filter(func, region="CN"):
    """
    Search coordinates by filter function
    :param func: The filter call for search
    :param region: the region name
    :return: A dictionary like {<name>:[<longitude>, <latitude>]}
    """
    result = GEO_DATA_BANK.search_in_region_by_filter(region, func)
    if result:
        return dict(result)
    else:
        return None


def search_coordinates_by_region_and_keyword(region, *args):
    """
    Search coordinates by region and city name
    :param region: the region name
    :param args: The keywords for fuzzy search
    :return: A dictionary like {<name>:[<longitude>, <latitude>]}
    """
    result = GEO_DATA_BANK.search_in_region(region, *args)
    if result:
        return dict(result)
    else:
        return None


def search_coordinates_by_keyword(*args):
    """
    Search coordinates by city name in China
    :param args: The keywords for fuzzy search
    :return: A dictionary like {<name>:[<longitude>, <latitude>]}
    """
    return search_coordinates_by_region_and_keyword("CN", *args)


def get_coordinate(name, region="CN"):
    """
    Return coordinate for the city name.
    :param name: City name or any custom name string.
    :param region: the region name
    :return: A list like [longitude, latitude] or None
    """
    return GEO_DATA_BANK.get_coordinate(name, region)
