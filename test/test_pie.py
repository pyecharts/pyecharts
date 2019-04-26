from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie


def test_pie_base():
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
