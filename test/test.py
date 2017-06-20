from echarts.bar import Bar
from echarts.gauge import Gauge
from echarts.graph import Graph
from echarts.line import Line
from echarts.pie import Pie
from echarts.radar import Radar
from echarts.scatter import Scatter


def test_bar():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [10, 25, 8, 60, 50, 150]
    bar = Bar()
    bar.add("A", attr, v1, label_text_size=20)
    bar.add("B", attr, v2, orient="vertical", mark_line=["average"])
    bar.show_config()
    bar.render()


def test_gague():
    gauge = Gauge("业务指标")
    gauge.add("业务指标", 100, "是萌萌哒真爱的概率")
    gauge.show_config()
    gauge.render()


def test_graph():
    links = [("结点1", "结点2"),
             ("结点2", "结点3"),
             ("结点3", "结点4"),
             ("结点4", "结点5"),
             ("结点5", "结点6"),
             ("结点6", "结点7"),
             ("结点7", "结点3"),
             ("结点8", "结点1"),
             ("结点7", "结点8")]
    graph = Graph()
    graph.add(links, label_show=True, label_text_color="#fff")
    graph.show_config()
    graph.render()


def test_line():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value_A = [5, 20, 36, 10, 10, 100]
    value_B = [55, 60, 16, 14, 15, 80]
    line = Line()
    line.add("商家A", attr, value_A, mark_point=["max", "min", "average"])
    line.add("商家B", attr, value_B, mark_line=["max", "min", "average"])
    line.show_config()
    line.render()


def test_pie():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [11, 12, 13, 10, 10, 10]
    pie = Pie()
    pie.add("商品", attr, value, label_show=True, rand_data=True, rad=[30, 70])
    pie.show_config()
    pie.render()


def test_radar():
    r = [("销售", 6500),
         ("管理", 16000),
         ("信息技术", 30000),
         ("客服", 38000),
         ("研发", 52000),
         ("市场", 25000)]

    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    radar = Radar()
    radar.config(r, split_area_show=True)
    radar.add("预算分配", v1, label_color=["#000"])
    radar.add("实际开销", v2, label_color=["#4e79a7"])
    radar.render()
    radar.show_config()


def test1_scatter():
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter()
    scatter.add("a", v1, v2)
    scatter.add("b", v1[::-1], v2)
    scatter.show_config()
    scatter.render()


if __name__ == "__main__":
    test_bar()
    test_gague()
    test_graph()
    test_line()
    test_pie()
    test_radar()
    test1_scatter()
