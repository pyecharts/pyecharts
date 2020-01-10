from pyecharts.commons.utils import JsCode

from pyecharts import options as opts
from pyecharts.charts import Bar, BMap, Grid, Map, Page, Pie, Sankey, Timeline
from pyecharts.faker import Collector, Faker

C = Collector()


@C.funcs
def timeline_bar() -> Timeline:
    x = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl


@C.funcs
def timeline_bar_reversal() -> Timeline:
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis(
                "商家A", Faker.values(), label_opts=opts.LabelOpts(position="right")
            )
            .add_yaxis(
                "商家B", Faker.values(), label_opts=opts.LabelOpts(position="right")
            )
            .reversal_axis()
            .set_global_opts(
                title_opts=opts.TitleOpts("Timeline-Bar-Reversal (时间: {} 年)".format(i))
            )
        )
        tl.add(bar, "{}年".format(i))
    return tl


@C.funcs
def timeline_bar_with_graphic() -> Timeline:
    x = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(
                title_opts=opts.TitleOpts("某商店{}年营业额 - With Graphic 组件".format(i)),
                graphic_opts=[
                    opts.GraphicGroup(
                        graphic_item=opts.GraphicItem(
                            rotation=JsCode("Math.PI / 4"),
                            bounding="raw",
                            right=100,
                            bottom=110,
                            z=100,
                        ),
                        children=[
                            opts.GraphicRect(
                                graphic_item=opts.GraphicItem(
                                    left="center", top="center", z=100
                                ),
                                graphic_shape_opts=opts.GraphicShapeOpts(
                                    width=400, height=50
                                ),
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="rgba(0,0,0,0.3)"
                                ),
                            ),
                            opts.GraphicText(
                                graphic_item=opts.GraphicItem(
                                    left="center", top="center", z=100
                                ),
                                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                    text="某商店{}年营业额".format(i),
                                    font="bold 26px Microsoft YaHei",
                                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                        fill="#fff"
                                    ),
                                ),
                            ),
                        ],
                    )
                ],
            )
        )
        tl.add(bar, "{}年".format(i))
    return tl


@C.funcs
def timeline_pie() -> Timeline:
    attr = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        pie = (
            Pie()
            .add(
                "商家A",
                [list(z) for z in zip(attr, Faker.values())],
                rosetype="radius",
                radius=["30%", "55%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(pie, "{}年".format(i))
    return tl


@C.funcs
def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2015, 2020):
        map0 = (
            Map()
            .add(
                "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Map-{}年某些数据".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=200),
            )
        )
        tl.add(map0, "{}年".format(i))
    return tl


@C.funcs
def timeline_with_multi_axis() -> Timeline:
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl


@C.funcs
def timeline_sankey() -> Timeline:
    tl = Timeline()
    names = ("商家A", "商家B", "商家C")
    nodes = [{"name": name} for name in names]
    for i in range(2015, 2020):
        links = [
            {"source": names[0], "target": names[1], "value": Faker.values()[0]},
            {"source": names[1], "target": names[2], "value": Faker.values()[0]},
        ]
        sankey = (
            Sankey()
            .add(
                "sankey",
                nodes,
                links,
                linestyle_opt=opts.LineStyleOpts(
                    opacity=0.2, curve=0.5, color="source"
                ),
                label_opts=opts.LabelOpts(position="right"),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年商店（A, B, C）营业额差".format(i))
            )
        )
        tl.add(sankey, "{}年".format(i))
    return tl


@C.funcs
def timeline_bmap() -> Timeline:
    tl = Timeline()
    tl.add_schema(pos_left="50%", pos_right="10px", pos_bottom="15px")
    for i in range(2015, 2020):
        bmap = (
            BMap()
            .add_schema(baidu_ak="FAKE_AK", center=[120.13066322374, 30.240018034923])
            .add(
                "bmap",
                [list(z) for z in zip(Faker.provinces, Faker.values())],
                type_="heatmap",
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Timeline-BMap-热力图-{}年".format(i)),
                visualmap_opts=opts.VisualMapOpts(
                    pos_bottom="center", pos_right="10px"
                ),
                tooltip_opts=opts.TooltipOpts(formatter=None),
            )
        )
        tl.add(bmap, "{}年".format(i))
    return tl


Page().add(*[fn() for fn, _ in C.charts]).render()
