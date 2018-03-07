# coding=utf8
"""
Test cases for rendering in jupyter notebook
"""
from __future__ import unicode_literals

import json

from pyecharts import Bar, Line, Pie, Page, online
from test.constants import CLOTHES, WEEK

TITLE = "柱状图数据堆叠示例"


def create_a_bar(title):
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar(title)
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)
    return bar


def test_single_chart():
    bar = create_a_bar(TITLE)
    html = bar._repr_html_()
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "require.config" in html
    assert "function(echarts)" in html
    assert "nbextensions/echarts" in html
    assert "width:800px" in html
    assert "height:400px" in html
    assert "<div" in html
    assert "myChart" in html
    assert bar.chart_id in html


def test_page():
    page = Page()
    line = Line("折线图示例")
    line.chart_id = 'id_my_cell_line'
    line.add("最高气温", WEEK, [11, 11, 15, 13, 12, 13, 10],
             mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", WEEK, [1, -2, 2, 5, 3, 2, 0],
             mark_point=["max", "min"], mark_line=["average"])

    # pie
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图-圆环图示例", title_pos='center', width='600px')
    pie.add("", CLOTHES, v1, radius=[40, 75], label_text_color=None,
            is_label_show=True, legend_orient='vertical', legend_pos='left')

    page.add([line, pie, create_a_bar(TITLE)])
    # Start render and test
    html = page._repr_html_()
    # Test base html structure
    assert html.count('<script>') == html.count('</script>') == 2
    assert html.count('<div') == html.count('</div>') == 3
    assert html.count("require.config") == html.count("function(echarts)") == 1
    # Test some chart attributes
    json_encoded_title = json.dumps(TITLE)
    assert json_encoded_title in html
    assert "nbextensions/echarts" in html  # default jshost
    assert html.count("height:400px") == 3
    assert html.count('width:600px') == 1
    assert html.count("width:800px") == 2
    assert html.count("id_my_cell_line") == 6


def test_online_feature():
    online()
    bar = create_a_bar(TITLE)
    html = bar._repr_html_()
    expected_jshost = 'https://pyecharts.github.io/jupyter-echarts/echarts'
    assert expected_jshost in html


def test_online_with_custom_jshost():
    online(host='https://my-site.com/js')
    bar = create_a_bar(TITLE)
    html = bar._repr_html_()
    expected_jshost = 'https://my-site.com/js'
    assert expected_jshost in html
