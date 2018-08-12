# coding=utf-8

from pyecharts.chart import Chart


class Tree(Chart):
    """
    <<< 树图 >>>

    树图主要用来可视化树形数据结构，是一种特殊的层次类型，具有唯一的根节点，左子树，和右子树。
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(Tree, self).__init__(title, subtitle, **kwargs)

    @staticmethod
    def collapse_interval(data, interval=0):
        if data and isinstance(data, list):
            children = data[0].get("children", None)
            if children and interval > 0:
                for index, value in enumerate(children):
                    if index % interval == 0:
                        value.update(collapsed="false")
                return data

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(
        self,
        name,
        data,
        tree_layout="orthogonal",
        tree_symbol="emptyCircle",
        tree_symbol_size=7,
        tree_orient="LR",
        tree_top="12%",
        tree_left="12%",
        tree_bottom="12%",
        tree_right="12%",
        tree_label_position="left",
        tree_label_vertical_align="middle",
        tree_label_align="right",
        tree_label_text_size=12,
        tree_leaves_position="right",
        tree_leaves_vertical_align="middle",
        tree_leaves_align="left",
        tree_leaves_text_size=12,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param data:
            数据项，list 类型。
            首先假设你有一份数据需要生产树图，大概长这样

                 |----B     |----E----|----I
                 |          |
                 |----C-----|----F         |----J
            A----|                         |
                 |----D-----|----G----|----|----K
                            |
                            |----H
            你需要来编写成 JSON 数据，节点都是以 {name, children} 为基础的递归嵌套模式，如下
            [{
                "children": [
                    {
                        "children": [],
                        "name": "B"
                    },
                    {
                        "children": [
                            {
                                "children": [
                                    {
                                        "children": [],
                                        "name": "I"
                                    }
                                ],
                                "name": "E"
                            },
                            {
                                "children": [],
                                "name": "F"
                            }
                        ],
                        "name": "C"
                    },
                    {
                        "children": [
                            {
                                "children": [
                                    {
                                        "children": [],
                                        "name": "J"
                                    },
                                    {
                                        "children": [],
                                        "name": "K"
                                    }
                                ],
                                "name": "G"
                            },
                            {
                                "children": [],
                                "name": "H"
                            }
                        ],
                        "name": "D"
                    }
                ],
                "name": "A"
            }]
        :param tree_layout:
            树图的布局，有 正交 和 径向 两种。这里的 正交布局 就是我们通常所说的
            水平 和 垂直 方向，对应的参数取值为 'orthogonal' 。而 径向布局 是指以
            根节点为圆心，每一层节点为环，一层层向外发散绘制而成的布局，
            对应的参数取值为 'radial' 。
        :param tree_symbol:
            标记的图形。
            ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle',
            'diamond', 'pin', 'arrow', 'none'
        :param tree_symbol_size:
            标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽
            和高，例如 [20, 10] 表示标记宽为 20，高为 10。
        :param tree_orient:
            树图中 正交布局 的方向，也就是说只有在 layout = 'orthogonal' 的时候，
            该配置项才生效。对应有 水平 方向的 从左到右，从右到左；以及垂直方向的
            从上到下，从下到上。取值分别为 'LR' , 'RL', 'TB', 'BT'。注意，之前
            的配置项值 'horizontal' 等同于 'LR'， 'vertical' 等同于 'TB'。
        :param tree_top:
            tree 组件离容器顶部的距离。可以是像 20 这样的具体像素值，
            可以是像 '20%' 这样相对于容器高宽的百分比。
        :param tree_left:
            tree 组件离容器左侧的距离。可以是像 20 这样的具体像素值，
            可以是像 '20%' 这样相对于容器高宽的百分比。
        :param tree_bottom:
            tree 组件离容器底部的距离。可以是像 20 这样的具体像素值，
            可以是像 '20%' 这样相对于容器高宽的百分比。
        :param tree_right:
            tree 组件离容器右侧的距离。可以是像 20 这样的具体像素值，
            可以是像 '20%' 这样相对于容器高宽的百分比。
        :param tree_label_position:
            标签的位置。
            * [x, y]
            通过相对的百分比或者绝对像素值表示标签相对于图形包围盒左上角的位置。 示例：
              // 绝对的像素值
              position: [10, 10],
              // 相对的百分比
              position: ['50%', '50%']
            * 'top'
            * 'left'
            * 'right'
            * 'bottom'
            * 'inside'
            * 'insideLeft'
            * 'insideRight'
            * 'insideTop'
            * 'insideBottom'
            * 'insideTopLeft'
            * 'insideBottomLeft'
            * 'insideTopRight'
            * 'insideBottomRight'
        :param tree_label_vertical_align:
            父节点文字垂直对齐方式，默认自动。可选：'top'，'middle'，'bottom'
        :param tree_label_align:
            父节点文字水平对齐方式，默认自动。可选：'left'，'center'，'right'
        :param tree_text_size:
            父节点文字的字体大小
        :param tree_leaves_position:
            距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。
            参加 tree_label_position
        :param tree_leaves_vertical_align:
            叶节点文字垂直对齐方式，默认自动。可选：'top'，'middle'，'bottom'
        :param tree_leaves_align:
            叶节点文字水平对齐方式，默认自动。可选：'left'，'center'，'right'
        :param tree_leaves_text_size:
            叶节点文字的字体大小
        :param kwargs:
        """
        self._option.get("series").append(
            {
                "type": "tree",
                "name": name,
                "data": data,
                "left": tree_left,
                "right": tree_right,
                "top": tree_top,
                "bottom": tree_bottom,
                "symbol": tree_symbol,
                "symbolSize": tree_symbol_size,
                "layout": tree_layout,
                "orient": tree_orient,
                "label": {
                    "normal": {
                        "position": tree_label_position,
                        "verticalAlign": tree_label_vertical_align,
                        "align": tree_label_align,
                        "fontSize": tree_label_text_size,
                    }
                },
                "leaves": {
                    "label": {
                        "normal": {
                            "position": tree_leaves_position,
                            "verticalAlign": tree_leaves_vertical_align,
                            "align": tree_leaves_align,
                            "fontSize": tree_leaves_text_size,
                        }
                    }
                },
            }
        )
        self._config_components(**kwargs)
