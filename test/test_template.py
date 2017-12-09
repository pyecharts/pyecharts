#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from nose.tools import eq_, raises
from pyecharts.template import ensure_echarts_is_in_the_front


def test_echarts_postion_in_dependency_list():
    test_sequence = set(['guangdong', 'shanghai', 'echarts'])
    result = ensure_echarts_is_in_the_front(test_sequence)
    eq_(result[0], 'echarts')


def test_echarts_postion_with_one_element_set():
    test_sequence = set(['echarts'])
    result = ensure_echarts_is_in_the_front(test_sequence)
    eq_(result[0], 'echarts')


@raises(Exception)
def test_echarts_postion_with_nothing():
    test_sequence = set()
    ensure_echarts_is_in_the_front(test_sequence)
