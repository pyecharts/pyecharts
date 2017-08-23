#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map
import json
import codecs


def test_map():

    # map_0
    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    map = Map("全国地图示例", width=1200, height=600)
    map.add("", attr, value, maptype='china')
    map.render()

    # map_1
    value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
    attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
    map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
    map.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
    map.render()

    # map_2
    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    map = Map("广东地图示例", width=1200, height=600)
    map.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')
    map.render()
    with codecs.open('render.html', 'r', 'utf-8') as f:
        actual_content = f.read()
        echarts_position = actual_content.find('exports.echarts')
        guangdong_position = actual_content.find(json.dumps('广东'))
        assert echarts_position < guangdong_position

    # map_3
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr= ["China", "Canada", "Brazil", "Russia", "United States"]
    map = Map("世界地图示例", width=1200, height=600)
    map.add("", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
    map.render()
