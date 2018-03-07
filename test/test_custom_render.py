# coding=utf8
from __future__ import unicode_literals

import codecs

from pyecharts import (Bar, Scatter3D)
from pyecharts import Page
from pyecharts.conf import CURRENT_CONFIG
from pyecharts.conf import configure
from test.constants import RANGE_COLOR, CLOTHES


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
    configure(
        jshost='https://chfw.github.io/jupyter-echarts/echarts',
        force_js_embed=False
    )
    page = create_three()
    # page.js_dependencies = ['echarts.min']
    page.render(path='new_version_page.html')
    with codecs.open('new_version_page.html', 'r', 'utf-8') as f:
        actual_content = f.read()
        assert "</html>" in actual_content
    CURRENT_CONFIG.jshost = None


def test_custom_template_for_chart():
    data = [{
        'name': '衬衫',
        'value': 5
    }, {
        'name': '羊毛衫',
        'value': 20
    }, {
        'name': '雪纺衫',
        'value': 36
    }]

    configure(echarts_template_dir='.')

    data1 = {'衬衫': '34', '羊毛衫': 45, '雪纺衫': 40}
    names, values = Bar.cast(data)
    names1, values1 = Bar.cast(data1)
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", names, values, is_stack=True)
    bar.add("商家B", names1, values1, is_stack=True)
    bar.render(path='new_version_bar.html')
    with codecs.open('new_version_bar.html', 'r', 'utf-8') as f:
        actual_content = f.read()
        assert "</html>" in actual_content
