import random
import unittest

from pyecharts import options as opts
from pyecharts.charts import Bar, Bar3D, Timeline
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker


def get_bar_3d_chart(i: int):
    data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
        .add(
            "",
            [[d[1], d[0], d[2]] for d in data],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=20),
            title_opts=opts.TitleOpts(title=f"Bar3D-{i}"),
        )
    )

    return c


class TestTimeLine(unittest.TestCase):
    def setUp(self):
        bar0 = (
            Bar()
            .add_xaxis(["a", "b"])
            .add_yaxis("shop a", [1, 2])
            .add_yaxis("shop b", [3, 4])
            .set_global_opts(
                title_opts=opts.TitleOpts("test"), visualmap_opts=opts.VisualMapOpts()
            )
        )
        self.tl = Timeline().add(bar0, "year 2015")

    def test_default_label(self):
        self.assertEqual(
            None, self.tl.options.get("baseOption").get("timeline").get("label")
        )

    def test_custom_label(self):
        custom_label_opts = {"custom": "label"}
        self.tl.add_schema(label_opts=custom_label_opts)
        self.assertEqual(
            custom_label_opts,
            self.tl.options.get("baseOption").get("timeline").get("label"),
        )

    def test_timeline_vertical(self):
        self.tl.add_schema(orient="vertical")
        self.assertEqual(
            "vertical", self.tl.options.get("baseOption").get("timeline").get("orient")
        )

    def test_timeline_inverse(self):
        self.tl.add_schema(is_inverse=True)
        self.assertEqual(
            True, self.tl.options.get("baseOption").get("timeline").get("inverse")
        )

    def test_timeline_width_height(self):
        width, height = "20", "30"
        self.tl.add_schema(width=width, height=height)
        self.assertEqual(
            width, self.tl.options.get("baseOption").get("timeline").get("width")
        )
        self.assertEqual(
            height, self.tl.options.get("baseOption").get("timeline").get("height")
        )

    def test_timeline_visual_map(self):
        self.assertEqual(
            type(opts.VisualMapOpts()),
            type(self.tl.options.get("options")[0].get("visualMap")),
        )

    def test_timeline_graphic(self):
        self.tl.add_schema(
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
            ]
        )
        self.assertEqual(
            type(opts.GraphicGroup()),
            type(self.tl.options.get("baseOption").get("timeline").get("graphic")[0]),
        )

    def test_timeline_graphic_v1(self):
        self.tl.add_schema(
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
                            ),
                        ),
                    ],
                )
            ]
        )
        self.assertEqual(
            type(opts.GraphicGroup()),
            type(self.tl.options.get("baseOption").get("timeline").get("graphic")[0]),
        )

    def test_page_with_multi_axis(self):
        tl = Timeline()
        for i in range(2015, 2020):
            bar = (
                Bar()
                .add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values())
                .add_yaxis("商家B", Faker.values())
            )
            tl.add(bar, "{}年".format(i))

        for t in tl.options.get("options"):
            assert "xAxis" in t
            assert "color" in t

    def test_timeline_with_3d_chart(self):
        tl = Timeline()
        for i in range(2, 5):
            bar_3d = get_bar_3d_chart(i=i)
            tl.add(bar_3d, "{}".format(i))

        for t in tl.options.get("options"):
            assert "xAxis3D" in t
            assert "yAxis3D" in t
            assert "zAxis3D" in t
