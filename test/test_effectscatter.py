from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_effectscatter_base(fake_writer):
    c = EffectScatter().add_xaxis(Faker.choose()).add_yaxis("", Faker.values())
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
