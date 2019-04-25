from pyecharts.charts import Line


def test_bar_base():
    c = (
        Line()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
