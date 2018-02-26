# coding=utf8
"""
Test Cases for jshost.
Input:a PyEchartsConfg object with cusom jshost and force_embed flag by user.
Test Target: js_embed (should render <script> in embed mode)
"""
from __future__ import unicode_literals

from nose.tools import eq_, raises

from pyecharts.conf import _ensure_echarts_is_in_the_front
from pyecharts.conf import PyEchartsConfig


def test_custom_local_jshost():
    target_config = PyEchartsConfig(jshost='/static/js/')
    eq_('/static/js', target_config.jshost)

    assert not target_config.js_embed

    target_config.force_js_embed = True

    assert target_config.js_embed


def test_get_js_library():
    test_config = PyEchartsConfig()
    actual = test_config.get_js_library('abc')
    assert actual is None


def test_custom_remote_jshost():
    target_config = PyEchartsConfig(
        jshost='https://cdn.bootcss.com/echarts/3.7.2/')
    eq_('https://cdn.bootcss.com/echarts/3.7.2', target_config.jshost)

    assert not target_config.js_embed

    target_config.force_js_embed = True

    assert target_config.js_embed


def test_echarts_postion_in_dependency_list():
    test_sequence = set(['guangdong', 'shanghai', 'echarts'])
    result = _ensure_echarts_is_in_the_front(test_sequence)
    eq_(result[0], 'echarts')


def test_echarts_postion_with_one_element_set():
    test_sequence = set(['echarts'])
    result = _ensure_echarts_is_in_the_front(test_sequence)
    eq_(result[0], 'echarts')


@raises(Exception)
def test_echarts_postion_with_nothing():
    test_sequence = set()
    _ensure_echarts_is_in_the_front(test_sequence)
