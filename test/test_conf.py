# coding=utf8
"""
Test Cases for jshost.
Input:a PyEchartsConfg object with cusom jshost and force_embed flag by user.
Test Target: js_embed (should render <script> in embed mode)
"""
from __future__ import unicode_literals

from nose.tools import eq_

from pyecharts.conf import PyEchartsConfig
from pyecharts.constants import DEFAULT_HOST, SCRIPT_LOCAL_JSHOST, JUPYTER_LOCAL_JSHOST


def test_with_default_value():
    target_config = PyEchartsConfig()
    eq_(SCRIPT_LOCAL_JSHOST, target_config.jshost)
    eq_(SCRIPT_LOCAL_JSHOST, target_config.get_current_jshost_for_script())
    eq_(JUPYTER_LOCAL_JSHOST, target_config.get_current_jshost_for_jupyter())

    assert target_config.js_embed

    target_config.force_js_embed = True

    assert target_config.js_embed


def test_pyecharts_remote_jshost():
    target_config = PyEchartsConfig(jshost=DEFAULT_HOST)
    eq_('https://chfw.github.io/jupyter-echarts/echarts', target_config.jshost)
    eq_('https://chfw.github.io/jupyter-echarts/echarts', target_config.get_current_jshost_for_script())
    eq_('https://chfw.github.io/jupyter-echarts/echarts', target_config.get_current_jshost_for_jupyter())
    eq_('/static/js/echarts', target_config.get_current_jshost_for_jupyter('/static/js/echarts'))

    assert target_config.js_embed

    target_config.force_js_embed = True

    assert target_config.js_embed


def test_custom_local_jshost():
    target_config = PyEchartsConfig(jshost='/static/js/')
    eq_('/static/js', target_config.jshost)
    eq_('/static/js', target_config.get_current_jshost_for_script())
    eq_('/static/js', target_config.get_current_jshost_for_jupyter())
    eq_('/static/js/echarts', target_config.get_current_jshost_for_jupyter('/static/js/echarts'))

    assert not target_config.js_embed

    target_config.force_js_embed = True

    assert target_config.js_embed


def test_custom_remote_jshost():
    target_config = PyEchartsConfig(jshost='https://cdn.bootcss.com/echarts/3.7.2/')
    eq_('https://cdn.bootcss.com/echarts/3.7.2', target_config.jshost)
    eq_('https://cdn.bootcss.com/echarts/3.7.2', target_config.get_current_jshost_for_script())
    eq_('https://cdn.bootcss.com/echarts/3.7.2', target_config.get_current_jshost_for_jupyter())
    eq_('/static/js/echarts', target_config.get_current_jshost_for_jupyter('/static/js/echarts'))

    assert not target_config.js_embed

    target_config.force_js_embed = True

    assert target_config.js_embed
