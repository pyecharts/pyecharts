from typing import Iterable

from nose.tools import (
    assert_equal,
    assert_in,
    assert_not_equal,
    assert_not_in,
    assert_true,
    raises,
)

from pyecharts.charts import Bar, Line, Page
from pyecharts.commons.utils import OrderedSet
from pyecharts.globals import ThemeType
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.faker import Faker


def _create_bar() -> Bar:
    return (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
        .add_xaxis(Faker.week)
        .add_yaxis("商家A", [1, 2, 3, 4, 5, 6, 7])
    )


def _create_line() -> Line:
    return (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(Faker.week)
        .add_yaxis("商家A", [7, 6, 5, 4, 3, 2, 1])
    )


def _create_table() -> Table:
    table = Table()
    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
    ]
    table.add(headers, rows)
    return table


def test_page_layout_default():
    page = Page()
    assert_equal(page.layout, "")


def test_page_layout_custom():
    page = Page(layout=Page.SimplePageLayout)
    assert_equal(page.layout, "justify-content:center; display:flex; flex-wrap:wrap; ")


def test_page_jshost_default():
    bar = _create_bar()
    line = _create_line()
    page = Page().add(bar, line)
    assert_equal(page.js_host, "https://assets.pyecharts.org/assets/v5/")


def test_page_jshost_custom():
    from pyecharts.globals import CurrentConfig

    default_host = CurrentConfig.ONLINE_HOST
    custom_host = "http://localhost:8888/assets/"
    CurrentConfig.ONLINE_HOST = custom_host
    bar = _create_bar()
    line = _create_line()
    page = Page().add(bar, line)
    assert_equal(page.js_host, custom_host)
    CurrentConfig.ONLINE_HOST = default_host


def test_page_render_embed():
    bar = _create_bar()
    line = _create_line()
    content = Page().add(bar, line).render_embed()
    assert_true(len(content) > 8000)


def test_page_render_notebook():
    page = Page()
    page.add(_create_line(), _create_bar(), _create_table())
    html = page.render_notebook().__html__()
    assert_in("City name", html)


def test_page_load_javascript():
    bar = _create_bar()
    line = _create_line()
    content = Page().add(bar, line).load_javascript()
    assert_equal("", content.data)
    assert_equal(["https://assets.pyecharts.org/assets/v5/echarts.min.js"], content.lib)


def _get_new_page(unique: bool = True) -> Page:
    bar = _create_bar()
    line = _create_line()

    if not unique:
        bar.chart_id = "chenjiandongx_is_an_awesome_boy"
        line.chart_id = "chenjiandongx_is_an_amazing_boy"

    p = Page(layout=Page.DraggablePageLayout)
    p.add(bar, line)
    return p


# chart_config.json content
LAYOUT_DICT = [
    {
        "cid": "chenjiandongx_is_an_awesome_boy",
        "width": "900px",
        "height": "500px",
        "top": "31px",
        "left": "8px",
    },
    {
        "cid": "chenjiandongx_is_an_amazing_boy",
        "width": "900px",
        "height": "500px",
        "top": "30px",
        "left": "910px",
    },
]


def test_page_draggable_layout_unique_chart_id():
    page1 = _get_new_page()
    html1 = page1.save_resize_html(source=page1.render(), cfg_dict=LAYOUT_DICT)

    page2 = _get_new_page()
    html2 = page2.save_resize_html(source=page2.render(), cfg_dict=LAYOUT_DICT)

    assert_not_equal(html1, html2)


def test_page_draggable_layout_same_chart_id():
    page1 = _get_new_page(unique=False)
    html1 = page1.save_resize_html(source=page1.render(), cfg_dict=LAYOUT_DICT)

    page2 = _get_new_page(unique=False)
    html2 = page2.save_resize_html(source=page2.render(), cfg_dict=LAYOUT_DICT)

    assert_equal(html1, html2)


@raises(ValueError, FileNotFoundError)
def test_page_cfg_type():
    page = Page()
    page.save_resize_html()


def test_page_iterable():
    page = Page()
    assert_true(isinstance(page, Iterable))


def test_page_attr():
    page = Page()
    assert_true(isinstance(page.js_functions, OrderedSet))
    assert_true(isinstance(page._charts, list))


def test_page_resize():
    page = Page()
    content = page.save_resize_html(
        cfg_dict=[{"cid": "xxx", "width": 100, "height": 100, "top": 100, "left": 100}]
    )
    assert_not_in(".resizable()", content)
    assert_not_in(".draggable()", content)


def test_page_resize_cfg():
    page = Page()
    content = page.save_resize_html(cfg_file="test/fixtures/resize_cfg.json")
    assert_not_in(".resizable()", content)
    assert_not_in(".draggable()", content)


@raises(ValueError)
def test_page_no_cfg_dict_or_file():
    page = Page()
    page.save_resize_html()
