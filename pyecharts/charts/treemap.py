# coding=utf-8

from pyecharts.chart import Chart


class TreeMap(Chart):
    """
    <<< 树图 >>>

    树图是一种常见的表达『层级数据』『树状数据』的可视化形式。它主要用面积的方式，
    便于突出展现出『树』的各层级中重要的节点。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(TreeMap, self).__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        data,
        treemap_left_depth=None,
        treemap_drilldown_icon="▶",
        treemap_visible_min=10,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选
        :param data:
            树图的数据项是一棵树，每个节点包括`value`, `name`（可选）,
            `children`（也是树，可选）如下所示
            [
                {
                    value: 1212,    # 数值
                    # 子节点
                    children: [
                        {
                            # 子节点数值
                            value: 2323,
                            # 子节点名
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
            leafDepth 表示『展示几层』，层次更深的节点则被隐藏起来。设置了 leafDepth 后，
            下钻（drill down）功能开启。drill down 功能即点击后才展示子层级。
            例如，leafDepth 设置为 1，表示展示一层节点。
        :param treemap_drilldown_icon:
            当节点可以下钻时的提示符。只能是字符。默认为 '▶'
        :param treemap_visible_min:
            如果某个节点的矩形的面积，小于这个数值（单位：px平方），这个节点就不显示。
        :param kwargs:
        """
        chart = self._get_all_options(**kwargs)
        self._option.get("legend")[0].get("data").append(name)

        self._option.get("series").append(
            {
                "type": "treemap",
                "name": name,
                "data": data,
                "label": chart["label"],
                "leafDepth": treemap_left_depth,
                "drillDownIcon": treemap_drilldown_icon,
                "visibleMin": treemap_visible_min,
                "seriesId": self._option.get("series_id"),
            }
        )
        self._config_components(**kwargs)
