import simplejson as json

from ..globals import BMapType
from .global_options import TooltipOpts
from .series_options import (
    BasicOpts,
    ItemStyleOpts,
    JSFunc,
    LabelOpts,
    LineStyleOpts,
    Numeric,
    Optional,
    Sequence,
    TextStyleOpts,
    Union,
    AreaStyleOpts,
)


# Chart Options
class GraphNode(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        x: Optional[Numeric] = None,
        y: Optional[Numeric] = None,
        is_fixed: bool = False,
        value: Union[str, Sequence, None] = None,
        category: Optional[int] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        symbol_rotate: Optional[int] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        is_disabled_emphasis: Optional[bool] = None,
        emphasis_itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        emphasis_label_opts: Union[LabelOpts, dict, None] = None,
        blur_itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        blur_label_opts: Union[LabelOpts, dict, None] = None,
        is_disabled_select: Optional[bool] = None,
        select_itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        select_label_opts: Union[LabelOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "x": x,
            "y": y,
            "fixed": is_fixed,
            "value": value,
            "category": category,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "symbolRotate": symbol_rotate,
            "itemStyle": itemstyle_opts,
            "label": label_opts,
            "emphasis": {
                "disabled": is_disabled_emphasis,
                "itemStyle": emphasis_itemstyle_opts,
                "label": emphasis_label_opts,
            },
            "blur": {
                "itemStyle": blur_itemstyle_opts,
                "label": blur_label_opts,
            },
            "select": {
                "disabled": is_disabled_select,
                "itemStyle": select_itemstyle_opts,
                "label": select_label_opts,
            },
            "tooltip": tooltip_opts,
        }


class GraphLink(BasicOpts):
    def __init__(
        self,
        source: Union[str, int, None] = None,
        target: Union[str, int, None] = None,
        value: Optional[Numeric] = None,
        symbol: Union[str, Sequence, None] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        is_disabled_emphasis: Optional[bool] = None,
        emphasis_linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        emphasis_label_opts: Union[LabelOpts, dict, None] = None,
        blur_linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        blur_label_opts: Union[LabelOpts, dict, None] = None,
        is_disabled_select: Optional[bool] = None,
        select_linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        select_label_opts: Union[LabelOpts, dict, None] = None,
        is_ignore_force_layout: bool = False
    ):
        self.opts: dict = {
            "source": source,
            "target": target,
            "value": value,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "lineStyle": linestyle_opts,
            "label": label_opts,
            "emphasis": {
                "disabled": is_disabled_emphasis,
                "lineStyle": emphasis_linestyle_opts,
                "label": emphasis_label_opts,
            },
            "blur": {
                "lineStyle": blur_linestyle_opts,
                "label": blur_label_opts,
            },
            "select": {
                "disabled": is_disabled_select,
                "lineStyle": select_linestyle_opts,
                "label": select_label_opts,
            },
            "ignoreForceLayout": is_ignore_force_layout,
        }


class GraphCategory(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
        }


class BMapNavigationControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_TOP_LEFT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 10,
        type_: Numeric = BMapType.NAVIGATION_CONTROL_LARGE,
        is_show_zoom_info: bool = False,
        is_enable_geo_location: bool = False,
    ):
        bmap_nav_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "type": type_,
                "showZoomInfo": is_show_zoom_info,
                "enableGeolocation": is_enable_geo_location,
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.NavigationControl({}));".format(
                    bmap_nav_config
                )
            ]
        }


class BMapOverviewMapControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_RIGHT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 50,
        is_open: bool = False,
    ):
        bmap_overview_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "isOpen": is_open,
            }
        )

        self.opts: dict = {
            "functions": [
                "var overview = new BMap.OverviewMapControl({});".format(
                    bmap_overview_config
                ),
                "bmap.addControl(overview);",
            ]
        }


class BMapScaleControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 80,
        offset_height: Numeric = 21,
    ):
        bmap_scale_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.ScaleControl({}));".format(bmap_scale_config)
            ]
        }


class BMapTypeControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_TOP_RIGHT,
        type_: Numeric = BMapType.MAPTYPE_CONTROL_HORIZONTAL,
    ):
        bmap_type_config = json.dumps({"anchor": position, "type": type_})

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.MapTypeControl({}));".format(bmap_type_config)
            ]
        }


class BMapCopyrightTypeOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 2,
        offset_height: Numeric = 2,
        copyright_: str = "",
    ):
        bmap_copyright_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
            }
        )

        bmap_copyright_content_config = json.dumps({"id": 1, "content": copyright_})

        self.opts: dict = {
            "functions": [
                "var copyright = new BMap.CopyrightControl({});".format(
                    bmap_copyright_config
                ),
                "copyright.addCopyright({});".format(bmap_copyright_content_config),
                "bmap.addControl(copyright);",
            ]
        }


class BMapGeoLocationControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 10,
        is_show_address_bar: bool = True,
        is_enable_auto_location: bool = False,
    ):
        bmap_geo_location_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "showAddressBar": is_show_address_bar,
                "enableAutoLocation": is_enable_auto_location,
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.GeolocationControl({}))".format(
                    bmap_geo_location_config
                )
            ]
        }


class ComponentTitleOpts:
    def __init__(
        self,
        title: str = "",
        subtitle: str = "",
        title_style: Optional[dict] = None,
        subtitle_style: Optional[dict] = None,
    ):
        self.title = title.replace("\n", "<br/>")
        self.subtitle = subtitle.replace("\n", "<br/>")
        self.title_style: str = ""
        self.subtitle_style: str = ""
        title_style = title_style or {"style": "font-size: 18px; font-weight:bold;"}
        subtitle_style = subtitle_style or {"style": "font-size: 12px;"}
        self._convert_dict_to_string(title_style, subtitle_style)

    def _convert_dict_to_string(self, title_style: dict, subtitle_style: dict):
        for k, v in title_style.items():
            self.title_style += '{}="{}" '.format(k, v)
        for k, v in subtitle_style.items():
            self.subtitle_style += '{}="{}" '.format(k, v)


class PageLayoutOpts(BasicOpts):
    def __init__(
        self,
        justify_content: Optional[str] = None,
        margin: Optional[str] = None,
        display: Optional[str] = None,
        flex_wrap: Optional[str] = None,
    ):
        self.opts: dict = {
            "justify-content": justify_content,
            "margin": margin,
            "display": display,
            "flex-wrap": flex_wrap,
        }


class BaseGraphic(BasicOpts):
    pass


class GraphicShapeOpts(BaseGraphic):
    def __init__(
        self,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        width: Numeric = 0,
        height: Numeric = 0,
        r: Union[Sequence, Numeric, None] = None,
    ):
        self.opts: dict = {
            "x": pos_x,
            "y": pos_y,
            "width": width,
            "height": height,
            "r": r,
        }


class GraphicBasicStyleOpts(BaseGraphic):
    def __init__(
        self,
        fill: str = "#000",
        stroke: Optional[str] = None,
        line_width: Numeric = 0,
        shadow_blur: Optional[Numeric] = None,
        shadow_offset_x: Optional[Numeric] = None,
        shadow_offset_y: Optional[Numeric] = None,
        shadow_color: Optional[str] = None,
    ):
        self.opts: dict = {
            "fill": fill,
            "stroke": stroke,
            "line_width": line_width,
            "shadowBlur": shadow_blur,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "shadowColor": shadow_color,
        }


class GraphicImageStyleOpts(BaseGraphic):
    def __init__(
        self,
        image: Optional[str] = None,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        width: Numeric = 0,
        height: Numeric = 0,
        opacity: Numeric = 1,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "image": image,
            "x": pos_x,
            "y": pos_y,
            "width": width,
            "height": height,
            "opacity": opacity,
        }

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(graphic_basicstyle_opts.opts)
            else:
                self.opts.update(graphic_basicstyle_opts)


class GraphicTextStyleOpts(BaseGraphic):
    def __init__(
        self,
        text: Optional[JSFunc] = None,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        font: Optional[str] = None,
        font_size: Optional[Numeric] = 0,
        text_align: str = "left",
        text_vertical_align: Optional[str] = None,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "text": text,
            "x": pos_x,
            "y": pos_y,
            "font": font,
            "fontSize": font_size,
            "textAlign": text_align,
            "textVerticalAlign": text_vertical_align,
        }

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(graphic_basicstyle_opts.opts)
            else:
                self.opts.update(graphic_basicstyle_opts)


class GraphicItem(BaseGraphic):
    def __init__(
        self,
        id_: Optional[str] = None,
        action: str = "merge",
        position: [Sequence, Numeric, None] = None,
        rotation: Union[Numeric, JSFunc, None] = 0,
        scale: Union[Sequence, Numeric, None] = None,
        origin: Union[Numeric, Sequence, None] = None,
        left: Union[Numeric, str, None] = None,
        right: Union[Numeric, str, None] = None,
        top: Union[Numeric, str, None] = None,
        bottom: Union[Numeric, str, None] = None,
        bounding: str = "all",
        z: Numeric = 0,
        z_level: Numeric = 0,
        is_silent: bool = False,
        is_invisible: bool = False,
        is_ignore: bool = False,
        cursor: str = "pointer",
        is_draggable: bool = False,
        is_progressive: bool = False,
        width: Numeric = 0,
        height: Numeric = 0,
    ):
        self.opts: dict = {
            "id": id_,
            "$action": action,
            "position": position,
            "rotation": rotation,
            "scale": scale,
            "origin": origin,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "bounding": bounding,
            "z": z,
            "zlevel": z_level,
            "silent": is_silent,
            "invisible": is_invisible,
            "ignore": is_ignore,
            "cursor": cursor,
            "draggable": is_draggable,
            "progressive": is_progressive,
            "width": width,
            "height": height,
        }


class GraphicGroup(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        is_diff_children_by_name: bool = False,
        children: Optional[Sequence[BaseGraphic]] = None,
    ):
        self.opts: dict = {
            "type": "group",
            "diffChildrenByName": is_diff_children_by_name,
            "children": children,
        }

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)


class GraphicImage(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_imagestyle_opts: Union[GraphicImageStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "image"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_imagestyle_opts:
            if isinstance(graphic_imagestyle_opts, GraphicImageStyleOpts):
                self.opts.update(style=graphic_imagestyle_opts.opts)
            else:
                self.opts.update(style=graphic_imagestyle_opts)


class GraphicText(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_textstyle_opts: Union[GraphicTextStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "text"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_textstyle_opts:
            if isinstance(graphic_textstyle_opts, GraphicTextStyleOpts):
                self.opts.update(style=graphic_textstyle_opts.opts)
            else:
                self.opts.update(style=graphic_textstyle_opts)


class GraphicRect(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_shape_opts: Union[GraphicShapeOpts, dict, None] = None,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "rect"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_shape_opts:
            if isinstance(graphic_shape_opts, GraphicShapeOpts):
                self.opts.update(shape=graphic_shape_opts.opts)
            else:
                self.opts.update(graphic_shape_opts)

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(style=graphic_basicstyle_opts.opts)
            else:
                self.opts.update(style=graphic_basicstyle_opts)


class SankeyLevelsOpts(BasicOpts):
    def __init__(
        self,
        depth: Numeric = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "depth": depth,
            "itemStyle": itemstyle_opts,
            "lineStyle": linestyle_opts,
        }


class TreeMapItemStyleOpts(BasicOpts):
    def __init__(
        self,
        color: Optional[str] = None,
        color_alpha: Union[Numeric, Sequence] = None,
        color_saturation: Union[Numeric, Sequence] = None,
        border_color: Optional[str] = None,
        border_width: Numeric = 0,
        border_color_saturation: Union[Numeric, Sequence] = None,
        gap_width: Numeric = 0,
        stroke_color: Optional[str] = None,
        stroke_width: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "color": color,
            "colorAlpha": color_alpha,
            "colorSaturation": color_saturation,
            "gapWidth": gap_width,
            "borderColor": border_color,
            "borderWidth": border_width,
            "borderColorSaturation": border_color_saturation,
            "strokeColor": stroke_color,
            "strokeWidth": stroke_width,
        }


class TreeMapLevelsOpts(BasicOpts):
    def __init__(
        self,
        color: Union[str, Sequence] = None,
        color_alpha: Union[Numeric, Sequence] = None,
        color_saturation: Union[Numeric, Sequence] = None,
        color_mapping_by: str = "index",
        treemap_itemstyle_opts: Union[TreeMapItemStyleOpts, dict, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        upper_label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "color": color,
            "colorAlpha": color_alpha,
            "colorSaturation": color_saturation,
            "colorMappingBy": color_mapping_by,
            "itemStyle": treemap_itemstyle_opts,
            "label": label_opts,
            "upperLabel": upper_label_opts,
        }


class Map3DLabelOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        distance: Numeric = None,
        formatter: Optional[JSFunc] = None,
        text_style: Union[TextStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "distance": distance,
            "formatter": formatter,
            "textStyle": text_style,
        }


class Map3DRealisticMaterialOpts(BasicOpts):
    def __init__(
        self,
        detail_texture: Optional[JSFunc] = None,
        texture_tiling: Numeric = 1,
        texture_offset: Numeric = 0,
        roughness: Numeric = 0.5,
        metalness: Numeric = 0,
        roughness_adjust: Numeric = 0.5,
        metalness_adjust: Numeric = 0.5,
        normal_texture: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "detailTexture": detail_texture,
            "textureTiling": texture_tiling,
            "textureOffset": texture_offset,
            "roughness": roughness,
            "metalness": metalness,
            "roughnessAdjust": roughness_adjust,
            "metalnessAdjust": metalness_adjust,
            "normalTexture": normal_texture,
        }


class Map3DLambertMaterialOpts(BasicOpts):
    def __init__(
        self,
        detail_texture: Optional[JSFunc] = None,
        texture_tiling: Numeric = 1,
        texture_offset: Numeric = 0,
    ):
        self.opts: dict = {
            "detailTexture": detail_texture,
            "textureTiling": texture_tiling,
            "textureOffset": texture_offset,
        }


class Map3DColorMaterialOpts(BasicOpts):
    def __init__(
        self,
        detail_texture: Optional[JSFunc] = None,
        texture_tiling: Numeric = 1,
        texture_offset: Numeric = 0,
    ):
        self.opts: dict = {
            "detailTexture": detail_texture,
            "textureTiling": texture_tiling,
            "textureOffset": texture_offset,
        }


class Map3DLightOpts(BasicOpts):
    def __init__(
        self,
        main_color: str = "#fff",
        main_intensity: Numeric = 1,
        is_main_shadow: bool = False,
        main_shadow_quality: str = "medium",
        main_alpha: Numeric = 40,
        main_beta: Numeric = 40,
        ambient_color: str = "#fff",
        ambient_intensity: Numeric = 0.2,
        ambient_cubemap_texture: Optional[str] = None,
        ambient_cubemap_diffuse_intensity: Numeric = 0.5,
        ambient_cubemap_specular_intensity: Numeric = 0.5,
    ):
        self.opts: dict = {
            "main": {
                "color": main_color,
                "intensity": main_intensity,
                "shadow": is_main_shadow,
                "shadowQuality": main_shadow_quality,
                "alpha": main_alpha,
                "beta": main_beta,
            },
            "ambient": {"color": ambient_color, "intensity": ambient_intensity},
            "ambientCubemap": {
                "texture": ambient_cubemap_texture,
                "diffuseIntensity": ambient_cubemap_diffuse_intensity,
                "specularIntensity": ambient_cubemap_specular_intensity,
            },
        }


class Map3DPostEffectOpts(BasicOpts):
    def __init__(
        self,
        is_enable: bool = False,
        is_bloom_enable: bool = False,
        bloom_intensity: Numeric = 0.1,
        is_depth_field_enable: bool = False,
        depth_field_focal_distance: Numeric = 50,
        depth_field_focal_range: Numeric = 20,
        depth_field_fstop: Numeric = 2.8,
        depth_field_blur_radius: Numeric = 10,
        is_ssao_enable: bool = False,
        ssao_quality: str = "medium",
        ssao_radius: Numeric = 2,
        ssao_intensity: Numeric = 1,
        is_color_correction_enable: bool = False,
        color_correction_lookup_texture: Optional[JSFunc] = None,
        color_correction_exposure: Numeric = 0,
        color_correction_brightness: Numeric = 0,
        color_correction_contrast: Numeric = 1,
        color_correction_saturation: Numeric = 1,
        is_fxaa_enable: bool = False,
    ):
        self.opts: dict = {
            "enable": is_enable,
            "bloom": {"enable": is_bloom_enable, "bloomIntensity": bloom_intensity},
            "depthOfField": {
                "enable": is_depth_field_enable,
                "focalDistance": depth_field_focal_distance,
                "focalRange": depth_field_focal_range,
                "fstop": depth_field_fstop,
                "blurRadius": depth_field_blur_radius,
            },
            "SSAO": {
                "enable": is_ssao_enable,
                "quality": ssao_quality,
                "radius": ssao_radius,
                "intensity": ssao_intensity,
            },
            "colorCorrection": {
                "enable": is_color_correction_enable,
                "lookupTexture": color_correction_lookup_texture,
                "exposure": color_correction_exposure,
                "brightness": color_correction_brightness,
                "contrast": color_correction_contrast,
                "saturation": color_correction_saturation,
            },
            "FXAA": {"enable": is_fxaa_enable},
        }


class Map3DViewControlOpts(BasicOpts):
    def __init__(
        self,
        projection: str = "perspective",
        auto_rotate: bool = False,
        auto_rotate_direction: str = "cw",
        auto_rotate_speed: Numeric = 10,
        auto_rotate_after_still: Numeric = 3,
        damping: Numeric = 0.8,
        rotate_sensitivity: Union[Numeric, Sequence] = 1,
        zoom_sensitivity: Numeric = 1,
        pan_sensitivity: Numeric = 1,
        pan_mouse_button: str = "left",
        rotate_mouse_button: str = "middle",
        distance: Numeric = 100,
        min_distance: Numeric = 40,
        max_distance: Numeric = 400,
        orthographic_size: Numeric = 100,
        min_orthographic_size: Numeric = 20,
        max_orthographic_size: Numeric = 400,
        alpha: Numeric = 40,
        beta: Numeric = 0,
        center: Optional[Sequence] = None,
        min_alpha: Numeric = 5,
        max_alpha: Numeric = 90,
        min_beta: Numeric = -80,
        max_beta: Numeric = 80,
        animation: bool = True,
        animation_duration_update: Numeric = 1000,
        animation_easing_update: str = "cubicInOut",
    ):
        self.opts: dict = {
            "projection": projection,
            "autoRotate": auto_rotate,
            "autoRotateDirection": auto_rotate_direction,
            "autoRotateSpeed": auto_rotate_speed,
            "autoRotateAfterStill": auto_rotate_after_still,
            "damping": damping,
            "rotateSensitivity": rotate_sensitivity,
            "zoomSensitivity": zoom_sensitivity,
            "panSensitivity": pan_sensitivity,
            "panMouseButton": pan_mouse_button,
            "rotateMouseButton": rotate_mouse_button,
            "distance": distance,
            "minDistance": min_distance,
            "maxDistance": max_distance,
            "orthographicSize": orthographic_size,
            "minOrthographicSize": min_orthographic_size,
            "maxOrthographicSize": max_orthographic_size,
            "alpha": alpha,
            "beta": beta,
            "center": center,
            "minAlpha": min_alpha,
            "maxAlpha": max_alpha,
            "minBeta": min_beta,
            "maxBeta": max_beta,
            "animation": animation,
            "animationDurationUpdate": animation_duration_update,
            "animationEasingUpdate": animation_easing_update,
        }


class GlobeLayersOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        type_: str = "overlay",
        name: Optional[str] = None,
        blend_to: str = "albedo",
        intensity: Numeric = 1,
        shading: str = "lambert",
        distance: Optional[Numeric] = None,
        texture: Union[JSFunc, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "type": type_,
            "name": name,
            "blendTo": blend_to,
            "intensity": intensity,
            "shading": shading,
            "distance": distance,
            "texture": texture,
        }


class BarBackgroundStyleOpts(BasicOpts):
    def __init__(
        self,
        color: str = "rgba(180, 180, 180, 0.2)",
        border_color: str = "#000",
        border_width: Numeric = 0,
        border_type: str = "solid",
        border_radius: Union[Numeric, Sequence] = 0,
        shadow_blur: Optional[Numeric] = None,
        shadow_color: Optional[str] = None,
        shadow_offset_x: Numeric = 0,
        shadow_offset_y: Numeric = 0,
        opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "color": color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "borderType": border_type,
            "borderRadius": border_radius,
            "shadowBlur": shadow_blur,
            "shadowColor": shadow_color,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "opacity": opacity,
        }


class GaugeTitleOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        offset_center: Sequence = None,
        color: str = "#333",
        font_style: str = "normal",
        font_weight: str = "normal",
        font_family: str = "sans-serif",
        font_size: Numeric = 15,
        background_color: str = "transparent",
        border_color: str = "transparent",
        border_width: Numeric = 0,
        border_radius: Numeric = 0,
        padding: Numeric = 0,
        shadow_color: Optional[str] = "transparent",
        shadow_blur: Optional[Numeric] = 0,
        shadow_offset_x: Numeric = 0,
        shadow_offset_y: Numeric = 0,
        overflow: Optional[str] = "none",
        rich: Optional[dict] = None,
        is_value_animation: bool = True,
    ):
        if offset_center is None:
            offset_center = [0, "-40%"]
        self.opts: dict = {
            "show": is_show,
            "offsetCenter": offset_center,
            "color": color,
            "fontStyle": font_style,
            "fontWeight": font_weight,
            "fontFamily": font_family,
            "fontSize": font_size,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "borderRadius": border_radius,
            "padding": padding,
            "shadowColor": shadow_color,
            "shadowBlur": shadow_blur,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "overflow": overflow,
            "rich": rich,
            "valueAnimation": is_value_animation,
        }


class GaugeDetailOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        background_color: str = "transparent",
        border_width: Numeric = 0,
        border_color: str = "transparent",
        offset_center: Sequence = None,
        formatter: Optional[JSFunc] = None,
        color: str = "#464646",
        font_style: str = "normal",
        font_weight: str = "normal",
        font_family: str = "sans-serif",
        font_size: Numeric = 15,
        border_radius: Numeric = 0,
        padding: Numeric = 0,
        shadow_color: Optional[str] = "transparent",
        shadow_blur: Optional[Numeric] = 0,
        shadow_offset_x: Numeric = 0,
        shadow_offset_y: Numeric = 0,
        overflow: Optional[str] = "none",
        rich: Optional[dict] = None,
        is_value_animation: bool = True,
    ):
        if offset_center is None:
            offset_center = [0, "-40%"]
        self.opts: dict = {
            "show": is_show,
            "backgroundColor": background_color,
            "borderWidth": border_width,
            "borderColor": border_color,
            "offsetCenter": offset_center,
            "formatter": formatter,
            "color": color,
            "fontStyle": font_style,
            "fontWeight": font_weight,
            "fontFamily": font_family,
            "fontSize": font_size,
            "borderRadius": border_radius,
            "padding": padding,
            "shadowColor": shadow_color,
            "shadowBlur": shadow_blur,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "overflow": overflow,
            "rich": rich,
            "valueAnimation": is_value_animation,
        }


class GaugeProgressOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = False,
        is_overlap: bool = True,
        width: Numeric = 10,
        is_round_cap: bool = False,
        is_clip: bool = False,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "overlap": is_overlap,
            "width": width,
            "roundCap": is_round_cap,
            "clip": is_clip,
            "itemStyle": itemstyle_opts,
        }


class GaugePointerOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        length: Union[str, Numeric] = "80%",
        width: Numeric = 8,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "length": length,
            "width": width,
            "itemStyle": itemstyle_opts,
        }


class GaugeAnchorOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        is_show_above: bool = False,
        size: Numeric = 6,
        icon: str = "circle",
        offset_center: Optional[Sequence] = None,
        is_keep_aspect: bool = False,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
    ):
        if offset_center is None:
            offset_center = [0, 0]
        self.opts: dict = {
            "show": is_show,
            "showAbove": is_show_above,
            "size": size,
            "icon": icon,
            "offsetCenter": offset_center,
            "keepAspect": is_keep_aspect,
            "itemStyle": itemstyle_opts,
        }


class PieLabelLineOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        is_show_above: bool = False,
        length: Numeric = 15,
        length_2: Numeric = 15,
        smooth: Union[bool, Numeric] = False,
        min_turn_angle: Numeric = 90,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        max_surface_angle: Numeric = 90,
    ):
        self.opts: dict = {
            "show": is_show,
            "showAbove": is_show_above,
            "length": length,
            "length2": length_2,
            "smooth": smooth,
            "minTurnAngle": min_turn_angle,
            "lineStyle": linestyle_opts,
            "maxSurfaceAngle": max_surface_angle,
        }


class PieEmptyCircleStyle(BasicOpts):
    def __init__(
        self,
        color: str = "lightgray",
        border_color: str = "#000",
        border_width: Numeric = 0,
        border_type: str = "solid",
        border_dash_offset: Numeric = 0,
        border_cap: str = "butt",
        border_join: str = "bevel",
        border_miter_limit: Numeric = 10,
        opacity: Numeric = 1,
    ):
        self.opts: dict = {
            "color": color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "borderType": border_type,
            "borderDashOffset": border_dash_offset,
            "borderCap": border_cap,
            "borderJoin": border_join,
            "borderMiterLimit": border_miter_limit,
            "opacity": opacity,
        }


class TimelineCheckPointerStyle(BasicOpts):
    def __init__(
        self,
        symbol: str = "circle",
        symbol_size: Union[Numeric, Sequence[Numeric]] = 13,
        symbol_rotate: Optional[Numeric] = None,
        symbol_keep_aspect: bool = False,
        symbol_offset: Optional[Sequence[Union[str, Numeric]]] = None,
        color: str = "#c23531",
        border_width: Numeric = 5,
        border_color: str = "rgba(194,53,49,0.5)",
        is_animation: bool = True,
        animation_duration: Numeric = 300,
        animation_easing: str = "quinticInOut",
    ):
        if symbol_offset is None:
            symbol_offset = [0, 0]

        self.opts: dict = {
            "symbol": symbol,
            "symbolSize": symbol_size,
            "symbolRotate": symbol_rotate,
            "symbolKeepAspect": symbol_keep_aspect,
            "symbolOffset": symbol_offset,
            "color": color,
            "borderWidth": border_width,
            "borderColor": border_color,
            "animation": is_animation,
            "animationDuration": animation_duration,
            "animationEasing": animation_easing,
        }


class TimelineControlStyle(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        is_show_play_button: bool = True,
        is_show_prev_button: bool = True,
        is_show_next_button: bool = True,
        item_size: Numeric = 22,
        item_gap: Numeric = 12,
        position: str = "left",
        play_icon: Optional[str] = None,
        stop_icon: Optional[str] = None,
        prev_icon: Optional[str] = None,
        next_icon: Optional[str] = None,
        color: str = "#304654",
        border_color: str = "#304654",
        border_width: Numeric = 1,
    ):
        self.opts: dict = {
            "show": is_show,
            "showPlayBtn": is_show_play_button,
            "showPrevBtn": is_show_prev_button,
            "showNextBtn": is_show_next_button,
            "itemSize": item_size,
            "itemGap": item_gap,
            "position": position,
            "playIcon": play_icon,
            "stopIcon": stop_icon,
            "prevIcon": prev_icon,
            "nextIcon": next_icon,
            "color": color,
            "borderColor": border_color,
            "borderWidth": border_width,
        }


class TabChartGlobalOpts(BasicOpts):
    def __init__(
        self,
        is_enable: bool = False,
        tab_base_css: Optional[dict] = None,
        tab_button_css: Optional[dict] = None,
        tab_button_hover_css: Optional[dict] = None,
        tab_button_active_css: Optional[dict] = None,
    ):
        self.opts: dict = {
            "enable": is_enable,
            "base": tab_base_css,
            "button_base": tab_button_css,
            "button_hover": tab_button_hover_css,
            "button_active": tab_button_active_css,
        }


class GraphGLNode(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        x: Optional[Numeric] = None,
        y: Optional[Numeric] = None,
        value: Union[str, Numeric, Sequence, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "x": x,
            "y": y,
            "value": value,
            "itemStyle": itemstyle_opts,
        }


class GraphGLLink(BasicOpts):
    def __init__(
        self,
        source: Union[str, int, None] = None,
        target: Union[str, int, None] = None,
        value: Optional[Numeric] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "source": source,
            "target": target,
            "value": value,
            "lineStyle": linestyle_opts,
        }


class GeoRegionsOpts(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        is_selected: bool = False,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        emphasis_itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        emphasis_label_opts: Union[LabelOpts, dict, None] = None,
        select_itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        select_label_opts: Union[LabelOpts, dict, None] = None,
        blur_itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        blur_label_opts: Union[LabelOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
        is_silent: bool = False,
    ):
        self.opts: dict = {
            "name": name,
            "selected": is_selected,
            "itemStyle": itemstyle_opts,
            "label": label_opts,
            "emphasis": {
                "itemStyle": emphasis_itemstyle_opts,
                "label": emphasis_label_opts,
            },
            "select": {
                "itemStyle": select_itemstyle_opts,
                "label": select_label_opts,
            },
            "blur": {
                "itemStyle": blur_itemstyle_opts,
                "label": blur_label_opts,
            },
            "tooltip": tooltip_opts,
            "silent": is_silent,
        }


class SunburstLabelLineOpts(BasicOpts):
    def __init__(
        self,
        is_show: Optional[bool] = None,
        is_show_above: Optional[bool] = None,
        length_2: Optional[Numeric] = None,
        smooth: Union[bool, Numeric] = False,
        min_turn_angle: Optional[Numeric] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "showAbove": is_show_above,
            "length2": length_2,
            "smooth": smooth,
            "minTurnAngle": min_turn_angle,
            "lineStyle": linestyle_opts,
        }


class SunburstLabelLayoutOpts(BasicOpts):
    def __init__(
        self,
        is_hide_overlap: Optional[bool] = None,
        is_move_overlap: Optional[bool] = None,
        rotate: Optional[Numeric] = None,
        width: Optional[Numeric] = None,
        height: Optional[Numeric] = None,
        align: Optional[str] = None,
        vertical_align: Optional[str] = None,
        font_size: Optional[Numeric] = None,
        is_draggable: Optional[bool] = None,
    ):
        self.opts: dict = {
            "hideOverlap": is_hide_overlap,
            "moveOverlap": is_move_overlap,
            "rotate": rotate,
            "width": width,
            "height": height,
            "align": align,
            "verticalAlign": vertical_align,
            "fontSize": font_size,
            "draggable": is_draggable,
        }


class SunburstLevelOpts(BasicOpts):
    def __init__(
        self,
        radius: Optional[Sequence] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        label_line_opts: Union[SunburstLabelLineOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "radius": radius,
            "label": label_opts,
            "labelLine": label_line_opts,
            "itemStyle": itemstyle_opts,
        }


# Data Item
class BarItem(BasicOpts):
    def __init__(
        self,
        name: Union[int, str, None],
        value: Numeric,
        *,
        group_id: Optional[str] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        is_show_label_line: Optional[bool] = None,
        label_line_linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        label_line = None
        if is_show_label_line:
            label_line = {
                "show": is_show_label_line,
                "lineStyle": label_line_linestyle_opts,
            }

        self.opts: dict = {
            "name": name,
            "value": value,
            "groupId": group_id,
            "label": label_opts,
            "labelLine": label_line,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class BoxplotItem(BasicOpts):
    def __init__(
        self,
        name: Union[int, str],
        value: Sequence,
        *,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class CandleStickItem(BasicOpts):
    def __init__(
        self,
        name: Union[str, int],
        value: Sequence,
        *,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class EffectScatterItem(BasicOpts):
    def __init__(
        self,
        name: Union[str, Numeric],
        value: Union[str, Numeric],
        *,
        symbol: Optional[str] = None,
        symbol_size: Union[Sequence[Numeric], Numeric] = None,
        symbol_rotate: Optional[Numeric] = None,
        symbol_keep_aspect: bool = False,
        symbol_offset: Optional[Sequence] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "symbolRotate": symbol_rotate,
            "symbolKeepAspect": symbol_keep_aspect,
            "symbolOffset": symbol_offset,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class FunnelItem(BasicOpts):
    def __init__(
        self,
        name: Union[str, int],
        value: Union[Sequence, str, Numeric],
        *,
        is_show_label_line: Optional[bool] = None,
        label_line_width: Optional[int] = None,
        label_line_linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "labelLine": {
                "show": is_show_label_line,
                "length": label_line_width,
                "lineStyle": label_line_linestyle_opts,
            },
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class LineItem(BasicOpts):
    def __init__(
        self,
        name: Union[str, Numeric] = None,
        value: Union[str, Numeric] = None,
        *,
        symbol: Optional[str] = "circle",
        symbol_size: Numeric = 4,
        symbol_rotate: Optional[Numeric] = None,
        symbol_keep_aspect: bool = False,
        symbol_offset: Optional[Sequence] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "symbolRotate": symbol_rotate,
            "symbolKeepAspect": symbol_keep_aspect,
            "symbolOffset": symbol_offset,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class MapItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Union[Sequence, Numeric, str] = None,
        group_id: Optional[str] = None,
        is_selected: bool = False,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "groupId": group_id,
            "selected": is_selected,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class GeoItem(BasicOpts):
    def __init__(
        self,
        longitude: Numeric,
        latitude: Numeric,
        name: str,
        value: Union[Sequence, Numeric, str] = None,
    ):
        self.opts: dict = {
            "longitude": longitude,
            "latitude": latitude,
            "name": name,
            "value": value,
        }


class ParallelItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Sequence] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        color: Union[str, dict] = "#000",
        width: Numeric = 2,
        type_: str = "solid",
        dash_offset: Numeric = 0,
        cap: str = "butt",
        join: str = "bevel",
        miter_limit: Optional[Numeric] = None,
        opacity: Numeric = 0.45,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "lineStyle": linestyle_opts,
            "color": color,
            "width": width,
            "type": type_,
            "dashOffset": dash_offset,
            "cap": cap,
            "join": join,
            "miterLimit": miter_limit,
            "opacity": opacity,
        }


class PieItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Numeric] = None,
        group_id: Optional[str] = None,
        is_selected: bool = False,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
        label_line_opts: Union[PieLabelLineOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "groupId": group_id,
            "selected": is_selected,
            "label": label_opts,
            "labelLine": label_line_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class RadarItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Union[Sequence, Numeric, str] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Sequence[Numeric], Numeric] = None,
        symbol_rotate: Optional[Numeric] = None,
        symbol_keep_aspect: bool = False,
        symbol_offset: Optional[Sequence] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        areastyle_opts: Union[AreaStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "symbolRotate": symbol_rotate,
            "symbolKeepAspect": symbol_keep_aspect,
            "symbolOffset": symbol_offset,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
            "lineStyle": linestyle_opts,
            "areaStyle": areastyle_opts,
        }


class ScatterItem(BasicOpts):
    def __init__(
        self,
        name: Union[str, Numeric] = None,
        value: Union[str, Numeric] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Sequence[Numeric], Numeric] = None,
        symbol_rotate: Optional[Numeric] = None,
        symbol_keep_aspect: bool = False,
        symbol_offset: Optional[Sequence] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "symbolRotate": symbol_rotate,
            "symbolKeepAspect": symbol_keep_aspect,
            "symbolOffset": symbol_offset,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class SunburstItem(BasicOpts):
    def __init__(
        self,
        value: Optional[Numeric] = None,
        name: Optional[str] = None,
        link: Optional[str] = None,
        target: Optional[str] = "blank",
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        children: Optional[Sequence] = None,
    ):
        self.opts: dict = {
            "value": value,
            "name": name,
            "link": link,
            "target": target,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "children": children,
        }


class ThemeRiverItem(BasicOpts):
    def __init__(
        self,
        date: Optional[str] = None,
        value: Optional[Numeric] = None,
        name: Optional[str] = None,
    ):
        self.opts: dict = {"date": date, "value": value, "name": name}


class TreeItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Numeric] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        children: Optional[Sequence] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "children": children,
            "label": label_opts,
        }
