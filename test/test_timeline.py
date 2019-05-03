from nose.tools import eq_

from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline


class TestTimeLine:
    def setUp(self):
        bar0 = (
            Bar()
            .add_xaxis(["a", "b"])
            .add_yaxis("shop a", [1, 2])
            .add_yaxis("shop b", [3, 4])
            .set_global_opts(title_opts=opts.TitleOpts("test"))
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
