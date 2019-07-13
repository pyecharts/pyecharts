from ... import options as opts
from ... import types
from ...charts.chart import Chart


class Calendar(Chart):
    """
    <<< Calendar Diagram >>>

    The calendar diagram is mainly used to represent the size of a value by
    color and must be used in conjunction with the visualMap component.
    Two categories of axes must be used in rectangular coordinates.
    """

    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(calendar=opts.CalendarOpts().opts)

    def add(
        self,
        series_name: str,
        yaxis_data: types.Sequence,
        *,
        is_selected: bool = True,
        label_opts: types.Label = opts.LabelOpts(),
        calendar_opts: types.Calendar = None,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
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
