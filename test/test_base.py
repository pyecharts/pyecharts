#!/usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals

import json
from pyecharts import Bar


def test_embed_option():

    # bar_0
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
