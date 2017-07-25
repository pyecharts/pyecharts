#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Graph(Base):
    """
    <<< 关系图 >>>
    用于展现节点以及节点之间的关系数据。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super(Graph, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, nodes, links, categories=None,
              is_focusnode=True,
              is_roam=True,
              is_rotatelabel=False,
              layout="force",
              edge_length=50,
              gravity=0.2,
              repulsion=50,
              **kwargs):
        """
        :param name:
            图例名称
        :param nodes:
            关系图结点，包含的数据项有
            # 必须！！
            name：结点名称
            # 非必须！！
            x：节点的初始 x 值
            y：节点的初始 y 值
            value：结点数值
            category：结点类目
            symbol：标记图形
            symbolSize：标记图形大小
        :param links:
            结点间的关系数据，包含的数据项有
            # 必须！！
            source：边的源节点名称的字符串，也支持使用数字表示源节点的索引
            target：边的目标节点名称的字符串，也支持使用数字表示源节点的索引
            # 非必须！！
            value：边的数值，可以在力引导布局中用于映射到边的长度
        :param categories:
            结点分类的类目
            如果节点有分类的话可以通过 nodes[i].category 指定每个节点的类目，类目的样式会被应用到节点样式上
        :param is_focusnode:
            是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点
        :param is_roam:
            是否开启鼠标缩放和平移漫游。默认不开启
            如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move'。设置成 true 为都开启
        :param is_rotatelabel:
            是否旋转标签，默认不旋转
        :param layout:
            关系图布局 'none' 不采用任何布局，使用节点中提供的 x， y 作为节点的位置
            circular：采用环形布局，
            force：采用力引导布局
        :param edge_length:
            力布局下边的两个节点之间的距离，这个距离也会受 repulsion 影响
            支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长
        :param gravity:
            节点受到的向中心的引力因子。该值越大节点越往中心点靠拢
        :param repulsion:
            节点之间的斥力因子
            支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
        :param kwargs:
        """
        kwargs.update(type="graph")
        chart = get_all_options(**kwargs)
        if categories:
            for c in categories:
                self._option.get('legend')[0].get('data').append(c)
        self._option.get('series').append({
            "type": "graph",
            "name": name,
            "layout": layout,
            "symbol": chart['symbol'],
            "circular": {"rotateLabel": is_rotatelabel},
            "force": {"repulsion": repulsion,
                      "edgeLength": edge_length,
                      "gravity": gravity},
            "label": chart['label'],
            "lineStyle": chart['line_style'],
            "roam": is_roam,
            "focusNodeAdjacency": is_focusnode,
            "data": nodes,
            "categories": categories,
            "links":links,
        })
        self._legend_visualmap_colorlst(**kwargs)
