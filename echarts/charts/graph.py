from echarts.base import Base

class Graph(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, nodes, links, categories=None, *,
             isroam=True, layout="force", edge_length=50, gravity=0.2, repulsion=50, **kwargs):
        if categories:
            for c in categories:
                self._option.get('legend').get('data').append(c)
        self._option.get('series').append({
            "type": "graph",
            "layout": layout,
            "circular": {"rotateLabel": False},
            "force": {"repulsion": repulsion,
                      "edgeLength": edge_length,
                      "gravity": gravity},
            "label": self.Option.label("graph", **kwargs),
            "lineStyle": self.Option.line_style(**kwargs),
            "roam": isroam,
            "focusNodeAdjacency": True,
            "data": nodes,
            "categories": categories,
            "links":links
        })
        self._option.get('legend').update(self.Option.legend(**kwargs))
        self._option.update(color=self.Option.color(self._colorlst, **kwargs))

if __name__ == "__main__":

    import json
    with open("E:\weibo.json", "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes, links, categories, cont, mid, userl = j
    graph = Graph("微博转发关系图", width=1300, height=700)
    graph.add(nodes, links, label_pos="right", repulsion=50, legend_show=False, line_curve=0.2, label_text_color="")
    graph.show_config()
    graph.render()