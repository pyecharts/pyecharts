from .. import options as opts
from .. import types
from ..charts.base import Base
from ..globals import RenderType, ThemeType, ToolTipFormatterType
from ..types import Optional, Sequence


class Chart(Base):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        if isinstance(init_opts, dict):
            temp_opts = opts.InitOpts()
            temp_opts.update(**init_opts)
            init_opts = temp_opts
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        # Change to Echarts V5 default color list
        self.colors = (
            "#5470c6 #91cc75 #fac858 #ee6666 #73c0de #3ba272 #fc8452 #9a60b4 " "#ea7ccc"
        ).split()
        self.default_color_n = len(self.colors)
        if init_opts.opts.get("theme") == ThemeType.WHITE:
            self.options.update(color=self.colors)
        self.options.update(
            series=[],
            legend=[{"data": [], "selected": dict()}],
            tooltip=opts.TooltipOpts().opts,
        )
        self._chart_type: Optional[str] = None

    def set_dark_mode(
        self,
        dark_mode_colors: Optional[Sequence[str]] = None,
        dark_mode_bg_color: str = "#100C2A",
    ):
        # [Hard Code Here] The Echarts default Dark Mode Configurations
        if dark_mode_colors is None:
            dark_mode_colors = (
                "#4992ff #7cffb2 #fddd60 #ff6e76 #58d9f9 #05c091 #ff8a45 "
                "#8d48e3 #dd79ff"
            ).split()
        self.options.update(
            backgroundColor=dark_mode_bg_color,
            darkMode=True,
            color=dark_mode_colors,
        )
        self.theme = ThemeType.DARK
        return self

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

    def _append_legend(self, name):
        self.options.get("legend")[0].get("data").append(name)

    def _append_color(self, color: Optional[str]):
        if color:
            # 这是一个bug
            # 添加轴（执行add_yaxis操作）的顺序与新添加的color值（设置color属性）未一一对应，正好颠倒
            self.colors.insert(-self.default_color_n, color)
            # self.colors = [color] + self.colors
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
            # _s.update(legend_opts)
            _s.update(**{k: v for k, v in legend_opts.items() if v is not None})

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
        transform: types.Optional[Sequence[opts.DatasetTransformOpts]] = None,
        from_dataset_index: types.Optional[types.Numeric] = None,
        from_dataset_id: types.Optional[types.Numeric] = None,
        from_transform_result: types.Optional[types.Numeric] = None,
    ):
        if self.options.get("dataset") is not None:
            self.options.get("dataset").append(
                {
                    "source": source,
                    "dimensions": dimensions,
                    "sourceHeader": source_header,
                    "transform": transform,
                    "fromDatasetIndex": from_dataset_index,
                    "fromDatasetId": from_dataset_id,
                    "fromTransformResult": from_transform_result,
                }
            )
        else:
            self.options.update(
                dataset=[
                    {
                        "source": source,
                        "dimensions": dimensions,
                        "sourceHeader": source_header,
                        "transform": transform,
                        "fromDatasetIndex": from_dataset_index,
                        "fromDatasetId": from_dataset_id,
                        "fromTransformResult": from_transform_result,
                    }
                ]
            )
        return self


class RectChart(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
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
        if self.options.get("legend")[0].get("selected") is not None:
            self.options.get("legend")[0].get("selected").update(
                chart.options.get("legend")[0].get("selected")
            )
        self.options.get("series").extend(chart.options.get("series"))
        # to merge colors of chart
        for c in chart.colors[: len(chart.colors) - self.default_color_n]:
            self.colors.insert(len(self.colors) - self.default_color_n, c)
        return self


class Chart3D(Chart):
    """
    `Chart3D`类是所有 3D 类图表的基类，继承自 `Chart` 类
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        init_opts.renderer = RenderType.CANVAS
        super().__init__(init_opts, render_opts)
        self.js_dependencies.add("echarts-gl")
        self._3d_chart_type: Optional[str] = None  # 3d chart type,don't use it directly

    def add_globe(
        self,
        is_show: bool = True,
        globe_radius: types.Numeric = 100,
        globe_outer_radius: types.Numeric = 150,
        environment: str = "auto",
        base_texture: types.Union[str, types.JsCode, None] = None,
        height_texture: types.Union[str, types.JsCode, None] = None,
        displacement_texture: types.Union[str, types.JsCode, None] = None,
        displacement_scale: types.Numeric = 0,
        displacement_quality: str = "medium",
        shading: types.Optional[str] = None,
        realistic_material_opts: types.Optional[types.Map3DRealisticMaterial] = None,
        lambert_material_opts: types.Optional[types.Map3DLambertMaterial] = None,
        color_material_opts: types.Optional[types.Map3DColorMaterial] = None,
        light_opts: types.Optional[types.Map3DLight] = None,
        post_effect_opts: types.Optional[types.Map3DPostEffect] = None,
        is_enable_super_sampling: types.Union[str, bool] = "auto",
        view_control_opts: types.Optional[types.Map3DViewControl] = None,
        layers: types.Optional[types.GlobeLayers] = None,
        z_level: types.Numeric = -10,
        pos_left: types.Union[str, types.Numeric] = "auto",
        pos_top: types.Union[str, types.Numeric] = "auto",
        pos_right: types.Union[str, types.Numeric] = "auto",
        pos_bottom: types.Union[str, types.Numeric] = "auto",
        width: types.Union[str, types.Numeric] = "auto",
        height: types.Union[str, types.Numeric] = "auto",
    ):
        self.options.update(
            globe={
                "show": is_show,
                "globeRadius": globe_radius,
                "globeOuterRadius": globe_outer_radius,
                "environment": environment,
                "baseTexture": base_texture,
                "heightTexture": height_texture,
                "displacementTexture": displacement_texture,
                "displacementScale": displacement_scale,
                "displacementQuality": displacement_quality,
                "shading": shading,
                "realisticMaterial": realistic_material_opts,
                "lambertMaterial": lambert_material_opts,
                "colorMaterial": color_material_opts,
                "light": light_opts,
                "postEffect": post_effect_opts,
                "temporalSuperSampling": {"enable": is_enable_super_sampling},
                "viewControl": view_control_opts,
                "layers": layers,
                "zlevel": z_level,
                "left": pos_left,
                "top": pos_top,
                "right": pos_right,
                "bottom": pos_bottom,
                "width": width,
                "height": height,
            }
        )
        return self


class ThreeAxisChart(Chart3D):
    def add(
        self,
        series_name: str,
        data: Sequence,
        coordinate_system: Optional[str] = None,
        shading: Optional[str] = None,
        itemstyle_opts: types.ItemStyle = None,
        label_opts: types.Label = opts.LabelOpts(is_show=False),
        grid_3d_index: types.Numeric = 0,
        xaxis3d_opts: types.Axis3D = opts.Axis3DOpts(type_="value", name="X"),
        yaxis3d_opts: types.Axis3D = opts.Axis3DOpts(type_="value", name="Y"),
        zaxis3d_opts: types.Axis3D = opts.Axis3DOpts(type_="value", name="Z"),
        grid3d_opts: types.Grid3D = opts.Grid3DOpts(),
        encode: types.Union[types.JSFunc, dict, None] = None,
        emphasis_opts: types.Optional[types.Emphasis3D] = None,
        is_parametric: types.Optional[bool] = None,
        is_show_wire_frame: types.Optional[bool] = None,
        wire_frame_line_style_opts: types.Optional[opts.LineStyleOpts] = None,
        equation: types.Optional[dict] = None,
        parametric_equation: types.Optional[dict] = None,
    ):
        self.options.get("legend")[0].get("data").append(series_name)
        self.options.update(
            xAxis3D=xaxis3d_opts,
            yAxis3D=yaxis3d_opts,
            zAxis3D=zaxis3d_opts,
            grid3D=grid3d_opts,
        )

        if self._3d_chart_type == "surface":
            self.options.get("series").append(
                {
                    "type": self._3d_chart_type,
                    "name": series_name,
                    "coordinateSystem": coordinate_system,
                    "data": data,
                    "label": label_opts,
                    "shading": shading,
                    "grid3DIndex": grid_3d_index,
                    "itemStyle": itemstyle_opts,
                    "parametric": is_parametric,
                    "wireframe": {
                        "show": is_show_wire_frame,
                        "lineStyle": wire_frame_line_style_opts,
                    },
                    "equation": equation,
                    "parametricEquation": parametric_equation,
                }
            )
        else:
            self.options.get("series").append(
                {
                    "type": self._3d_chart_type,
                    "name": series_name,
                    "coordinateSystem": coordinate_system,
                    "data": data,
                    "label": label_opts,
                    "shading": shading,
                    "grid3DIndex": grid_3d_index,
                    "itemStyle": itemstyle_opts,
                    "emphasis": emphasis_opts,
                    "encode": encode,
                }
            )
        return self
