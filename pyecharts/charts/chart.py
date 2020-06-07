from .. import options as opts
from .. import types
from ..charts.base import Base
from ..globals import RenderType, ThemeType, ToolTipFormatterType
from ..types import Optional, Sequence


class Chart(Base):
    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        if isinstance(init_opts, dict):
            temp_opts = opts.InitOpts()
            temp_opts.update(**init_opts)
            init_opts = temp_opts
        super().__init__(init_opts=init_opts)
        self.colors = (
            "#c23531 #2f4554 #61a0a8 #d48265 #749f83 #ca8622 #bda29a #6e7074 "
            "#546570 #c4ccd3 #f05b72 #ef5b9c #f47920 #905a3d #fab27b #2a5caa "
            "#444693 #726930 #b2d235 #6d8346 #ac6767 #1d953f #6950a1 #918597"
        ).split()
        if init_opts.opts.get("theme") == ThemeType.WHITE:
            self.options.update(color=self.colors)
        self.options.update(
            series=[],
            legend=[{"data": [], "selected": dict()}],
            tooltip=opts.TooltipOpts().opts,
        )
        self._chart_type: Optional[str] = None

    def set_colors(self, colors: Sequence[str]):
        self.options.update(color=colors)
        return self

    def set_series_opts(
        self,
        label_opts: types.Label = None,
        linestyle_opts: types.LineStyle = None,
        splitline_opts: types.SplitLine = None,
        areastyle_opts: types.AreaStyle = None,
        axisline_opts: types.AxisLine = None,
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        markarea_opts: types.MarkArea = None,
        effect_opts: types.Effect = opts.EffectOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        **kwargs,
    ):
        for s in self.options.get("series"):
            if label_opts:
                s.update(label=label_opts)

            if linestyle_opts:
                s.update(lineStyle=linestyle_opts)

            if splitline_opts:
                s.update(splitLine=splitline_opts)

            if areastyle_opts:
                s.update(areaStyle=areastyle_opts)

            if axisline_opts:
                s.update(axisLine=axisline_opts)

            if markpoint_opts:
                s.update(markPoint=markpoint_opts)

            if markline_opts:
                s.update(markLine=markline_opts)

            if markarea_opts:
                s.update(markArea=markarea_opts)

            if effect_opts:
                s.update(rippleEffect=effect_opts)

            if tooltip_opts:
                s.update(tooltip=tooltip_opts)

            if itemstyle_opts:
                s.update(itemStyle=itemstyle_opts)

            if len(kwargs) > 0:
                s.update(kwargs)

        return self

    def _append_legend(self, name, is_selected):
        self.options.get("legend")[0].get("data").append(name)
        self.options.get("legend")[0].get("selected").update({name: is_selected})

    def _append_color(self, color: Optional[str]):
        if color:
            self.colors = [color] + self.colors
            if self.theme == ThemeType.WHITE:
                self.options.update(color=self.colors)

    def set_global_opts(
        self,
        title_opts: types.Title = opts.TitleOpts(),
        legend_opts: types.Legend = opts.LegendOpts(),
        tooltip_opts: types.Tooltip = None,
        toolbox_opts: types.Toolbox = None,
        brush_opts: types.Brush = None,
        xaxis_opts: types.Axis = None,
        yaxis_opts: types.Axis = None,
        visualmap_opts: types.VisualMap = None,
        datazoom_opts: types.DataZoom = None,
        graphic_opts: types.Graphic = None,
        axispointer_opts: types.AxisPointer = None,
    ):
        if tooltip_opts is None:
            tooltip_opts = opts.TooltipOpts(
                formatter=ToolTipFormatterType.get(self._chart_type, None)
            )
        self.options.update(
            title=title_opts,
            toolbox=toolbox_opts,
            tooltip=tooltip_opts,
            visualMap=visualmap_opts,
            dataZoom=datazoom_opts,
            graphic=graphic_opts,
            axisPointer=axispointer_opts,
        )

        if brush_opts is not None:
            self.options.update(brush=brush_opts)

        if isinstance(legend_opts, opts.LegendOpts):
            legend_opts = legend_opts.opts
        for _s in self.options["legend"]:
            _s.update(legend_opts)

        if xaxis_opts and self.options.get("xAxis", None):
            if isinstance(xaxis_opts, opts.AxisOpts):
                xaxis_opts = xaxis_opts.opts
            self.options["xAxis"][0].update(xaxis_opts)

        if yaxis_opts and self.options.get("yAxis", None):
            if isinstance(yaxis_opts, opts.AxisOpts):
                yaxis_opts = yaxis_opts.opts
            self.options["yAxis"][0].update(yaxis_opts)

        return self

    def add_dataset(
        self,
        source: types.Union[types.Sequence, types.JSFunc] = None,
        dimensions: types.Optional[types.Sequence] = None,
        source_header: types.Optional[bool] = None,
    ):
        self.options.update(
            dataset={
                "source": source,
                "dimensions": dimensions,
                "sourceHeader": source_header,
            }
        )
        return self


class RectChart(Chart):
    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(xAxis=[opts.AxisOpts().opts], yAxis=[opts.AxisOpts().opts])

    def extend_axis(
        self,
        xaxis_data: Sequence = None,
        xaxis: types.Axis = None,
        yaxis: types.Axis = None,
    ):
        if xaxis is not None:
            if isinstance(xaxis, opts.AxisOpts):
                xaxis = xaxis.opts
            xaxis.update(data=xaxis_data)
            self.options["xAxis"].append(xaxis)
        if yaxis is not None:
            if isinstance(yaxis, opts.AxisOpts):
                yaxis = yaxis.opts
            self.options["yAxis"].append(yaxis)
        return self

    def add_xaxis(self, xaxis_data: Sequence):
        self.options["xAxis"][0].update(data=xaxis_data)
        self._xaxis_data = xaxis_data
        return self

    def reversal_axis(self):
        self.options["yAxis"][0]["data"] = self._xaxis_data
        self.options["xAxis"][0]["data"] = None
        return self

    def overlap(self, chart: Base):
        self.options.get("legend")[0].get("data").extend(
            chart.options.get("legend")[0].get("data")
        )
        self.options.get("legend")[0].get("selected").update(
            chart.options.get("legend")[0].get("selected")
        )
        self.options.get("series").extend(chart.options.get("series"))
        return self


class Chart3D(Chart):
    """
    `Chart3D`类是所有 3D 类图表的基类，继承自 `Chart` 类
    """

    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        init_opts.renderer = RenderType.CANVAS
        super().__init__(init_opts)
        self.js_dependencies.add("echarts-gl")
        self.options.update(visualMap=opts.VisualMapOpts().opts)
        self._3d_chart_type: Optional[str] = None  # 3d chart type,don't use it directly


class ThreeAxisChart(Chart3D):
    def add(
        self,
        series_name: str,
        data: Sequence,
        shading: Optional[str] = None,
        itemstyle_opts: types.ItemStyle = None,
        label_opts: types.Label = opts.LabelOpts(is_show=False),
        xaxis3d_opts: types.Axis3D = opts.Axis3DOpts(type_="category"),
        yaxis3d_opts: types.Axis3D = opts.Axis3DOpts(type_="category"),
        zaxis3d_opts: types.Axis3D = opts.Axis3DOpts(type_="value"),
        grid3d_opts: types.Grid3D = opts.Grid3DOpts(),
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        self.options.get("legend")[0].get("data").append(series_name)
        self.options.update(
            xAxis3D=xaxis3d_opts,
            yAxis3D=yaxis3d_opts,
            zAxis3D=zaxis3d_opts,
            grid3D=grid3d_opts,
        )

        self.options.get("series").append(
            {
                "type": self._3d_chart_type,
                "name": series_name,
                "data": data,
                "label": label_opts,
                "shading": shading,
                "itemStyle": itemstyle_opts,
                "encode": encode,
            }
        )
        return self
