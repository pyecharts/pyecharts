#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import os
import json
import shutil

import pandas as pd
import numpy as np

from mock import patch
from nose.tools import eq_

from pyecharts import Bar
from pyecharts.base import install_echarts_if_needed


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
    bar.add('loss', df2.index, dtvalue2)
    html = bar.render_embed()
    assert title in html


@patch("jupyter_core.paths.jupyter_data_dir")
def test_echarts_installation(fake_jupyter_data_dir):
    # test preparation
    fake_dir_name = 'fake_jupyter_data_dir'
    fake_nbextension_folder = os.path.join(fake_dir_name, 'nbextensions')
    os.makedirs(fake_nbextension_folder)

    # install js files to the fake directory
    fake_jupyter_data_dir.return_value = os.path.abspath(fake_dir_name)
    install_echarts_if_needed()

    # check if the signature file is there
    fake_signature_file = os.path.join(
        fake_nbextension_folder, '.pyecharts.signature')
    assert os.path.exists(fake_signature_file), True
    all_files = os.listdir(fake_nbextension_folder)
    eq_(len(all_files), 40)

    # clean it up
    for js in all_files:
        os.unlink(os.path.join(fake_nbextension_folder, js))
    shutil.rmtree(fake_dir_name)
