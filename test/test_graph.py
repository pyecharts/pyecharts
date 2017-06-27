import json

from echarts import Graph

def test_graph():
    with open("E:\Python\pyecharts\json\weibo.json", "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes, links, categories, cont, mid, userl = j
    graph = Graph("微博转发关系图", width=1300, height=700)
    graph.add(nodes, links, label_pos="right", repulsion=50, legend_show=False, line_curve=0.2, label_text_color="")
    graph.show_config()
    graph.render()