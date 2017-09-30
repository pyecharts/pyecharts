#!/usr/bin/env python
# coding=utf-8

from pyecharts.base import Base
from pyecharts.option import get_all_options


class TreeMap(Base):
    """
    <<< TreeMap >>>

    TreeMap is a common way to present "hierarchical data" or "tree data".
    It primarily highlights the important nodes at all hierarchies in 『Tree』
    with area.
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(TreeMap, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data,
              treemap_left_depth=None,
              treemap_drilldown_icon='▶',
              treemap_visible_min=10,
              **kwargs):
        """

        :param name:
            Series name used for displaying in tooltip and filtering with legend,
            or updating data and configuration with setOption.
        :param data:
            the the data format of series-treemap.data is a forest. For example:
            [ # Tips, the top level is a list.
                {
                    value: 1212,
                    children: [
                        {
                            # The value of this node, indicating the area size.
                            value: 2323,
                            # show the description text in rectangle.
                            name: 'description of this node',
                            children: [...],
                        },
                        {
                            value: 4545,
                            name: 'description of this node',
                            children: [
                                {
                                    value: 5656,
                                    name: 'description of this node',
                                    children: [...]
                                },
                                ...
                            ]
                        }
                    ]
                },
                ...
            ]
        :param treemap_left_depth:
            When leafDepth is set, the feature "drill down" is enabled, which means
            when clicking a tree node, this node will be set as root and its
            children will be shown.
            leafDepth represents how many levels are shown at most. For example,
            when leafDepth is set to 1, only one level will be shown.
        :param treemap_drilldown_icon:
            Marker when the node is able to be drilled down.
        :param treemap_visible_min:
            A node will not be shown when its area size is smaller than this
            value (unit: px square).
            In this way, tiny nodes will be hidden, otherwise they will huddle
            together. When user zoom the treemap, the area size will increase
            and the rectangle will be shown if the area size is larger than
            this threshold.
        :param kwargs:
        """
        chart = get_all_options(**kwargs)
        self._option.get('legend')[0].get('data').append(name)

        self._option.get('series').append({
            "type": "treemap",
            "name": name,
            "data": data,
            "label": chart['label'],
            "leafDepth": treemap_left_depth,
            "drillDownIcon": treemap_drilldown_icon,
            "visibleMin": treemap_visible_min,
            "seriesId": self._option.get('series_id'),
        })
        self._config_components(**kwargs)
