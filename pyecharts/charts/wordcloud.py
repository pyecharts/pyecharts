# coding=utf-8
import random

from pyecharts.chart import Chart

SHAPES = (
    "cardioid",
    "diamond",
    "triangle-forward",
    "triangle",
    "pentagon",
    "star",
)


def gen_color():
    """
    为词云图生成随机颜色
    """
    return "rgb(%s,%s,%s)" % (
        random.randint(0, 160),
        random.randint(0, 160),
        random.randint(0, 160),
    )


class WordCloud(Chart):
    """
    <<< 词云图 >>>
    """

    def __init__(self, title="", subtitle="", **kwargs):
        super(WordCloud, self).__init__(title, subtitle, **kwargs)
        self._js_dependencies.add("wordcloud")

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)
        return self

    def __add(
        self,
        name,
        attr,
        value,
        shape="circle",
        word_gap=20,
        word_size_range=None,
        rotate_step=45,
        **kwargs
    ):
        """

        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param shape:
            词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward',
            'triangle', 'pentagon', 'star'可选。
        :param word_gap:
            单词间隔，默认为 20。
        :param word_size_range:
            单词字体大小范围，默认为 [12, 60]。
        :param rotate_step:
            旋转单词角度，默认为 45。
        """
        assert len(attr) == len(value)
        _data = []
        for data in zip(attr, value):
            _name, _value = data
            _data.append(
                {
                    "name": _name,
                    "value": _value,
                    "textStyle": {"normal": {"color": gen_color()}},
                }
            )
        _min, _max = 12, 60
        if word_size_range is not None:
            if len(word_size_range) == 2:
                _min, _max = word_size_range

        _rmin, _rmax = -90, 90
        # 确保设置的形状有效，单词的旋转角度应该设置在 [-90, 90]
        if shape in SHAPES:
            _rmin = _rmax = 0
        else:
            shape = "circle"

        self._option.get("series").append(
            {
                "type": "wordCloud",
                "name": name,
                "shape": shape,
                "rotationRange": [_rmin, _rmax],
                "rotationStep": rotate_step,
                "girdSize": word_gap,
                "sizeRange": [_min, _max],
                "data": _data,
            }
        )
        self._config_components(**kwargs)
