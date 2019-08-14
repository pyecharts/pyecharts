import unittest

from nose.tools import eq_

from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.commons.utils import JsCode


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
        eq_(None, self.tl.options.get("baseOption").get("timeline").get("label"))

    def test_custom_label(self):
        custom_label_opts = {"custom": "label"}
        self.tl.add_schema(label_opts=custom_label_opts)
        eq_(
            custom_label_opts,
            self.tl.options.get("baseOption").get("timeline").get("label"),
        )

    def test_timeline_vertical(self):
        self.tl.add_schema(orient="vertical")
        eq_("vertical", self.tl.options.get("baseOption").get("timeline").get("orient"))

    def test_timeline_inverse(self):
        self.tl.add_schema(is_inverse=True)
        eq_(True, self.tl.options.get("baseOption").get("timeline").get("inverse"))

    def test_timeline_width_height(self):
        width, height = "20", "30"
        self.tl.add_schema(width=width, height=height)
        eq_(width, self.tl.options.get("baseOption").get("timeline").get("width"))
        eq_(height, self.tl.options.get("baseOption").get("timeline").get("height"))

    def test_timeline_visual_map(self):
        eq_(
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
        eq_(
            type(opts.GraphicGroup()),
            type(self.tl.options.get("baseOption").get("timeline").get("graphic")[0]),
        )
