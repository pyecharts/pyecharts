from ... import options as opts
from ... import types
from ...charts.chart import Chart3D
from ...globals import ChartType
from ...options import InitOpts, RenderOpts


class Map3D(Chart3D):
    """
    3D map
    """

    def __init__(
        self,
        init_opts: types.Init = InitOpts(),
        render_opts: types.RenderInit = RenderOpts(),
    ):
        super().__init__(init_opts, render_opts)
        self._3d_chart_type = ChartType.MAP3D

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence,
        *,
        type_: ChartType = None,
        maptype: str = "china",
        is_map_symbol_show: bool = True,
        grid_3d_index: types.Numeric = 0,
        geo_3d_index: types.Numeric = 0,
        globe_index: types.Numeric = 0,
        bar_size: types.Optional[types.Numeric] = None,
        bevel_size: types.Numeric = 0,
        bevel_smoothness: types.Numeric = 2,
        stack: types.Optional[str] = None,
        min_height: types.Numeric = 2,
        symbol: str = "circle",
        symbol_size: types.Union[types.Numeric, types.Sequence, types.JSFunc] = 10,
        blend_mode: str = "source-over",
        is_polyline: bool = False,
        effect: types.Lines3DEffect = None,
        linestyle_opts: types.LineStyle = opts.LineStyleOpts(),
        label_opts: types.Label = opts.LabelOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_label_opts: types.Label = None,
        emphasis_itemstyle_opts: types.ItemStyle = None,
        shading: types.Optional[str] = None,
        realistic_material_opts: types.Optional[types.Map3DRealisticMaterial] = None,
        lambert_material_opts: types.Optional[types.Map3DLambertMaterial] = None,
        color_material_opts: types.Optional[types.Map3DColorMaterial] = None,
        zlevel: types.Numeric = -10,
        is_silent: bool = False,
        is_animation: bool = True,
        animation_duration_update: types.Numeric = 100,
        animation_easing_update: types.Numeric = "cubicOut",
    ):
        if type_ != ChartType.LINES3D:
            data = [{"name": n, "value": v} for n, v in data_pair]
        else:
            data = data_pair
        self._append_legend(series_name)
        if type_ is None or type_ == ChartType.MAP3D:
            self.options.get("series").append(
                {
                    "type": ChartType.MAP3D,
                    "name": series_name,
                    "map": maptype,
                    "coordinateSystem": "geo3D",
                    "label": label_opts,
                    "data": data,
                    "itemStyle": itemstyle_opts,
                    "showLegendSymbol": is_map_symbol_show,
                    "tooltip": tooltip_opts,
                    "emphasis": {
                        "label": emphasis_label_opts,
                        "itemStyle": emphasis_itemstyle_opts,
                    },
                }
            )
        elif type_ == ChartType.BAR3D:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "geo3D",
                    "grid3DIndex": grid_3d_index,
                    "geo3DIndex": geo_3d_index,
                    "globeIndex": globe_index,
                    "barSize": bar_size,
                    "bevelSize": bevel_size,
                    "bevelSmoothness": bevel_smoothness,
                    "stack": stack,
                    "minHeight": min_height,
                    "label": label_opts,
                    "itemStyle": itemstyle_opts,
                    "emphasis": {
                        "label": emphasis_label_opts,
                        "itemStyle": emphasis_itemstyle_opts,
                    },
                    "data": data,
                    "shading": shading,
                    "realisticMaterial": realistic_material_opts,
                    "lambertMaterial": lambert_material_opts,
                    "colorMaterial": color_material_opts,
                    "zlevel": zlevel,
                    "silent": is_silent,
                    "animation": is_animation,
                    "animationDurationUpdate": animation_duration_update,
                    "animationEasingUpdate": animation_easing_update,
                }
            )
        elif type_ == ChartType.SCATTER3D:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "geo3D",
                    "grid3DIndex": grid_3d_index,
                    "geo3DIndex": geo_3d_index,
                    "globeIndex": globe_index,
                    "symbol": symbol,
                    "symbolSize": symbol_size,
                    "label": label_opts,
                    "itemStyle": itemstyle_opts,
                    "emphasis": {
                        "label": emphasis_label_opts,
                        "itemStyle": emphasis_itemstyle_opts,
                    },
                    "data": data,
                    "blendMode": blend_mode,
                    "zlevel": zlevel,
                    "silent": is_silent,
                    "animation": is_animation,
                    "animationDurationUpdate": animation_duration_update,
                    "animationEasingUpdate": animation_easing_update,
                }
            )
        elif type_ == ChartType.LINE3D:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "geo3D",
                    "grid3DIndex": grid_3d_index,
                    "lineStyle": linestyle_opts,
                    "data": data,
                    "zlevel": zlevel,
                    "silent": is_silent,
                    "animation": is_animation,
                    "animationDurationUpdate": animation_duration_update,
                    "animationEasingUpdate": animation_easing_update,
                }
            )
        elif type_ == ChartType.LINES3D:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "geo3D",
                    "geo3DIndex": geo_3d_index,
                    "globeIndex": globe_index,
                    "polyline": is_polyline,
                    "effect": effect,
                    "lineStyle": linestyle_opts,
                    "data": data,
                    "blendMode": blend_mode,
                    "zlevel": zlevel,
                    "silent": is_silent,
                }
            )
        return self

    def add_schema(
        self,
        maptype: str = "china",
        name: types.Optional[str] = None,
        *,
        box_width: types.Optional[types.Numeric] = 100,
        box_height: types.Optional[types.Numeric] = 10,
        box_depth: types.Optional[types.Numeric] = None,
        region_height: types.Optional[types.Numeric] = 3,
        environment: types.Optional[types.JSFunc] = None,
        is_show_ground: bool = False,
        ground_color: str = "#aaa",
        is_instancing: bool = False,
        map3d_label: types.Map3DLabel = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_label_opts: types.Label = None,
        emphasis_itemstyle_opts: types.ItemStyle = None,
        shading: types.Optional[str] = None,
        realistic_material_opts: types.Optional[types.Map3DRealisticMaterial] = None,
        lambert_material_opts: types.Optional[types.Map3DLambertMaterial] = None,
        color_material_opts: types.Optional[types.Map3DColorMaterial] = None,
        light_opts: types.Optional[types.Map3DLight] = None,
        post_effect_opts: types.Optional[types.Map3DPostEffect] = None,
        is_enable_super_sampling: types.Union[str, bool] = "auto",
        view_control_opts: types.Optional[types.Map3DViewControl] = None,
        zlevel: types.Optional[types.Numeric] = -10,
        pos_left: types.Union[types.Numeric, str] = "auto",
        pos_top: types.Union[types.Numeric, str] = "auto",
        pos_right: types.Union[types.Numeric, str] = "auto",
        pos_bottom: types.Union[types.Numeric, str] = "auto",
        pos_width: types.Union[types.Numeric, str] = "auto",
        pos_height: types.Union[types.Numeric, str] = "auto",
    ):
        self.js_dependencies.add(maptype)
        self.options.update(
            geo3D={
                "map": maptype,
                "name": name,
                "boxWidth": box_width,
                "boxHeight": box_height,
                "boxDepth": box_depth,
                "regionHeight": region_height,
                "environment": environment,
                "groundPlane": {"show": is_show_ground, "color": ground_color},
                "instancing": is_instancing,
                "itemStyle": itemstyle_opts,
                "label": map3d_label,
                "emphasis": {
                    "label": emphasis_label_opts,
                    "itemStyle": emphasis_itemstyle_opts,
                },
                "shading": shading,
                "realisticMaterial": realistic_material_opts,
                "lambertMaterial": lambert_material_opts,
                "colorMaterial": color_material_opts,
                "light": light_opts,
                "postEffect": post_effect_opts,
                "temporalSuperSampling": {"enable": is_enable_super_sampling},
                "viewControl": view_control_opts,
                "zlevel": zlevel,
                "left": pos_left,
                "top": pos_top,
                "right": pos_right,
                "bottom": pos_bottom,
                "width": pos_width,
                "height": pos_height,
            }
        )
        return self
