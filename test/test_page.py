# coding=utf-8
from __future__ import unicode_literals

import codecs
import json
import random
import sys
from test.constants import CLOTHES, RANGE_COLOR, WEEK

from nose.tools import assert_list_equal, eq_, raises

from mock import MagicMock
from pyecharts import (
    Bar,
    Kline,
    Line,
    Liquid,
    Map,
    Page,
    Pie,
    Radar,
    Scatter3D,
    WordCloud,
)

TEST_PAGE_TITLE = "my awesome chart"

PY36 = sys.version_info >= (3, 6)


def test_page_init():
    line = MagicMock(page_title="Line-Chart")
    bar = MagicMock(page_title="Bar-Chart")
    page = Page(line=line, bar=bar)
    eq_("Line-Chart", page["line"].page_title)
    assert "line" in page
    assert "bar" in page
    if PY36:
        eq_("Line-Chart", page[0].page_title)


def test_page_add_chart():
    nc = (
        Page()
        .add_chart(MagicMock(page_title="Line-Chart"), name="line")
        .add_chart(MagicMock(page_title="Bar-Chart"))
    )
    nc["map"] = MagicMock(page_title="Map-Chart")
    eq_("Line-Chart", nc["line"].page_title)
    eq_("Bar-Chart", nc["c1"].page_title)
    assert_list_equal(
        ["Line-Chart", "Bar-Chart", "Map-Chart"], [c.page_title for c in nc]
    )


def create_three_charts():
    page = Page(page_title=TEST_PAGE_TITLE)

    # bar
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)
    page.add(bar)

    # scatter3D
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    scatter3d = Scatter3D("3D 散点图示例", width=1200, height=600)
    scatter3d.add("", data, is_visualmap=True, visual_range_color=RANGE_COLOR)
    page.add(scatter3d)

    # guangdong
    value = [20, 190, 253, 77, 65]
    attr = ["汕头市", "汕尾市", "揭阳市", "阳江市", "肇庆市"]
    map = Map("广东地图示例", width=1200, height=600)
    map.add("", attr, value, maptype="广东", is_visualmap=True, visual_text_color="#000")
    page.add(map)

    return page


@raises(NotImplementedError)
def test_no_image_rendering_for_page():
    page = create_three_charts()
    page.render(path="page.png")


def test_two_bars():
    page = create_three_charts()
    page.render()
    with codecs.open("render.html", "r", "utf-8") as f:
        actual_content = f.read()
        assert json.dumps("柱状图数据堆叠示例") in actual_content
        assert "<html>" in actual_content
        assert TEST_PAGE_TITLE in actual_content
        # test the optimization
        assert "registerMap('china'," not in actual_content
        assert "registerMap('world'," not in actual_content
        echarts_position = actual_content.find("exports.options")
        guangdong_position = actual_content.find(json.dumps("广东"))
        assert echarts_position < guangdong_position


def test_page_get_js_dependencies():
    page = create_three_charts()
    dependencies = page.get_js_dependencies()
    eq_(dependencies[0], "options.min")
    assert "guangdong" in dependencies
    assert "options-gl.min" in dependencies
    eq_(len(dependencies), 3)


def test_page_embed():
    page = create_three_charts()
    html = page.render_embed()
    assert "<html>" not in html
    assert json.dumps("柱状图数据堆叠示例") in html


def test_page_in_notebook():
    page = create_three_charts()
    html = page._repr_html_()

    assert "echartsgl" in html
    assert "options" in html
    assert "guangdong" in html
    # find the appearing postion of options.min in html
    echarts_position = html.find("options.min")
    # find the appearing postion of guangdong in html
    guangdong_position = html.find("guangdong")
    assert echarts_position < guangdong_position


def test_more_charts():
    page = Page()

    # line
    line = Line("折线图示例")
    line.add(
        "最高气温",
        WEEK,
        [11, 11, 15, 13, 12, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    line.add(
        "最低气温",
        WEEK,
        [1, -2, 2, 5, 3, 2, 0],
        mark_point=["max", "min"],
        mark_line=["average"],
    )

    # pie
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图-圆环图示例", title_pos="center")
    pie.add(
        "",
        CLOTHES,
        v1,
        radius=[40, 75],
        label_text_color=None,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
    )

    page.add([line, pie])

    # kline
    v1 = [
        [2320.26, 2320.26, 2287.3, 2362.94],
        [2300, 2291.3, 2288.26, 2308.38],
        [2295.35, 2346.5, 2295.35, 2345.92],
        [2347.22, 2358.98, 2337.35, 2363.8],
        [2360.75, 2382.48, 2347.89, 2383.76],
        [2383.43, 2385.42, 2371.23, 2391.82],
        [2377.41, 2419.02, 2369.57, 2421.15],
        [2425.92, 2428.15, 2417.58, 2440.38],
        [2411, 2433.13, 2403.3, 2437.42],
        [2432.68, 2334.48, 2427.7, 2441.73],
        [2430.69, 2418.53, 2394.22, 2433.89],
        [2416.62, 2432.4, 2414.4, 2443.03],
        [2441.91, 2421.56, 2418.43, 2444.8],
        [2420.26, 2382.91, 2373.53, 2427.07],
        [2383.49, 2397.18, 2370.61, 2397.94],
        [2378.82, 2325.95, 2309.17, 2378.82],
        [2322.94, 2314.16, 2308.76, 2330.88],
        [2320.62, 2325.82, 2315.01, 2338.78],
        [2313.74, 2293.34, 2289.89, 2340.71],
        [2297.77, 2313.22, 2292.03, 2324.63],
        [2322.32, 2365.59, 2308.92, 2366.16],
        [2364.54, 2359.51, 2330.86, 2369.65],
        [2332.08, 2273.4, 2259.25, 2333.54],
        [2274.81, 2326.31, 2270.1, 2328.14],
        [2333.61, 2347.18, 2321.6, 2351.44],
        [2340.44, 2324.29, 2304.27, 2352.02],
        [2326.42, 2318.61, 2314.59, 2333.67],
        [2314.68, 2310.59, 2296.58, 2320.96],
        [2309.16, 2286.6, 2264.83, 2333.29],
        [2282.17, 2263.97, 2253.25, 2286.33],
        [2255.77, 2270.28, 2253.31, 2276.22],
    ]
    kline = Kline("K 线图示例")
    kline.add(
        "日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, is_datazoom_show=True
    )
    page.add(kline)

    # radar
    schema = [
        ("销售", 6500),
        ("管理", 16000),
        ("信息技术", 30000),
        ("客服", 38000),
        ("研发", 52000),
        ("市场", 25000),
    ]
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    radar = Radar("雷达图示例")
    radar.config(schema)
    radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
    radar.add(
        "实际开销",
        v2,
        label_color=["#4e79a7"],
        is_area_show=False,
        legend_selectedmode="single",
    )
    page.add(radar)

    # scatter3d
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=RANGE_COLOR)
    page.add(scatter3D)

    # wordcloud
    name = [
        "Sam S Club",
        "Macys",
        "Amy Schumer",
        "Jurassic World",
        "Charter Communications",
        "Chick Fil A",
        "Planet Fitness",
        "Pitch Perfect",
        "Express",
        "Home",
        "Johnny Depp",
        "Lena Dunham",
        "Lewis Hamilton",
        "KXAN",
        "Mary Ellen Mark",
        "Farrah Abraham",
        "Rita Ora",
        "Serena Williams",
        "NCAA baseball tournament",
        "Point Break",
    ]
    value = [
        10000,
        6181,
        4386,
        4055,
        2467,
        2244,
        1898,
        1484,
        1112,
        965,
        847,
        582,
        555,
        550,
        462,
        366,
        360,
        282,
        273,
        265,
    ]
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[30, 100], rotate_step=66)
    page.add(wordcloud)

    # liquid
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6])
    page.add(liquid)
    assert len(page) == 7
    assert isinstance(page[0], Line)
    assert ("options" in page.js_dependencies) or (
        "options.min" in page.js_dependencies
    )
    page.render()


def test_page_extra_html_text_label():
    page = Page()
    line = Line("折线图示例", extra_html_text_label=["LINE TEXT LABEL", "color:red"])
    line.add(
        "最高气温",
        WEEK,
        [11, 11, 15, 13, 12, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    page.add(line)

    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图-圆环图示例", title_pos="center", extra_html_text_label=["PIE TEXT LABEL"])
    pie.add(
        "",
        CLOTHES,
        v1,
        radius=[40, 75],
        label_text_color=None,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
    )
    page.add(pie)

    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图", extra_html_text_label=["BAR TEXT LABEL"])
    bar.add("商家B", CLOTHES, v2)
    page.add(bar)

    html_content = page._repr_html_()
    assert '<p style="">BAR TEXT LABEL</p>' in html_content
    assert '<p style="color:red">LINE TEXT LABEL</p>' in html_content
    assert '<p style="">PIE TEXT LABEL</p>' in html_content
