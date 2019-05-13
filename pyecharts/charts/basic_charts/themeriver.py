from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Sequence, Union
from ...globals import ChartType


class ThemeRiver(Chart):
    """
    <<< ThemeRiver >>>

    ThemeRiver graph is a special kind of flow graph,
    which is mainly used to show the changes of events or themes
    over a period of time.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
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
