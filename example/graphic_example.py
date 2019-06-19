from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Page
from pyecharts.commons.utils import JsCode

C = Collector()


@C.funcs
def bar_graphic_rect_text_one_component() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic Rect+Text 1 组件示例"),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=110,
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
                                text="pyecharts bar chart",
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
    return c


@C.funcs
def bar_graphic_rect_text_two_component() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic Rect+Text 2 组件示例"),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(left="50%", top="15%"),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(
                                z=100, left="center", top="middle"
                            ),
                            graphic_shape_opts=opts.GraphicShapeOpts(
                                width=190, height=90
                            ),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="#fff",
                                stroke="#555",
                                line_width=2,
                                shadow_blur=8,
                                shadow_offset_x=3,
                                shadow_offset_y=3,
                                shadow_color="rgba(0,0,0,0.3)",
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(
                                left="center", top="middle", z=100
                            ),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text=JsCode(
                                    "['横轴表示数据类别',"
                                    "'纵轴表示数值的值',"
                                    "'这个文本块可以放在图中各',"
                                    "'种位置'].join('\\n')"
                                ),
                                font="14px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="#333"
                                ),
                            ),
                        ),
                    ],
                )
            ],
        )
    )
    return c


@C.funcs
def bar_graphic_image_component() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic Image 组件示例"),
            graphic_opts=[
                opts.GraphicImage(
                    graphic_item=opts.GraphicItem(
                        id_="logo",
                        right=20,
                        top=20,
                        z=-10,
                        bounding="raw",
                        origin=[75, 75],
                    ),
                    graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                        image="http://echarts.baidu.com/images/favicon.png",
                        width=150,
                        height=150,
                        opacity=0.4,
                    ),
                )
            ],
        )
    )
    return c


@C.funcs
def bar_graphic_image_with_js_component() -> Grid:
    bar = (
        Bar(init_opts=opts.InitOpts(chart_id="1234"))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic Image（旋转功能）组件示例"),
            graphic_opts=[
                opts.GraphicImage(
                    graphic_item=opts.GraphicItem(
                        id_="logo",
                        right=20,
                        top=20,
                        z=-10,
                        bounding="raw",
                        origin=[75, 75],
                    ),
                    graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                        image="http://echarts.baidu.com/images/favicon.png",
                        width=150,
                        height=150,
                        opacity=0.4,
                    ),
                )
            ],
        )
    )
    c = (
        Grid(init_opts=opts.InitOpts(chart_id="1234"))
        .add(
            chart=bar,
            grid_opts=opts.GridOpts(pos_left="5%", pos_right="4%", pos_bottom="5%"),
        )
        .add_js_funcs(
            """
            var rotation = 0;
            setInterval(function () {
                chart_1234.setOption({
                    graphic: {
                        id: 'logo',
                        rotation: (rotation += Math.PI / 360) % (Math.PI * 2)
                    }
                });
            }, 30);
        """
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
