#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import json

import pandas as pd
import numpy as np

from nose.tools import eq_
from pyecharts import Bar


TITLE = "柱状图数据堆叠示例"


def create_a_bar(title):
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar(title)
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    return bar


def test_embed_option():
    bar = create_a_bar(TITLE)
    html = bar.render_embed()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "<html>" not in html
    assert "<body>" not in html


def test_notebook_render():
    bar = create_a_bar(TITLE)
    html = bar._repr_html_()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "require.config" in html
    assert "function(ec)" in html


def test_notebook_dom():

    bar = create_a_bar(TITLE)
    html = bar._render_notebook_dom_()
    assert bar._chart_id in html
    assert str(bar._width) in html
    assert str(bar._height) in html
    assert "<div" in html


def test_notebook_component():

    bar = create_a_bar(TITLE)
    html = bar._render_notebook_component_()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "myChart" in html
    assert bar._chart_id in html


def test_base_get_js_dependencies():

    bar = create_a_bar(TITLE)
    dependencies = bar.get_js_dependencies()
    expected = ['echarts.min']
    eq_(dependencies, expected)


def test_numpy_array():

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = np.array([5, 20, 36, 10, 75, 90])
    bar = Bar(TITLE)
    bar.add("商家A", attr, v1, is_stack=True)
    html = bar.render_embed()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html


def test_pandas_dataframe():
    title = 'bar chart'
    index = pd.date_range('3/8/2017', periods=6, freq='M')
    df1 = pd.DataFrame(np.random.randn(6), index=index)
    df2 = pd.DataFrame(np.random.randn(6), index=index)

    dtvalue1 = [i[0] for i in df1.values]
    dtvalue2 = [i[0] for i in df2.values]
    _index = [i for i in df1.index.format()]

    bar = Bar(title, 'Profit and loss situation')
    bar.add('profit', _index, dtvalue1)
    bar.add('loss', _index, dtvalue2)
    html = bar.render_embed()
    assert title in html
    bar.render()
