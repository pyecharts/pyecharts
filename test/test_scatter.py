from echarts import Scatter

def test_scatter():
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter()
    scatter.add("a", v1, v2)
    scatter.add("b", v1[::-1], v2)
    scatter.show_config()
    scatter.render()