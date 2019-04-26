from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie


def test_pie_base():
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
