# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import List, Optional, Sequence, Union
from ...globals import ChartType


class Radar(Chart):
    """
    <<< 雷达图 >>>

    雷达图主要用于表现多变量的数据。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add_schema(
        self,
        schema: List[Union[opts.RadarIndicatorItem, dict]],
        shape: Optional[str] = None,
        textstyle_opts: Union[opts.TextStyleOpts, dict] = opts.TextStyleOpts(),
        splitline_opt: Union[opts.SplitLineOpts, dict] = opts.SplitLineOpts(
            is_show=True
        ),
        splitarea_opt: Union[opts.SplitAreaOpts, dict] = opts.SplitAreaOpts(),
        axisline_opt: Union[opts.AxisLineOpts, dict] = opts.AxisLineOpts(),
    ):
        if isinstance(textstyle_opts, opts.TextStyleOpts):
            textstyle_opts = textstyle_opts.opts
        if isinstance(splitline_opt, opts.SplitLineOpts):
            splitline_opt = splitline_opt.opts
        if isinstance(splitarea_opt, opts.SplitAreaOpts):
            splitarea_opt = splitarea_opt.opts
        if isinstance(axisline_opt, opts.AxisLineOpts):
            axisline_opt = axisline_opt.opts

        indicators = []
        for s in schema:
            if isinstance(s, opts.RadarIndicatorItem):
                s = s.opts
            indicators.append(s)

        self.options.update(
            radar={
                "indicator": indicators,
                "shape": shape,
                "name": {"textStyle": textstyle_opts},
                "splitLine": splitline_opt,
                "splitArea": splitarea_opt,
                "axisLine": axisline_opt,
            }
        )
        return self

    def add(
        self,
        series_name: str,
        data: Sequence,
        *,
        is_selected: bool = True,
        symbol: Optional[str] = None,
        color: Optional[str] = None,
        label_opts: opts.LabelOpts = opts.LabelOpts(),
        linestyle_opts: opts.LineStyleOpts = opts.LineStyleOpts(),
        areastyle_opts: opts.AreaStyleOpts = opts.AreaStyleOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(linestyle_opts, opts.LineStyleOpts):
            linestyle_opts = linestyle_opts.opts
        if isinstance(areastyle_opts, opts.AreaStyleOpts):
            areastyle_opts = areastyle_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts

        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.RADAR,
                "name": series_name,
                "data": data,
                "symbol": symbol,
                "label": label_opts,
                "itemStyle": {"normal": {"color": color}},
                "lineStyle": linestyle_opts,
                "areaStyle": areastyle_opts,
                "tooltip": tooltip_opts,
            }
        )
        return self
