from pyecharts.charts import TreeMap


def test_treemap_base():
    data = [
        {"value": 40, "name": "我是A"},
        {
            "value": 180,
            "name": "我是B",
            "children": [
                {
                    "value": 76,
                    "name": "我是B.children",
                    "children": [
                        {"value": 12, "name": "我是B.children.a"},
                        {"value": 28, "name": "我是B.children.b"},
                        {"value": 20, "name": "我是B.children.c"},
                        {"value": 16, "name": "我是B.children.d"},
                    ],
                }
            ],
        },
    ]

    c = TreeMap().add("演示数据", data)
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
