from echarts.base import Base

class Graph(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)
        self._option.update(series=[], legend={"data":[]})

    def add(self, links, **kwargs):
        data, _links = [], []
        dataset = set()
        for link in links:
            dataset.add(link[0])
            dataset.add(link[1])
        for d in list(dataset):
            data.append({"name": d})
        for link in links:
            _links.append({"source": link[0], "target": link[1]})
        self._option.get('series').append({
            "type": "graph",
            "layout": kwargs.get('layout', "force"),
            "circular": {"rotateLabel": False},
            "force": {"repulsion": 1000},
            "symbolSize": kwargs.get('symbol_size', 50),
            "label": Base._label(**kwargs),
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
             ("结点7", "结点8")]
    graph = Graph()
    graph.add(links)
    graph.show_config()
    graph.render()