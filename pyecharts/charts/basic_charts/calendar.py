from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Sequence, Union


class Calendar(Chart):
    """
    <<< Calendar Diagram >>>

    The calendar diagram is mainly used to represent the size of a value by
    color and must be used in conjunction with the visualMap component.
    Two categories of axes must be used in rectangular coordinates.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
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
