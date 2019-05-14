from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Sequence, Union
from ...globals import ChartType


class Parallel(Chart):
    """
    <<< Parallel >>>

    Parallel coordinate systems are commonly used to visualize graphs of
    high dimensional data.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(parallel=opts.ParallelOpts().opts)

    def add_schema(
        self,
        schema: Sequence[Union[opts.ParallelAxisOpts, dict]],
        parallel_opts: Union[opts.ParallelOpts, dict, None] = None,
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
        data: Sequence,
        *,
        is_selected: bool = True,
        linestyle_opts: Union[opts.LineStyleOpts, dict] = opts.LineStyleOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.PARALLEL,
                "coordinateSystem": "parallel",
                "lineStyle": linestyle_opts,
                "name": series_name,
                "data": data,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
