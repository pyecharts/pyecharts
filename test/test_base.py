from datetime import datetime
from unittest.mock import patch

from nose.tools import assert_equal, assert_in, assert_not_in

from pyecharts.charts import Bar
from pyecharts.commons import utils
from pyecharts.datasets import EXTRA
from pyecharts.options import InitOpts, RenderOpts
from pyecharts.globals import CurrentConfig
from pyecharts.charts.base import Base, default
from pyecharts.options.global_options import AnimationOpts


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


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_render_js_host_none(fake_writer):
    my_render_content = "my_render_content"
    bar = Bar()
    bar.add_xaxis(["1"]).add_yaxis("", [1])
    # Hack to test
    bar.js_host = None
    # Render
    bar.render(my_render_content=my_render_content)
    assert_equal(bar.js_host, CurrentConfig.ONLINE_HOST)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_render_embed_js(_):
    c = Base(render_opts=RenderOpts(is_embed_js=True))
    # Embedded JavaScript
    content = c.render_embed()
    assert_not_in(CurrentConfig.ONLINE_HOST, content, "Embedding JavaScript fails")
    # No embedded JavaScript
    c.render_options.update(embed_js=False)
    content = c.render_embed()
    assert_in(
        CurrentConfig.ONLINE_HOST, content, "Embedded JavaScript cannot be closed"
    )


def test_base_render_options():
    c0 = Base(render_opts=RenderOpts(is_embed_js=True))
    assert_equal(c0.render_options.get("embed_js"), True)


def test_base_iso_format():
    mock_time_str = "2022-04-14 14:42:00"
    mock_time = datetime.strptime(mock_time_str, "%Y-%m-%d %H:%M:%S")
    assert default(mock_time) == "2022-04-14T14:42:00"


def test_base_animation_option():
    c0 = Base(init_opts=InitOpts(animation_opts=AnimationOpts(animation=False)))
    assert_equal(c0.options.get("animation"), False)

    c1 = Base({"animationOpts": {"animation": False}})
    assert_equal(c1.options.get("animation"), False)


def test_base_chart_id():
    c0 = Base(init_opts=InitOpts(chart_id="1234567"))
    assert_equal(c0.chart_id, "1234567")

    c1 = Base(init_opts=InitOpts(chart_id="1234567"))
    assert_equal(c1.get_chart_id(), "1234567")
