from echarts import Scatter

def test_scatter():
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]

    scatter = Scatter()
    # v1, v2 = scatter.draw(r"e:\python\pyecharts\_images\boy.png")
    scatter.add("boy", v1, v2)
    # scatter.add("a", v1, v2)
    # scatter.add("b", v1[::-1], v2)
    scatter.show_config()
    scatter.render()