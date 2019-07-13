from unittest.mock import patch

from nose.tools import assert_in, eq_

from example.commons import Faker
from pyecharts.charts import MapGlobe
from pyecharts.globals import CurrentConfig, NotebookType


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_map_base(fake_writer):
    c = MapGlobe().add(
        "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("document.createElement('canvas')", content)
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    assert_in("baseTexture", content)


def test_map_globe_in_jupyter():
    CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK

    c = MapGlobe().add(
        "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
    )
    content = c.render_notebook()._repr_html_()
    assert_in("document.createElement('canvas')", content)
    assert_in("baseTexture", content)
