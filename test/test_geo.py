#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Geo, Style

style = Style(
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color='#404a59'
    )


cities = [
    ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12),
    ("齐齐哈尔", 14), ("盐城", 15), ("赤峰", 16), ("青岛", 18),
    ("乳山", 18), ("金昌", 19), ("泉州", 21), ("莱西", 21),
    ("日照", 21), ("胶南", 22), ("南通", 23), ("拉萨", 24),
    ("云浮", 24), ("梅州", 25), ("文登", 25), ("上海", 25),
    ("攀枝花", 25), ("威海", 25), ("承德", 25), ("厦门", 26),
    ("汕尾", 26), ("潮州", 26), ("丹东", 27), ("太仓", 27),
    ("曲靖", 27), ("烟台", 28), ("福州", 29), ("瓦房店", 30),
    ("即墨", 30), ("抚顺", 31), ("玉溪", 31), ("张家口", 31),
    ("阳泉", 31), ("莱州", 32), ("湖州", 32), ("汕头", 32),
    ("昆山", 33), ("宁波", 33), ("湛江", 33), ("揭阳", 34),
    ("荣成", 34), ("连云港", 35), ("葫芦岛", 35), ("常熟", 36),
    ("东莞", 36), ("河源", 36), ("淮安", 36), ("泰州", 36),
    ("南宁", 37), ("营口", 37), ("惠州", 37), ("江阴", 37),
    ("蓬莱", 37), ("韶关", 38), ("嘉峪关", 38), ("广州", 38),
    ("延安", 38), ("太原", 39), ("清远", 39), ("中山", 39),
    ("昆明", 39), ("寿光", 40), ("盘锦", 40), ("长治", 41),
    ("深圳", 41), ("珠海", 42), ("宿迁", 43), ("咸阳", 43),
    ("铜川", 44), ("平度", 44), ("佛山", 44), ("海口", 44),
    ("江门", 45), ("章丘", 45), ("肇庆", 46), ("大连", 47),
    ("临汾", 47), ("吴江", 47), ("石嘴山", 49), ("沈阳", 50),
    ("苏州", 50), ("茂名", 50), ("嘉兴", 51), ("长春", 51),
    ("胶州", 52), ("银川", 52), ("张家港", 52), ("三门峡", 53),
    ("锦州", 54), ("南昌", 54), ("柳州", 54), ("三亚", 54),
    ("自贡", 56), ("吉林", 56), ("阳江", 57), ("泸州", 57),
    ("西宁", 57), ("宜宾", 58), ("呼和浩特", 58), ("成都", 58),
    ("大同", 58), ("镇江", 59), ("桂林", 59), ("张家界", 59),
    ("宜兴", 59), ("北海", 60), ("西安", 61), ("金坛", 62),
    ("东营", 62), ("牡丹江", 63), ("遵义", 63), ("绍兴", 63),
    ("扬州", 64), ("常州", 64), ("潍坊", 65), ("重庆", 66),
    ("台州", 67), ("南京", 67), ("滨州", 70), ("贵阳", 71),
    ("无锡", 71), ("本溪", 71), ("克拉玛依", 72), ("渭南", 72),
    ("马鞍山", 72), ("宝鸡", 72), ("焦作", 75), ("句容", 75),
    ("北京", 79), ("徐州", 79), ("衡水", 80), ("包头", 80),
    ("绵阳", 80), ("乌鲁木齐", 84), ("枣庄", 84), ("杭州", 84),
    ("淄博", 85), ("鞍山", 86), ("溧阳", 86), ("库尔勒", 86),
    ("安阳", 90), ("开封", 90), ("济南", 92), ("德阳", 93),
    ("温州", 95), ("九江", 96), ("邯郸", 98), ("临安", 99),
    ("兰州", 99), ("沧州", 100), ("临沂", 103), ("南充", 104),
    ("天津", 105), ("富阳", 106), ("泰安", 112), ("诸暨", 112),
    ("郑州", 113), ("哈尔滨", 114), ("聊城", 116), ("芜湖", 117),
    ("唐山", 119), ("平顶山", 119), ("邢台", 119), ("德州", 120),
    ("济宁", 120), ("荆州", 127), ("宜昌", 130), ("义乌", 132),
    ("丽水", 133), ("洛阳", 134), ("秦皇岛", 136), ("株洲", 143),
    ("石家庄", 147), ("莱芜", 148), ("常德", 152), ("保定", 153),
    ("湘潭", 154), ("金华", 157), ("岳阳", 169), ("长沙", 175),
    ("衢州", 177), ("廊坊", 193), ("菏泽", 194), ("合肥", 229),
    ("武汉", 273), ("大庆", 279)
    ]


def test_geo_china_scatter():
    geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
    attr, value = geo.cast(cities)
    geo.add("", attr, value, visual_range=[0, 200],
            visual_text_color="#fff", is_legend_show=False,
            symbol_size=15, is_visualmap=True, tooltip_formatter='{b}',
            label_emphasis_textsize=15, label_emphasis_pos='right')
    html_content = geo._repr_html_()
    assert '"type": "scatter"' in html_content
    assert '"type": "heatmap"' not in html_content
    assert '"type": "effectScatter"' not in html_content


def test_geo_china_heatmap():
    geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
    attr, value = geo.cast(cities)
    geo.add("", attr, value, type="heatmap", is_visualmap=True,
            visual_range=[0, 300], visual_text_color='#fff')
    assert '"type": "heatmap"' in geo._repr_html_()


def test_geo_china_effectscatter():
    data = [
        ("海门", 9), ("鄂尔多斯", 12), ("招远", 12),
        ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)
    ]
    geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
    attr, value = geo.cast(data)
    geo.add("", attr, value, type="effectScatter", is_random=True,
            effect_scale=5)
    assert '"type": "effectScatter"' in geo._repr_html_()


def test_geo_with_noexist_city():
    data = [
        ("海门", 9), ("鄂尔多斯", 12), ("招远", 12),
        ("舟山", 12), ("齐齐哈尔", 14), ("伦敦", 15)
    ]
    geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
    attr, value = geo.cast(data)
    geo.add("", attr, value, type="effectScatter", is_random=True,
            effect_scale=5)
    geo.render()


def test_geo_guangdong_province():
    data = [
        ('汕头市', 50), ('汕尾市', 60), ('揭阳市', 35),
        ('阳江市', 44), ('肇庆市', 72)
    ]
    geo = Geo("广东城市空气质量", "data from pm2.5", **style.init_style)
    attr, value = geo.cast(data)
    geo.add("", attr, value, maptype='广东', type="effectScatter",
            is_random=True, effect_scale=5, is_legend_show=False)
    geo.render()


def test_geo_shantou_city():
    data = [
        ('澄海区', 30), ('南澳县', 40), ('龙湖区', 50), ('金平区', 60)
    ]
    geo = Geo("汕头市地图示例", **style.init_style)
    attr, value = geo.cast(data)
    geo.add("", attr, value, maptype="汕头", is_visualmap=True,
            tooltip_formatter='{b}', is_legend_show=False,
            label_emphasis_textsize=15, label_emphasis_pos='right')
    geo.render()


def test_geo_user_define_coords():
    coords = {
        "0": [0.572430556, 19.246],
        "1": [0.479039352, 1.863],
        "2": [0.754143519, -20.579]
    }

    geo = Geo(**style.init_style)
    geo.add("", ["0", "1", "2"], [6, 5.8, 6.2], is_visualmap=True,
            geo_cities_coords=coords, maptype="world")
    geo.render()


def test_geo_visualmap_pieces():
    data = [
        ("海门", 9), ("鄂尔多斯", 12), ("招远", 12),
        ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)
    ]
    geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
    attr, value = geo.cast(data)
    geo.add("", attr, value, type="effectScatter", is_random=True,
            is_visualmap=True, is_piecewise=True,
            visual_text_color="#fff",
            pieces=[
                {"min": 0, "max": 13, "label": "0 < x < 13"},
                {"min": 14, "max": 16, "label": "14 < x < 16"},
            ],
            effect_scale=5)
    content = geo._repr_html_()
    assert '"max": 13' in content
    assert '"label": "14 < x < 16"' in content
