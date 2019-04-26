from pyecharts.charts import Gauge


def test_gauge_base():
    c = Gauge().add("", [("完成率", 66.6)])
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
