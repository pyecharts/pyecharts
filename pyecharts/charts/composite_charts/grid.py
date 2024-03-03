import copy

from ... import options as opts
from ... import types
from ...globals import ThemeType
from ..basic_charts.radar import Radar
from ..chart import Base, Chart, RectChart


class Grid(Base):
    """
    `Gird` Drawing grid in rectangular coordinate. In a single grid,
    at most two X and Y axes each is allowed. Line chart, bar chart,
    and scatter chart (bubble chart) can be drawn in grid.
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options: types.Optional[dict] = None
        self._axis_index: int = 0
        self._grow_grid_index: int = 0
        self.bg_color = init_opts.opts.get("bg_color")

    def add(
        self,
        chart: Chart,
        grid_opts: types.Union[opts.GridOpts, dict],
        *,
        grid_index: int = 0,
        is_control_axis_index: bool = False,
    ):
        if self.options is None:
            self.options = copy.deepcopy(chart.options)
            self.chart_id = chart.chart_id
            self.options.update(grid=[], title=[])
            if self.theme != ThemeType.WHITE:
                self.options.update(color=[])

            # Priority Order: Grid > Other Chart
            self.options.update(backgroundColor=self.bg_color)

            if not is_control_axis_index:
                for s in self.options.get("series"):
                    s.update(xAxisIndex=self._axis_index, yAxisIndex=self._axis_index)

        # visualMap 配置添加
        visual_map = chart.options.get("visualMap")
        if visual_map is not None:
            if isinstance(self.options.get("visualMap"), opts.VisualMapOpts):
                self.options.update(visualMap=[self.options.get("visualMap")])
            else:
                if self.options.get("visualMap") is None:
                    self.options.update(visualMap=[visual_map])
                else:
                    self.options.get("visualMap").extend([visual_map])

        # dataZoom 配置添加
        data_zoom = chart.options.get("dataZoom")
        if data_zoom is not None:
            if isinstance(self.options.get("dataZoom"), opts.DataZoomOpts):
                self.options.update(dataZoom=[self.options.get("dataZoom")])
            else:
                if self.options.get("dataZoom") is None:
                    self.options.update(dataZoom=[data_zoom])
                else:
                    self.options.get("dataZoom").extend([data_zoom])

        # title 配置添加
        title = chart.options.get("title", opts.TitleOpts().opts)
        if isinstance(title, opts.TitleOpts):
            title = title.opts
        if not isinstance(title, types.Sequence):
            title = (title,)
        self.options.get("title").extend(title)

        if not is_control_axis_index:
            for s in chart.options.get("series"):
                s.update(xAxisIndex=self._axis_index, yAxisIndex=self._axis_index)

        for dep in chart.js_dependencies.items:
            self.js_dependencies.add(dep)

        if chart.options.get("geo") is not None:
            self.options.update(geo=chart.options.get("geo"))

        if isinstance(chart, RectChart):
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
            if isinstance(chart, RectChart):
                self.options.get("xAxis").extend(chart.options.get("xAxis"))
                self.options.get("yAxis").extend(chart.options.get("yAxis"))
            if isinstance(chart, Radar):
                self.options.get("radar").extend(chart.options.get("radar"))

        self.options.get("grid").append(grid_opts)
        self._axis_index += 1
        return self
