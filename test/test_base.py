#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import os
import sys
import json
import codecs

import pandas as pd
import numpy as np

from nose.tools import eq_
from pyecharts import Bar, Map
from test.constants import CLOTHES


TITLE = "柱状图数据堆叠示例"


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
    assert str(bar.width) in html
    assert str(bar.height) in html
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
    v1 = np.array([5, 20, 36, 10, 75, 90])
    bar = Bar(TITLE)
    bar.add("商家A", CLOTHES, v1, is_stack=True)
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


def test_echarts_position_in_render_html():
    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    map = Map("广东地图示例", width=1200, height=600, page_title=TITLE)
    map.add("", attr, value, maptype='广东',
            is_visualmap=True, visual_text_color='#000')
    map.render()
    with codecs.open('render.html', 'r', 'utf-8') as f:
        actual_content = f.read()
        assert TITLE in actual_content


def test_show_config():
    stdout_ = sys.stdout
    captured_stdout = 'stdout.txt'
    try:
        with open(captured_stdout, 'w') as f:
            sys.stdout = f
            bar = create_a_bar("new")
            bar.show_config()
    except Exception as e:
        # whatever happens, continue and restore stdout
        print(e)
    sys.stdout = stdout_
    with open(captured_stdout, 'r') as f:
        content = f.read()
        assert 'None' not in content
        assert 'null' in content
        assert 'false' in content
        assert 'False' not in content
    os.unlink(captured_stdout)


def test_base_cast_records():
    records = [{"key": 1}, {"value": 2}]
    keys, values = Bar.cast(records)
    eq_(keys, ["key", "value"])
    eq_(values, [1, 2])


def test_base_cast_dict():
    adict = {"key": 1, "value": 2}
    keys, values = Bar.cast(adict)
    eq_(keys, ["key", "value"])
    eq_(values, [1, 2])
