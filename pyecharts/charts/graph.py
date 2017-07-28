#!/usr/bin/env python
#coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options

class Graph(Base):
    """
    <<< Graph chart >>>
    Graph is a diagram to represent nodes and the links connecting nodes.
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
            Series name used for displaying in tooltip and filtering with legend,
            or updaing data and configuration with setOption.
        :param nodes:
            Relational nodes data
            name：Name of data item.     # required！！
            x：x value of node position.
            y：y value of node position.
            value：value of data item.
            category：Index of category which the data item belongs to.
            symbol：Symbol of node of this category.
                    Includes 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
            symbolSize：symbol size
        :param links:
            Relational data between nodes
            source：name of source node on edge      # required！！
            target：name of target node on edge      # required！！
            value：value of edge,It can be used in the force layout to map to the length of the edge
        :param categories:
            Name of category, which is used to correspond with legend and the content of tooltip.
        :param is_focusnode:
            Whether to focus/highlight the hover node and it's adjacencies.
        :param is_roam:
            Whether to enable mouse zooming and translating. false by default.
            If either zooming or translating is wanted,
            it can be set to 'scale' or 'move'. Otherwise, set it to be true to enable both.
        :param is_rotatelabel:
            Whether to rotate the label automatically.
        :param layout:
            Graph layout.
            'none': No any layout, use x, y provided in node as the position of node.
            'circular': Adopt circular layout, see the example Les Miserables.
            'force': Adopt force-directed layout, see the example Force,
                     the detail about configrations of layout are in graph.force
        :param edge_length:
            The distance between 2 nodes on edge. This distance is also affected by repulsion.
            It can be an array to represent the range of edge length.In this case edge with
            larger value will be shorter, which means two nodes are closer. And edge with smaller value will be longer.
        :param gravity:
            The gravity factor enforcing nodes approach to the center.
            The nodes will be closer to the center as the value becomes larger.
        :param repulsion:
            The repulsion factor between nodes. The repulsion will be stronger and the distance between 2 nodes
            becomes further as this value becomes larger.
            It can be an array to represent the range of repulsion.
            In this case larger value have larger repulsion and smaller value will have smaller repulsion.
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
