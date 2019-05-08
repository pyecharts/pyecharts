from nose.tools import eq_

from pyecharts.charts.base import Base


def test_base_add_functions():
    c = Base()
    c.add_js_funcs("console.log('hello')", "console.log('hello')")
    eq_(1, len(c.js_functions.items))
    eq_(["console.log('hello')"], c.js_functions.items)
