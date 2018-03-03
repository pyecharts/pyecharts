# coding=utf-8
from __future__ import unicode_literals

from pyecharts import ChoroplethMap

from test.utils import get_default_rendering_file_content


def test_choropleth_map():
    # show label
    value = ['A', 'B', 'C', 'THIS_KEY_IS_NOT_IN_HTML', 'A']
    attr = ["福建", "山东", "北京", "上海", "西藏"]
    legends = {
        'A': 'test a',
        'B': 'test b',
        'C': 'test c',
        'THIS_KEY_IS_NOT_IN_HTML': 'test d'
    }
    map = ChoroplethMap("Choropleth map - 等值区域图示例", width=1200, height=600)
    map.add("", attr, value, legends, maptype='china',
            visual_range_color=['red', 'blue', 'yellow', 'green'],
            is_label_show=True)
    map.render()
    content = get_default_rendering_file_content()
    assert '"type": "piecewise"' in content
    assert '"label": "test a",' in content
    assert '"max": 2.1, ' in content
    assert 'THIS_KEY_IS_NOT_IN_HTML' not in content
