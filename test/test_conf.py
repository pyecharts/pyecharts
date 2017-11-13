# coding=utf8

from __future__ import unicode_literals

from pyecharts.conf import PyEchartsConfig


def test_config():
    pec = PyEchartsConfig(jshost='https://demo')
    assert pec.jshost == 'https://demo'
    pec.jshost = 'https://demo/'
    assert pec.jshost == 'https://demo'

    pec.force_js_embed = True
    assert pec.js_embed
    pec.force_js_embed = False
    assert not pec.js_embed

    pec.jshost = '/templates/js/'
    assert pec.jshost == '/templates/js'
    pec.force_js_embed = True
    assert pec.js_embed
    pec.force_js_embed = False
    assert not pec.js_embed

    pec1 = PyEchartsConfig(jshost='http://demo/')
    assert pec1.jshost == 'http://demo'
