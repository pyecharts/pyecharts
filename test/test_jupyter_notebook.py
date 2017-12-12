#!/usr/bin/env python
# coding=utf-8
"""
Test cases for jupyter notebook.
"""
from __future__ import unicode_literals

import json
from pyecharts import Bar
from test.constants import CLOTHES

TITLE = "柱状图数据堆叠示例"

DEFAULT_NBEXTENSION_PATH = '/nbextensions/echarts'


def create_a_bar(title):
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar(title)
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)
    return bar


def test_embed_option():
    bar = create_a_bar(TITLE)
    html = bar.render_embed()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "<html>" not in html
    assert "<body>" not in html


def test_notebook_dom():
    bar = create_a_bar(TITLE)
    html = bar._render_notebook_dom_()
    assert bar._chart_id in html
    assert str(bar.width) in html
    assert str(bar.height) in html
    assert "<div" in html


def test_notebook_component():
    bar = create_a_bar(TITLE)
    html = bar._render_notebook_component_()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "myChart" in html
    assert bar.chart_id in html


def test_notebook_render():
    bar = create_a_bar(TITLE)
    html = bar._repr_html_()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "require.config" in html
    assert "function(ec)" in html
    assert DEFAULT_NBEXTENSION_PATH in html


def test_notebook_render_with_custom_jshost():
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar(TITLE, jshost='http://localhost:9090')
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)

    html = bar._repr_html_()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "require.config" in html
    assert "function(ec)" in html
    assert 'http://localhost:9090' in html
