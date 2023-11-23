from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class ThemeRiver(Chart):
    """
    <<< ThemeRiver >>>

    ThemeRiver graph is a special kind of flow graph,
    which is mainly used to show the changes of events or themes
    over a period of time.
    """

    def add(
        self,
        series_name: types.Sequence,
        data: types.Sequence[types.Union[opts.ThemeRiverItem, dict]],
        *,
        label_opts: types.Label = opts.LabelOpts(),
        singleaxis_opts: types.SingleAxis = opts.SingleAxisOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
    ):
        for n in series_name:
            self._append_legend(n)

        self.options.get("series").append(
            {
                "type": ChartType.THEMERIVER,
                "name": series_name,
                "data": data,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
            }
        )

        self.options.update(singleAxis=singleaxis_opts)
        self.options.get("tooltip").update(trigger="axis")
        return self
