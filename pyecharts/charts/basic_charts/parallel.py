# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import List, Sequence, Union
from ...globals import ChartType


class Parallel(Chart):
    """
    <<< 平行坐标系 >>>

    平行坐标系是一种常用的可视化高维数据的图表。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(parallel=opts.ParallelOpts().opts)

    def add_schema(
        self,
        schema: List[Union[opts.ParallelAxisOpts, dict]],
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
        if isinstance(linestyle_opts, opts.LineStyleOpts):
            linestyle_opts = linestyle_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts
        if isinstance(itemstyle_opts, opts.ItemStyleOpts):
            itemstyle_opts = itemstyle_opts.opts

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
