from nose.tools import assert_not_in, eq_

from pyecharts.charts.base import Base


def test_base_add_functions():
    c = Base()
    c.add_js_funcs("console.log('hello')", "console.log('hello')")
    eq_(1, len(c.js_functions.items))
    eq_(["console.log('hello')"], c.js_functions.items)


def test_base_init_funcs():
    c0 = Base({"width": "100px", "height": "200px"})
    eq_(c0.width, "100px")
    eq_(c0.height, "200px")

    c1 = Base(dict(width="110px", height="210px"))
    eq_(c1.width, "110px")
    eq_(c1.height, "210px")
    assert_not_in(c1.js_host, ["", None])
