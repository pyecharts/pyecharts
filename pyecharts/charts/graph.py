# coding=utf-8

from pyecharts.chart import Chart


class Graph(Chart):
    """
    <<< 关系图 >>>

    用于展现节点以及节点之间的关系数据。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Graph, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        nodes,
        links,
        categories=None,
        is_focusnode=True,
        is_roam=True,
        is_rotatelabel=False,
        graph_layout="force",
        graph_edge_length=50,
        graph_gravity=0.2,
        graph_repulsion=50,
        graph_edge_symbol=None,
        graph_edge_symbolsize=10,
        **kwargs
    ):
        """
        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param nodes:
            关系图结点，包含的数据项有
            name：结点名称（必须有！）。
            x: 节点的初始 x 值。
            y：节点的初始 y 值。
            value：结点数值。
            category：结点类目。
            symbol：标记图形，有'circle', 'rect', 'roundRect', 'triangle',
                    'diamond', 'pin', 'arrow'可选。
            symbolSize：标记图形大小。
        :param links:
            结点间的关系数据，包含的数据项有
            source：边的源节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）
            target：边的目标节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）
            value：边的数值，可以在力引导布局中用于映射到边的长度
        :param categories:
            结点分类的类目，结点可以指定分类，也可以不指定。
            如果节点有分类的话可以通过 nodes[i].category 指定每个节点的类目，
            类目的样式会被应用到节点样式上
        :param is_focusnode:
            是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点
        :param is_roam:
            是否开启鼠标缩放和平移漫游。
            如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
        :param is_rotatelabel:
            是否旋转标签
        :param graph_layout:
            关系图布局，默认为 'force'
            none：不采用任何布局，使用节点中必须提供的 x， y 作为节点的位置。
            circular：采用环形布局
            force：采用力引导布局
        :param graph_edge_length:
            力布局下边的两个节点之间的距离，这个距离也会受 repulsion 影响。
            支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的
            长度。值越小则长度越长。
        :param graph_gravity:
            节点受到的向中心的引力因子。该值越大节点越往中心点靠拢。
        :param graph_repulsion:
            节点之间的斥力因子。默认为 50
            支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。
            值越大则斥力越大
        :param graph_edge_symbol:
            边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。
            默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol: ['circle', 'arrow']。
        :param graph_edge_symbolsize:
            边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
        :param kwargs:
        """
        kwargs.update(type="graph")
        chart = self._get_all_options(**kwargs)

        if categories:
            for c in categories:
                self._option.get("legend")[0].get("data").append(c)

        if graph_edge_symbol is None:
            graph_edge_symbol = [None, None]

        self._option.get("series").append(
            {
                "type": "graph",
                "name": name,
                "layout": graph_layout,
                "symbol": chart["symbol"],
                "circular": {"rotateLabel": is_rotatelabel},
                "force": {
                    "repulsion": graph_repulsion,
                    "edgeLength": graph_edge_length,
                    "gravity": graph_gravity,
                },
                "label": chart["label"],
                "lineStyle": chart["line_style"],
                "roam": is_roam,
                "focusNodeAdjacency": is_focusnode,
                "data": nodes,
                "categories": categories,
                "edgeSymbol": graph_edge_symbol,
                "edgeSymbolSize": graph_edge_symbolsize,
                "links": links,
            }
        )
        self._config_components(**kwargs)
