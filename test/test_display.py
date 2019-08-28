from nose.tools import assert_equal

from pyecharts.render.display import HTML, Javascript


def test_display_html():
    html_content = "<p>hello world<p/>"
    obj = HTML(html_content)
    assert_equal(obj.data, html_content)
    assert_equal(obj.__html__(), html_content)


def test_display_javascript():
    js_content = "console.log('hello world')"
    obj = Javascript(js_content)
    assert_equal(obj.data, js_content)
    assert_equal(obj._repr_javascript_(), js_content)
