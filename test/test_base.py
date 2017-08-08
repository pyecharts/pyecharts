#!/usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals

import json

import pandas as pd
import numpy as np
from pyecharts import Bar


def test_embed_option():

    title = "柱状图数据堆叠示例"
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar(title)
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    html = bar.render_embed()
    json_encoded_title = json.dumps(title)
    assert json_encoded_title in html
    assert "<html>" not in html
    assert "<body>" not in html


def test_numpy_array():

    title = "柱状图数据堆叠示例"
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = np.array([5, 20, 36, 10, 75, 90])
    bar = Bar(title)
    bar.add("商家A", attr, v1, is_stack=True)
    html = bar.render_embed()
    json_encoded_title = json.dumps(title)
    assert json_encoded_title in html


def test_pandas_dataframe():

    title = 'Bar chart'
    index = pd.date_range('3/8/2017', periods=6, freq='M')
    df1 = pd.DataFrame(np.random.randn(6), index=index)
    df2 = pd.DataFrame(np.random.randn(6), index=index)

    dtvalue1 = [i[0] for i in df1.values]
    dtvalue2 = [i[0] for i in df2.values]

    bar = Bar(title, 'Profit and loss situation')
    bar.add('profit', df1.index, dtvalue1)
    bar.add('loss', df2.index,  dtvalue2)
    html = bar.render_embed()
    assert title in html
