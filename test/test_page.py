from nose.tools import eq_

from example.commons import Faker
from pyecharts.charts import Bar, Line, Page


def _create_bar() -> Bar:
    return Bar().add_xaxis(Faker.choose()).add_yaxis("商家A", Faker.values())


def _create_line() -> Line:
    return Line().add_xaxis(Faker.choose()).add_yaxis("商家A", Faker.values())


def test_page_layout_default():
    page = Page()
    eq_(page.layout, "")


def test_page_layout_custom():
    page = Page(layout=Page.SimplePageLayout)
    eq_(page.layout, "justify-content:center; display:flex; flex-wrap:wrap; ")


def test_page_jshost_default():
    bar = _create_bar()
    line = _create_line()
    page = Page().add(bar, line)
    eq_(page.js_host, "https://assets.pyecharts.org/assets/")


def test_page_jshost_custom():
    from pyecharts.globals import CurrentConfig

    custom_host = "http://localhost:8888/assets/"
    CurrentConfig.ONLINE_HOST = custom_host
    bar = _create_bar()
    line = _create_line()
    page = Page().add(bar, line)
    eq_(page.js_host, custom_host)
