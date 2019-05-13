import copy

from ... import options as opts
from ...commons.types import Optional, Sequence, Union
from ...globals import ThemeType
from ..chart import Base, RectChart


class Grid(Base):
    """
    `Gird` Drawing grid in rectangular coordinate. In a single grid,
    at most two X and Y axes each is allowed. Line chart, bar chart,
    and scatter chart (bubble chart) can be drawn in grid.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
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
        if self.options is None:
            self.options = copy.deepcopy(chart.options)
            self.chart_id = chart.chart_id
            self.options.update(grid=[], title=[])
            if self.theme != ThemeType.WHITE:
                self.options.update(color=[])
            for s in self.options.get("series"):
                s.update(xAxisIndex=self._axis_index, yAxisIndex=self._axis_index)

        title = chart.options.get("title", opts.TitleOpts().opts)
        if isinstance(title, opts.TitleOpts):
            title = title.opts
        if not isinstance(title, Sequence):
            title = (title,)
        self.options.get("title").extend(title)

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
