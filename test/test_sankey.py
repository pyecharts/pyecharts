from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Sankey


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_sankey_base(fake_writer):
    nodes = [{"name": "category1"}, {"name": "category2"}, {"name": "category3"}]

    links = [
        {"source": "category1", "target": "category2", "value": 10},
        {"source": "category2", "target": "category3", "value": 15},
    ]
    c = Sankey().add(
        "sankey",
        nodes,
        links,
        layout_iterations=16,
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"),
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
    assert_in("layoutIteration", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_sankey_new_opts(fake_writer):
    nodes = [
        {"name": "a"},
        {"name": "b"},
        {"name": "a1"},
        {"name": "b1"},
        {"name": "c"},
        {"name": "e"},
    ]
    links = [
        {"source": "a", "target": "a1", "value": 5},
        {"source": "e", "target": "b", "value": 3},
        {"source": "a", "target": "b1", "value": 3},
        {"source": "b1", "target": "a1", "value": 1},
        {"source": "b1", "target": "c", "value": 2},
        {"source": "b", "target": "c", "value": 1},
    ]
    c = Sankey().add(
        "sankey",
        nodes,
        links,
        pos_bottom="10%",
        orient="vertical",
        levels=[
            opts.SankeyLevelsOpts(
                depth=0,
                itemstyle_opts=opts.ItemStyleOpts(color="#eee"),
                linestyle_opts=opts.LineStyleOpts(color="source", opacity=0.6),
            )
        ],
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"),
        layout_iterations=30,
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("bottom", content)
    assert_in("orient", content)
    assert_in("levels", content)
    assert_in("layoutIterations", content)
