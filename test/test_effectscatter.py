from example.commons import Faker
from pyecharts.charts import EffectScatter


def test_effectscatter_base():
    c = EffectScatter().add_xaxis(Faker.choose()).add_yaxis("", Faker.values())
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
