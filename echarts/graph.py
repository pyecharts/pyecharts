from echarts.base import Base
from echarts.option import Option

class Graph(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, links, **kwargs):
        data = [{"name": d} for d in {_ for link in links for _ in link}]
        _links = [{"source": link[0], "target": link[1]} for link in links]
        self._option.get('series').append({
            "type": "graph",
            "layout": kwargs.get('layout', "force"),
            "circular": {"rotateLabel": False},
            "force": {"repulsion": 1000},
            "symbolSize": kwargs.get('symbol_size', 50),
            "label": Option.label("graph", **kwargs),
            "data":data,
            "links":_links
        })

if __name__ == "__main__":
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