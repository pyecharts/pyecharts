import random
from unittest.mock import patch

from nose.tools import assert_equal

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter3D


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter3d_base(fake_writer):
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    c = (
        Scatter3D()
        .add("", data)
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color)
        )
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
