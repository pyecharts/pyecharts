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


def test_display_javascript_v2():
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    obj = Javascript(lib=['https://assets.pyecharts.org/assets/v5/echarts.min.js'])
    obj.load_javascript_contents()
    assert_in(
        "echarts",
        obj.javascript_contents["https://assets.pyecharts.org/assets/v5/echarts.min.js"],
    )

    obj_1 = Javascript(lib=['https://assets.pyecharts.org/assets/v4/echarts.min.js'])
    try:
        obj_1.load_javascript_contents()
    except RuntimeError:
        pass
