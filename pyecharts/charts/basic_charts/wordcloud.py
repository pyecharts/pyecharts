# coding=utf-8
import random

from ...charts.chart import Chart
from ...options import *
from ...types import *

SHAPES = ("cardioid", "diamond", "triangle-forward", "triangle", "pentagon", "star")


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

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.js_dependencies.add("wordcloud")

    def add(
        self,
        name: str,
        data_pair: ListTuple,
        shape: str = "circle",
        word_gap: Numeric = 20,
        word_size_range=None,
        rotate_step: Numeric = 45,
    ):
        _data = []
        for (_name, _value) in data_pair:
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

        self.options.get("series").append(
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
