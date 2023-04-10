from nose.tools import assert_equal, assert_in

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


def test_display_javascript_v1():
    js_content = "console.log('hello world')"
    obj = Javascript(js_content, lib="test lib", css="test css")
    assert_equal(obj.data, js_content)

    obj_1 = Javascript(
        data=js_content,
        lib=["lib1", "lib2"],
        css=["css1", "css2"],
    )
    assert_equal(obj_1.data, js_content)
    assert_in(js_content, obj_1._repr_javascript_())
