from unittest.mock import patch

from nose.tools import eq_

from pyecharts import options as opts
from pyecharts.charts import Sunburst


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_sunburst_base(fake_writer):
    data = [
        {
            "name": "Grandpa",
            "children": [
                {
                    "name": "Uncle Leo",
                    "value": 15,
                    "children": [
                        {"name": "Cousin Jack", "value": 2},
                        {
                            "name": "Cousin Mary",
                            "value": 5,
                            "children": [{"name": "Jackson", "value": 2}],
                        },
                        {"name": "Cousin Ben", "value": 4},
                    ],
                },
                {
                    "name": "Father",
                    "value": 10,
                    "children": [
                        {"name": "Me", "value": 5},
                        {"name": "Brother Peter", "value": 1},
                    ],
                },
            ],
        },
        {
            "name": "Nancy",
            "children": [
                {
                    "name": "Uncle Nike",
                    "children": [
                        {"name": "Cousin Betty", "value": 1},
                        {"name": "Cousin Jenny", "value": 2},
                    ],
                }
            ],
        },
    ]

    c = Sunburst().add("Sunburst 演示数据", data)
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")


def test_sunburst_dataitem():
    item_name = "test_data_item"
    item = opts.SunburstItem(name=item_name)
    eq_(item.opts.get("name"), item_name)
