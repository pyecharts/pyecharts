# coding=utf8
from __future__ import unicode_literals

import json
import codecs
from test.constants import RANGE_COLOR, CLOTHES, WEEK
from pyecharts import (
    Bar, Scatter3D, Line, Pie, Map,
    Kline, Radar, WordCloud, Liquid)
from pyecharts import Page
from pyecharts.utils import get_resource_dir
from pyecharts.engine import configure
from nose.tools import eq_


def create_three():
    # bar
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)

    # scatter3D
    import random
    data = [
        [random.randint(0, 100),
         random.randint(0, 100),
         random.randint(0, 100)] for _ in range(80)
        ]
    scatter3d = Scatter3D("3D 散点图示例", width=1200, height=600)
    scatter3d.add("", data, is_visualmap=True, visual_range_color=RANGE_COLOR)

    return Page.from_charts(bar, scatter3d)


def test_custom_templates():
    configure(jshost='https://chfw.github.io/jupyter-echarts/echarts')
    page = create_three()
    # page.js_dependencies = ['echarts.min']
    page.render(new_version=True, path='new_version_page.html')
    with codecs.open('new_version_page.html', 'r', 'utf-8') as f:
        actual_content = f.read()
        assert "</html>" in actual_content
