from unittest.mock import patch

from nose.tools import eq_

from example.commons import Faker
from pyecharts.charts import Map


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_map_base(fake_writer):
    c = Map().add(
        "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
    )
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
