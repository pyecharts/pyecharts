from echarts.base import Base

class Graph(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, links,
             layout="force", symbol_size=50, symbol_rate=1, repulsion=1000, **kwargs):
        data, _links = [], []
        try:
            for node in {_ for link in links for _ in link}:
                if isinstance(node, tuple) and len(node) == 2:
                    data.append({"name": node[0],
                                 "value": node[1],
                                 "symbolSize": int(node[1] / symbol_rate)})
                else:
                    data.append({"name": node,
                                 "value": 0,
                                 "symbolSize": symbol_size})
            for link in links:
                if isinstance(link[0], tuple):
                    _links.append({"source": link[0][0], "target": link[1][0]})
                else:
                    _links.append({"source": link[0], "target": link[1]})
        except Exception as e:
            print(e)

        self._option.get('series').append({
            "type": "graph",
            "layout": layout,
            "circular": {"rotateLabel": False},
            "force": {"repulsion": repulsion},
            "label": self.Option.label("graph", **kwargs),
            "data":data,
            "links":_links
        })
        self._option.get('legend').update(self.Option.legend(**kwargs))
        self._option.update(color=self.Option.color(self._colorlst, **kwargs))

if __name__ == "__main__":
    import random
    links = [("结点1", "结点2"),
             ("结点2", "结点3"),
             ("结点3", "结点4"),
             ("结点4", "结点5"),
             ("结点5", "结点6"),
             ("结点6", "结点7"),
             ("结点7", "结点3"),
             ("结点8", "结点1"),
             ("结点7", "结点8")]
    # nodes = [("结点{}".format(i), random.randint(1, 100)) for i in range(1, 11)]
    nodes = [("结点{}".format(i)) for i in range(1, 20)]
    link = [(n1, n2) for n1 in nodes for n2 in nodes if n2 != n1]
    graph = Graph()
    # # graph.add(links, label_text_color="#fff", symbol_size=30, repulsion=1000)
    graph.add(link, label_text_color="#fff", symbol_size=1, symbol_rate=4, repulsion=1000, layout="circular")
    graph.show_config()
    graph.render()