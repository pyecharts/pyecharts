#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options


class Sankey(Base):
    """
    <<< Sankey chart >>>

    Sankey graphs are a specific type of stream graphs, in which the width of each branch is
    shown proportionally to the flow quantity. These graphs are typically used to
    visualize energy or material or cost transfers between processes.
    They can also visualize the energy accounts, material flow accounts on a regional or
    national level, and also the breakdown of cost of item or services.
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Sankey, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, nodes, links,
              sankey_node_width=20,
              sankey_node_gap=8,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updating data and configuration with setOption.
        :param nodes:
            Relational nodes data
            name：Name of data item.         # required！！
            value: Value of data item.       # required！！
        :param links:
            Relational data between nodes
            source：name of source node on edge      # required！！
            target：name of target node on edge      # required！！
            value：value of edge,It can be used in the force layout to map to the length of the edge
        :param sankey_node_width:
            The node width of rectangle in graph.
        :param sankey_node_gap:
            The gap between any two regtangles in each column from the graph.
        :param kwargs:
        :return:
        """
        chart = get_all_options(**kwargs)
        self._option.get('legend')[0].get('data').append(name)

        self._option.get('series').append({
            "type": "sankey",
            "name": name,
            "layout": None,
            "data": nodes,
            "links": links,
            "nodeWidth": sankey_node_width,
            "nodeGap": sankey_node_gap,
            "label": chart['label'],
            "lineStyle": chart['line_style'],
        })
        self._config_components(**kwargs)
