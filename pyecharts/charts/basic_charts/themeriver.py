# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Sequence, Union
from ...globals import ChartType


class ThemeRiver(Chart):
    """
    <<< 主题河流图 >>>

    主题河流图是一种特殊的流图, 它主要用来表示事件或主题等在一段时间内的变化。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: Sequence,
        data: Sequence,
        *,
        is_selected: bool = True,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        singleaxis_opts: Union[opts.SingleAxisOpts, dict] = opts.SingleAxisOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts
        if isinstance(singleaxis_opts, opts.SingleAxisOpts):
            singleaxis_opts = singleaxis_opts.opts
        if isinstance(itemstyle_opts, opts.ItemStyleOpts):
            itemstyle_opts = itemstyle_opts.opts

        for n in series_name:
            self._append_legend(n, is_selected)

        self.options.get("series").append(
            {
                "type": ChartType.THEMERIVER,
                "name": series_name,
                "data": data,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )

        self.options.update(singleAxis=singleaxis_opts)
        self.options.get("tooltip").update(trigger="axis")
        return self
