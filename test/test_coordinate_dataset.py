# coding=utf8
"""
Test Case for the acccess interface of coordinate dataset
"""
from __future__ import unicode_literals
from nose.tools import eq_, raises
from nose.tools import assert_dict_equal

from pyecharts.datasets.coordinates import (
    get_coordinate,
    search_coordinates_by_region_and_keyword,
    search_coordinates_by_keyword,
    search_coordinates_by_filter,
    DefaultChinaDataBank,
    GEO_DATA_BANK,
)
from pyecharts.exceptions import RegionNotFound


def test_get_coordinate():
    coordinate = get_coordinate("北京")
    assert [116.407526, 39.904030] == coordinate


def test_get_coordinate_without_data():
    coordinate = get_coordinate("A市")
    assert coordinate is None


def test_search_coordinates():
    # search the city name containing '北京'
    result = search_coordinates_by_keyword("北京")
    assert "北京" in result
    assert "北京市" in result


def test_search_coordinates_by_region():
    # search the city name containing '北京'
    result = search_coordinates_by_region_and_keyword("CN", "北京")
    assert "北京" in result
    assert "北京市" in result


def test_search_coordinates_by_region_in_chinese():
    # search the city name containing '北京'
    result = search_coordinates_by_region_and_keyword("中国", "北京")
    assert "北京" in result
    assert "北京市" in result


@raises(RegionNotFound)
def test_get_coordinate_from_unknown_region():
    get_coordinate("Alien City", "Glaxy")


def test_advance_search_coordinates():
    result = search_coordinates_by_filter(
        func=lambda name: "福州" in name or "杭州" in name
    )
    assert "福州" in result
    assert "杭州" in result
    result2 = search_coordinates_by_keyword("福州", "杭州")
    assert_dict_equal(result, result2)


def test_default_china_data_bank():
    bank = DefaultChinaDataBank()
    cities = bank.get_cities_in_region("CN")
    assert "北京市" in cities


def test_default_china_data_bank_with_mars():
    bank = DefaultChinaDataBank()
    cities = bank.get_cities_in_region("火星")
    assert len(cities) == 0


def test_two_digit_iso_code():
    code = GEO_DATA_BANK.ensure_two_digit_iso_code("安提瓜和巴布达")
    eq_(code, "AG")


def test_two_digit_iso_code_with_two_digit_code():
    code = GEO_DATA_BANK.ensure_two_digit_iso_code("LU")
    eq_(code, "LU")


def test_two_digit_iso_code_with_wrong_input():
    code = GEO_DATA_BANK.ensure_two_digit_iso_code(None)
    eq_(code, None)
