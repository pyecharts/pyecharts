# coding=utf8
"""
Test Case for the acccess interface of coordinate dataset
"""
from __future__ import unicode_literals
from pyecharts.datasets.coordinates import (
    get_coordinate,
    search_coordinates_by_keyword,
    search_coordinates_by_filter,
)

from nose.tools import assert_dict_equal


def test_get_coordinate():
    coordinate = get_coordinate("北京")
    assert [116.46, 39.92] == coordinate


def test_get_coordinate_without_data():
    coordinate = get_coordinate("A市")
    assert coordinate is None


def test_search_coordinates():
    # search the city name containing '北京'
    result = search_coordinates_by_keyword("北京")
    assert "北京" in result
    assert "北京市" in result


def test_advance_search_coordinates():
    result = search_coordinates_by_filter(
        func=lambda name: "福州" in name or "杭州" in name
    )
    assert "福州" in result
    assert "杭州" in result
    result2 = search_coordinates_by_keyword("福州", "杭州")
    assert_dict_equal(result, result2)
