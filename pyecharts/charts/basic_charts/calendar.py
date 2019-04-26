# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Sequence, Union


class Calendar(Chart):
    """
    <<< 日历图 >>>

    热力图主要通过颜色去表现数值的大小，必须要配合 visualMap 组件使用。
    直角坐标系上必须要使用两个类目轴。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(calendar=opts.CalendarOpts().opts)

    def add(
        self,
        series_name: str,
        yaxis_data: Sequence,
        *,
        is_selected: bool = True,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        calendar_opts: Union[opts.CalendarOpts, dict, None] = None,
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(calendar_opts, opts.CalendarOpts):
            calendar_opts = calendar_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts
        if isinstance(itemstyle_opts, opts.ItemStyleOpts):
            itemstyle_opts = itemstyle_opts.opts

        if calendar_opts:
            self.options.update(calendar=calendar_opts)

        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": "heatmap",
                "coordinateSystem": "calendar",
                "name": series_name,
                "data": yaxis_data,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
