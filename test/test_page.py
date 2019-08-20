from nose.tools import assert_not_equal, assert_true, eq_, raises

from example.commons import Faker
from pyecharts.charts import Bar, Line, Page


def _create_bar() -> Bar:
    return Bar().add_xaxis(Faker.week).add_yaxis("商家A", [1, 2, 3, 4, 5, 6, 7])


def _create_line() -> Line:
    return Line().add_xaxis(Faker.week).add_yaxis("商家A", [7, 6, 5, 4, 3, 2, 1])


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

    default_host = CurrentConfig.ONLINE_HOST
    custom_host = "http://localhost:8888/assets/"
    CurrentConfig.ONLINE_HOST = custom_host
    bar = _create_bar()
    line = _create_line()
    page = Page().add(bar, line)
    eq_(page.js_host, custom_host)
    CurrentConfig.ONLINE_HOST = default_host


def test_page_render_embed():
    bar = _create_bar()
    line = _create_line()
    content = Page().add(bar, line).render_embed()
    assert_true(len(content) > 1000)


def test_page_load_javascript():
    bar = _create_bar()
    line = _create_line()
    content = Page().add(bar, line).load_javascript()
    eq_("", content.data)
    eq_(["https://assets.pyecharts.org/assets/echarts.min.js"], content.lib)


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

    eq_(html1, html2)


@raises(ValueError)
def test_page_cfg_type():
    page = Page()
    page.save_resize_html()
