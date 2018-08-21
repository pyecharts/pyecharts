# coding=utf-8

from pyecharts.chart import Chart


class Sankey(Chart):
    """
    <<< 桑基图  >>>

    桑基图是一种特殊的流图, 它主要用来表示原材料、能量等如何从初始形式经过中
    间过程的加工、转化到达最终形式。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Sankey, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        nodes,
        links,
        sankey_node_width=20,
        sankey_node_gap=8,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param nodes:
            桑基图结点，必须包含的数据项有：
                name：数据项名称
                value：数据项数值
        :param links:
            桑基图结点关系
                source：边的源节点名称（必须有！）
                target：边的目标节点名称（必须有！）
                value：边的数值，决定边的宽度。
        :param sankey_node_width:
            图中每个矩形节点的宽度。默认为 20。
        :param sankey_node_gap:
            图中每一列任意两个矩形节点之间的间隔。默认为 8。
        :param kwargs:
        """
        chart = self._get_all_options(**kwargs)
        self._option.get("legend")[0].get("data").append(name)

        self._option.get("series").append(
            {
                "type": "sankey",
                "name": name,
                "layout": None,
                "data": nodes,
                "links": links,
                "nodeWidth": sankey_node_width,
                "nodeGap": sankey_node_gap,
                "label": chart["label"],
                "lineStyle": chart["line_style"],
            }
        )
        self._config_components(**kwargs)
