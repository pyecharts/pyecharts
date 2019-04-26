from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Map


def test_map_base():
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
