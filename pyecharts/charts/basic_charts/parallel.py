# coding=utf-8
from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import List, ListTuple, Union
from ...consts import ChartType


class Parallel(Chart):
    """
    <<< 平行坐标系 >>>

    平行坐标系是一种常用的可视化高维数据的图表。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add_schema(self, schema: List[opts.ParallelSchemaOpts]):
        self.options.update(parallelAxis=schema)
        return self

    def add(
        self,
        series_name: str,
        data: ListTuple,
        linestyle_opts: Union[opts.LineStyleOpts, dict] = opts.LineStyleOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
    ):
        if isinstance(linestyle_opts, opts.LineStyleOpts):
            linestyle_opts = linestyle_opts.opts
        if isinstance(tooltip_opts, opts.TooltipOpts):
            tooltip_opts = tooltip_opts.opts

        self.options.update(parallel=opts.ParallelOpts())
        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.PARALLEL,
                "coordinateSystem": "parallel",
                "lineStyle": linestyle_opts,
                "name": series_name,
                "data": data,
                "tooltip": tooltip_opts,
            }
        )
        return self
