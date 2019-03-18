# coding=utf-8

from ...charts.chart import Chart
from ...options import (
    AreaStyleOpts,
    AxisLineOpts,
    InitOpts,
    LabelOpts,
    LineStyleOpts,
    SplitAreaOpt,
    SplitLineOpts,
)
from ...types import *


class Radar(Chart):
    """
    <<< 雷达图 >>>

    雷达图主要用于表现多变量的数据。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)

    def set_radar_component(
        self,
        schema=None,
        c_schema=None,
        shape="",
        text_color="#333",
        text_size=12,
        splitline_opt: SplitLineOpts = SplitLineOpts(),
        splitarea_opt: SplitAreaOpt = SplitAreaOpt(),
        axisline_opt: AxisLineOpts = AxisLineOpts(),
    ):
        if isinstance(splitline_opt, SplitLineOpts):
            splitline_opt = splitline_opt.opts
        if isinstance(splitarea_opt, SplitAreaOpt):
            splitarea_opt = splitarea_opt.opts
        if isinstance(axisline_opt, AxisLineOpts):
            axisline_opt = axisline_opt.opts

        indicator = []
        if schema:
            for s in schema:
                _name, _max = s
                indicator.append({"name": _name, "max": _max})
        if c_schema:
            indicator = c_schema
        self.options.update(
            radar={
                "indicator": indicator,
                "shape": shape,
                "name": {"textStyle": {"color": text_color, "fontSize": text_size}},
                "splitLine": splitline_opt,
                "splitArea": splitarea_opt,
                "axisLine": axisline_opt,
            }
        )
        return self

    def add(
        self,
        name: str,
        value: ListTuple,
        symbol: Optional[str] = None,
        item_color=None,
        label_opts: LabelOpts = LabelOpts(),
        linestyle_opts: LineStyleOpts = LineStyleOpts(),
        areastyle_opts: AreaStyleOpts = AreaStyleOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts
        if isinstance(areastyle_opts, AreaStyleOpts):
            areastyle_opts = areastyle_opts.opts

        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "radar",
                "name": name,
                "data": value,
                "symbol": symbol,
                "label": label_opts,
                "itemStyle": {"normal": {"color": item_color}},
                "lineStyle": linestyle_opts,
                "areaStyle": areastyle_opts,
            }
        )
