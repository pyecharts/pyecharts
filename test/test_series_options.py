from nose.tools import assert_equal

from pyecharts.options.series_options import LabelOpts


def test_label_options_defaults():
    option = LabelOpts()
    expected = {
        "show": True,
        "position": "top",
        "color": None,
        "rotate": None,
        "margin": 8,
        "interval": None,
        "fontSize": None,
        "fontStyle": None,
        "fontWeight": None,
        "fontFamily": None,
        "align": None,
        "verticalAlign": None,
        "formatter": None,
        "backgroundColor": None,
        "borderColor": None,
        "borderWidth": None,
        "borderRadius": None,
        "rich": None,
    }
    assert_equal(expected, option.opts)


def test_label_options_custom():
    option = LabelOpts(
        background_color="red", border_color="green", border_width=1, border_radius=2
    )
    expected = {
        "show": True,
        "position": "top",
        "color": None,
        "rotate": None,
        "margin": 8,
        "interval": None,
        "fontSize": None,
        "fontStyle": None,
        "fontWeight": None,
        "fontFamily": None,
        "align": None,
        "verticalAlign": None,
        "formatter": None,
        "backgroundColor": "red",
        "borderColor": "green",
        "borderWidth": 1,
        "borderRadius": 2,
        "rich": None,
    }
    assert_equal(expected, option.opts)
