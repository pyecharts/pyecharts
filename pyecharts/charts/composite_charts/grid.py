# coding=utf-8
import copy

from ... import options as opts
from ...commons.types import Optional, Union
from ..chart import Base, RectChart


class Grid(Base):
    """
    <<< 并行显示多张图 >>>
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options: Optional[dict] = None
        self._axis_index: int = 0
        self._grow_grid_index: int = 0

    def add(
        self,
        chart: RectChart,
        grid_opts: Union[opts.GridOpts, dict],
        grid_index: int = 0,
    ):
        if isinstance(grid_opts, opts.GridOpts):
            grid_opts = grid_opts.opts

        if self.options is None:
            self.options = copy.deepcopy(chart.options)
            self.chart_id = chart.chart_id
            self.options.update(grid=[], title=[])
            for s in self.options.get("series"):
                s.update(xAxisIndex=self._axis_index, yAxisIndex=self._axis_index)

        title = chart.options.get("title", opts.TitleOpts().opts)
        self.options.update(
            title=self.options.get("title", opts.TitleOpts().opts) + title
        )

        for s in chart.options.get("series"):
            s.update(xAxisIndex=self._axis_index, yAxisIndex=self._axis_index)

        for dep in chart.js_dependencies.items:
            self.js_dependencies.add(dep)

        if grid_index == 0:
            grid_index = self._grow_grid_index

        for x in chart.options.get("xAxis"):
            x.update(gridIndex=grid_index)
        for y in chart.options.get("yAxis"):
            y.update(gridIndex=grid_index)
        self._grow_grid_index += 1

        if self._axis_index > 0:
            self.options.get("series").extend(chart.options.get("series"))
            self.options.get("legend").extend(chart.options.get("legend"))
            self.options.get("xAxis").extend(chart.options.get("xAxis"))
            self.options.get("yAxis").extend(chart.options.get("yAxis"))

        self.options.get("grid").append(grid_opts)
        self._axis_index += 1
        return self
