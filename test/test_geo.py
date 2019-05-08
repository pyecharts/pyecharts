from nose.tools import eq_

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo


def test_geo_base():
    c = (
        Geo()
        .add_schema(maptype="china")
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
