from typing import Sequence

from ... import options as opts
from ... import types
from ...charts.chart import Base


class Timeline(Base):
    """
    `Timeline` provides functions like switching and playing between multiple charts.
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options = {"baseOption": {"series": [], "timeline": {}}, "options": []}
        self.add_schema()
        self._time_points: types.Sequence = []

    def add_schema(
        self,
        axis_type: str = "category",
        current_index: types.Numeric = 0,
        orient: str = "horizontal",
        symbol: types.Optional[str] = None,
        symbol_size: types.Optional[types.Numeric] = None,
        play_interval: types.Optional[types.Numeric] = None,
        control_position: str = "left",
        is_auto_play: bool = False,
        is_loop_play: bool = True,
        is_rewind_play: bool = False,
        is_timeline_show: bool = True,
        is_inverse: bool = False,
        pos_left: types.Optional[str] = None,
        pos_right: types.Optional[str] = None,
        pos_top: types.Optional[str] = None,
        pos_bottom: types.Optional[str] = "-5px",
        width: types.Optional[str] = None,
        height: types.Optional[str] = None,
        linestyle_opts: types.LineStyle = None,
        label_opts: types.Label = None,
        itemstyle_opts: types.ItemStyle = None,
        graphic_opts: types.Graphic = None,
        checkpointstyle_opts: types.TimeLinkCheckPoint = None,
        controlstyle_opts: types.TimeLineControl = None,
        progress_linestyle_opts: types.LineStyle = None,
        progress_itemstyle_opts: types.ItemStyle = None,
        progress_label_opts: types.Label = None,
    ):
        self.options.get("baseOption").get("timeline").update(
            {
                "axisType": axis_type,
                "currentIndex": current_index,
                "orient": orient,
                "autoPlay": is_auto_play,
                "controlPosition": control_position,
                "loop": is_loop_play,
                "rewind": is_rewind_play,
                "show": is_timeline_show,
                "inverse": is_inverse,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "playInterval": play_interval,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "width": width,
                "height": height,
                "lineStyle": linestyle_opts,
                "label": label_opts,
                "itemStyle": itemstyle_opts,
                "graphic": graphic_opts,
                "checkpointStyle": checkpointstyle_opts,
                "controlStyle": controlstyle_opts,
                "progress": {
                    "lineStyle": progress_linestyle_opts,
                    "itemStyle": progress_itemstyle_opts,
                    "label": progress_label_opts,
                },
            }
        )
        return self

    def add(self, chart: Base, time_point: str):
        for dep in chart.js_dependencies.items:
            self.js_dependencies.add(dep)
        self._time_points.append(time_point)

        self.options.get("baseOption").get("timeline").update(data=self._time_points)
        self.options.get("options").append(
            {
                "backgroundColor": chart.options.get("backgroundColor"),
                "legend": chart.options.get("legend"),
                "series": chart.options.get("series"),
                "xAxis": chart.options.get("xAxis"),
                "yAxis": chart.options.get("yAxis"),
                "title": chart.options.get("title"),
                "tooltip": chart.options.get("tooltip"),
                "visualMap": chart.options.get("visualMap"),
                "color": chart.options.get("color"),
                "graphic": chart.options.get("graphic"),
                "bmap": chart.options.get("bmap"),
                "toolbox": chart.options.get("toolbox"),
                "dataset": chart.options.get("dataset"),
                "radiusAxis": chart.options.get("radiusAxis"),
                "angleAxis": chart.options.get("angleAxis"),
                "xAxis3D": chart.options.get("xAxis3D"),
                "yAxis3D": chart.options.get("yAxis3D"),
                "zAxis3D": chart.options.get("zAxis3D"),
                "grid3D": chart.options.get("grid3D"),
            }
        )
        self.__check_components(chart)
        self.options.get("baseOption").update(series=chart.options.get("series"))
        return self

    def __check_components(self, chart: Base):
        components = [
            "grid",
            "xAxis",
            "yAxis",
            "polar",
            "radiusAxis",
            "geo",
            "angleAxis",
            "radar",
            "visualMap",
            "dataZoom",
            "parallelAxis",
            "legend",
        ]

        for component in components:
            c = chart.options.get(component, None)
            if c is not None:
                self.options.get("baseOption").update({component: c})
