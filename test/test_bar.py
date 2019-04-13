from pyecharts.charts import Bar


def test_bar_base():
    c = (
        Bar()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("bar0", [1, 2, 4])
        .add_yaxis("bar1", [2, 3, 6])
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
