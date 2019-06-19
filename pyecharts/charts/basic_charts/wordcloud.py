import random

from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType

SHAPES = ("cardioid", "diamond", "triangle-forward", "triangle", "pentagon", "star")


def gen_color():
    """
    generate random color for WordCloud
    """
    return "rgb(%s,%s,%s)" % (
        random.randint(0, 160),
        random.randint(0, 160),
        random.randint(0, 160),
    )


class WordCloud(Chart):
    """
    <<< WordCloud >>>

    Word cloud is to visually highlight the keywords that
    appear frequently in the text.
    """

    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.js_dependencies.add("echarts-wordcloud")

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence,
        *,
        shape: str = "circle",
        word_gap: types.Numeric = 20,
        word_size_range: types.Optional[types.Sequence] = None,
        rotate_step: types.Numeric = 45,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        data = []
        for n, v in data_pair:
            data.append(
                {"name": n, "value": v, "textStyle": {"normal": {"color": gen_color()}}}
            )

        word_size_range = word_size_range or (12, 60)

        _rmin, _rmax = -90, 90
        # 确保设置的形状有效，单词的旋转角度应该设置在 [-90, 90]
        if shape in SHAPES:
            _rmin = _rmax = 0
        else:
            shape = "circle"

        self.options.get("series").append(
            {
                "type": ChartType.WORDCLOUD,
                "name": series_name,
                "shape": shape,
                "rotationRange": [_rmin, _rmax],
                "rotationStep": rotate_step,
                "girdSize": word_gap,
                "sizeRange": word_size_range,
                "data": data,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
