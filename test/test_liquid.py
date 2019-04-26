from pyecharts.charts import Liquid


def test_liquid_base():
    c = Liquid().add("lq", [0.6, 0.7])
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
