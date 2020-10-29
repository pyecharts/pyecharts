from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Parallel(Chart):
    """
    <<< Parallel >>>

    Parallel coordinate systems are commonly used to visualize graphs of
    high dimensional data.
    """

    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(parallel=opts.ParallelOpts().opts)

    def add_schema(
        self,
        schema: types.Sequence[types.Union[opts.ParallelAxisOpts, dict]],
        parallel_opts: types.Union[opts.ParallelOpts, dict, None] = None,
    ):
        sc = []
        for s in schema:
            if isinstance(s, opts.ParallelAxisOpts):
                s = s.opts
            sc.append(s)
        self.options.update(parallelAxis=sc)

        if parallel_opts:
            if isinstance(parallel_opts, opts.ParallelOpts):
                parallel_opts = parallel_opts.opts
            self.options.update(parallel=parallel_opts)
        return self

    def add(
        self,
        series_name: str,
        data: types.Sequence[types.Union[dict]],
        *,
        is_smooth: bool = False,
        is_selected: bool = True,
        linestyle_opts: types.LineStyle = opts.LineStyleOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.PARALLEL,
                "coordinateSystem": "parallel",
                "lineStyle": linestyle_opts,
                "name": series_name,
                "data": data,
                "smooth": is_smooth,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
