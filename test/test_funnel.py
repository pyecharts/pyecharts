from example.commons import Faker
from pyecharts.charts import Funnel


def test_funnel_base():
    c = Funnel().add("商品", [list(z) for z in zip(Faker.choose(), Faker.values())])
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
