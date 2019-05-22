from nose.tools import eq_

from pyecharts.render.display import HTML, Javascript


def test_display_html():
    html_content = "<p>hello world<p/>"
    obj = HTML(html_content)
    eq_(obj.data, html_content)
    eq_(obj.__html__(), html_content)


def test_display_javascript():
    js_content = "console.log('hello world')"
    obj = Javascript(js_content)
    eq_(obj.data, js_content)
    eq_(obj._repr_javascript_(), js_content)
