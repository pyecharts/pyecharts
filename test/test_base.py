from unittest.mock import patch

from nose.tools import assert_equal, assert_not_in

from pyecharts.charts import Bar
from pyecharts.charts.base import Base


def test_base_add_functions():
    c = Base()
    c.add_js_funcs("console.log('hello')", "console.log('hello')")
    assert_equal(1, len(c.js_functions.items))
    assert_equal(["console.log('hello')"], c.js_functions.items)


def test_base_init_funcs():
    c0 = Base({"width": "100px", "height": "200px"})
    assert_equal(c0.width, "100px")
    assert_equal(c0.height, "200px")

    c1 = Base(dict(width="110px", height="210px"))
    assert_equal(c1.width, "110px")
    assert_equal(c1.height, "210px")
    assert_not_in(c1.js_host, ["", None])


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_render(fake_writer):
    my_render_content = "my_render_content"
    bar = Bar()
    bar.add_xaxis(["1"]).add_yaxis("", [1]).render(my_render_content=my_render_content)
    assert "test ok" == "test ok"
