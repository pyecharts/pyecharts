from ..globals import CurrentConfig, RenderType, ThemeType
from ..options.series_options import (
    BasicOpts,
    AnimationOpts,
    AreaStyleOpts,
    ItemStyleOpts,
    JSFunc,
    LabelOpts,
    LineStyleOpts,
    Numeric,
    MinorTickOpts,
    MinorSplitLineOpts,
    Optional,
    Sequence,
    SplitAreaOpts,
    SplitLineOpts,
    TextStyleOpts,
    Union,
)


class AriaLabelOpts(BasicOpts):
    def __init__(
        self,
        is_enable: bool = True,
        description: Optional[str] = None,
        general_with_title: str = "这是一个关于“{title}”的图表。",
        general_without_title: str = "这是一个图表，",
        series_max_count: int = 10,
        series_single_prefix: str = "",
        series_single_with_name: str = "图表类型是{seriesType}，表示{seriesName}。",
        series_single_without_name: str = "图表类型是{seriesType}。",
        series_multiple_prefix: str = "它由{seriesCount}个图表系列组成。",
        series_multiple_with_name: str = "图表类型是{seriesType}，表示{seriesName}。",
        series_multiple_without_name: str = "图表类型是{seriesType}。",
        series_multiple_separator_middle: str = "；",
        series_multiple_separator_end: str = "。",
        data_max_count: int = 10,
        data_all_data: str = "其数据是——",
        data_partial_data: str = "其中，前{displayCnt}项是——",
        data_with_name: str = "{name}的数据是{value}",
        data_without_name: str = "{value}",
        data_separator_middle: str = "，",
        data_separator_end: str = "",
    ):
        self.opts: dict = {
            "enabled": is_enable,
            "description": description,
            "general": {
                "withTitle": general_with_title,
                "withoutTitle": general_without_title,
            },
            "series": {
                "maxCount": series_max_count,
                "single": {
                    "prefix": series_single_prefix,
                    "withName": series_single_with_name,
                    "withoutName": series_single_without_name,
                },
                "multiple": {
                    "prefix": series_multiple_prefix,
                    "withName": series_multiple_with_name,
                    "withoutName": series_multiple_without_name,
                    "separator": {
                        "middle": series_multiple_separator_middle,
                        "end": series_multiple_separator_end,
                    },
                },
            },
            "data": {
                "maxCount": data_max_count,
                "allData": data_all_data,
                "partialData": data_partial_data,
                "withName": data_with_name,
                "withoutName": data_without_name,
                "separator": {
                    "middle": data_separator_middle,
                    "end": data_separator_end,
                },
            },
        }


class AriaDecalOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = False,
        decals_symbol: Union[str, Sequence] = "rect",
        decals_symbol_size: Numeric = 1,
        decals_symbol_keep_aspect: bool = True,
        decals_color: str = "rgba(0, 0, 0, 0.2)",
        decals_background_color: Optional[str] = None,
        decals_dash_array_x: Union[Numeric, Sequence] = 5,
        decals_dash_array_y: Union[Numeric, Sequence] = 5,
        decals_rotation: Numeric = 0,
        decals_max_tile_width: Numeric = 512,
        decals_max_tile_height: Numeric = 512,
    ):
        self.opts: dict = {
            "show": is_show,
            "decals": {
                "symbol": decals_symbol,
                "symbolSize": decals_symbol_size,
                "symbolKeepAspect": decals_symbol_keep_aspect,
                "color": decals_color,
                "backgroundColor": decals_background_color,
                "dashArrayX": decals_dash_array_x,
                "dashArrayY": decals_dash_array_y,
                "rotation": decals_rotation,
                "maxTileWidth": decals_max_tile_width,
                "maxTileHeight": decals_max_tile_height,
            },
        }


class AriaOpts(BasicOpts):
    def __init__(
        self,
        is_enable: bool = False,
        aria_label_opts: Optional[AriaLabelOpts] = None,
        aria_decal_opts: Optional[AriaDecalOpts] = None,
    ):
        self.opts: dict = {
            "enabled": is_enable,
            "label": aria_label_opts,
            "decal": aria_decal_opts,
        }


class InitOpts(BasicOpts):
    def __init__(
        self,
        width: str = "900px",
        height: str = "500px",
        is_horizontal_center: bool = False,
        chart_id: Optional[str] = None,
        renderer: str = RenderType.CANVAS,
        page_title: str = CurrentConfig.PAGE_TITLE,
        theme: str = ThemeType.WHITE,
        bg_color: Union[str, dict] = None,
        is_fill_bg_color: bool = False,
        js_host: str = "",
        animation_opts: Union[AnimationOpts, dict] = AnimationOpts(),
        aria_opts: Union[AriaOpts, dict] = AriaOpts(),
    ):
        self.opts: dict = {
            "width": width,
            "height": height,
            "is_horizontal_center": is_horizontal_center,
            "chart_id": chart_id,
            "renderer": renderer,
            "page_title": page_title,
            "theme": theme,
            "bg_color": bg_color,
            "fill_bg": is_fill_bg_color,
            "js_host": js_host,
            "animationOpts": animation_opts,
            "ariaOpts": aria_opts,
        }


class RenderOpts(BasicOpts):
    def __init__(self, is_embed_js: bool = False):
        self.opts: dict = {
            "embed_js": is_embed_js,
        }


class ToolBoxFeatureSaveAsImageOpts(BasicOpts):
    def __init__(
        self,
        type_: str = "png",
        name: Optional[str] = None,
        background_color: str = "auto",
        connected_background_color: str = "#fff",
        exclude_components: Optional[Sequence[str]] = None,
        is_show: bool = True,
        title: str = "保存为图片",
        icon: Optional[JSFunc] = None,
        pixel_ratio: Numeric = 1,
    ):
        self.opts: dict = {
            "type": type_,
            "name": name,
            "backgroundColor": background_color,
            "connectedBackgroundColor": connected_background_color,
            "excludeComponents": exclude_components,
            "show": is_show,
            "title": title,
            "icon": icon,
            "pixelRatio": pixel_ratio,
        }


class ToolBoxFeatureRestoreOpts(BasicOpts):
    def __init__(
        self, is_show: bool = True, title: str = "还原", icon: Optional[JSFunc] = None
    ):
        self.opts: dict = {"show": is_show, "title": title, "icon": icon}


class ToolBoxFeatureDataViewOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        title: str = "数据视图",
        icon: Optional[JSFunc] = None,
        is_read_only: bool = False,
        option_to_content: Optional[JSFunc] = None,
        content_to_option: Optional[JSFunc] = None,
        lang: Optional[Sequence[str]] = None,
        background_color: str = "#fff",
        text_area_color: str = "#fff",
        text_area_border_color: str = "#333",
        text_color: str = "#000",
        button_color: str = "#c23531",
        button_text_color: str = "#fff",
    ):
        if lang is None:
            lang = ["数据视图", "关闭", "刷新"]

        self.opts: dict = {
            "show": is_show,
            "title": title,
            "icon": icon,
            "readOnly": is_read_only,
            "optionToContent": option_to_content,
            "contentToOption": content_to_option,
            "lang": lang,
            "backgroundColor": background_color,
            "textareaColor": text_area_color,
            "textareaBorderColor": text_area_border_color,
            "textColor": text_color,
            "buttonColor": button_color,
            "buttonTextColor": button_text_color,
        }


class ToolBoxFeatureDataZoomOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        zoom_title: str = "区域缩放",
        back_title: str = "区域缩放还原",
        zoom_icon: Optional[JSFunc] = None,
        back_icon: Optional[JSFunc] = None,
        xaxis_index: Union[Numeric, Sequence, bool] = None,
        yaxis_index: Union[Numeric, Sequence, bool] = None,
        filter_mode: str = "filter",
    ):
        self.opts: dict = {
            "show": is_show,
            "title": {"zoom": zoom_title, "back": back_title},
            "icon": {"zoom": zoom_icon, "back": back_icon},
            "xAxisIndex": xaxis_index,
            "yAxisIndex": yaxis_index,
            "filterMode": filter_mode,
        }


class ToolBoxFeatureMagicTypeOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        type_: Optional[Sequence] = None,
        line_title: str = "切换为折线图",
        bar_title: str = "切换为柱状图",
        stack_title: str = "切换为堆叠",
        tiled_title: str = "切换为平铺",
        line_icon: Optional[JSFunc] = None,
        bar_icon: Optional[JSFunc] = None,
        stack_icon: Optional[JSFunc] = None,
        tiled_icon: Optional[JSFunc] = None,
    ):
        if type_ is None:
            type_ = ["line", "bar", "stack", "tiled"]

        self.opts: dict = {
            "show": is_show,
            "type": type_,
            "title": {
                "line": line_title,
                "bar": bar_title,
                "stack": stack_title,
                "tiled": tiled_title,
            },
            "icon": {
                "line": line_icon,
                "bar": bar_icon,
                "stack": stack_icon,
                "tiled": tiled_icon,
            },
        }


class ToolBoxFeatureBrushOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        rect_icon: Optional[JSFunc] = None,
        polygon_icon: Optional[JSFunc] = None,
        line_x_icon: Optional[JSFunc] = None,
        line_y_icon: Optional[JSFunc] = None,
        keep_icon: Optional[JSFunc] = None,
        clear_icon: Optional[JSFunc] = None,
        rect_title: str = "矩形选择",
        polygon_title: str = "圈选",
        line_x_title: str = "横向选择",
        line_y_title: str = "纵向选择",
        keep_title: str = "保持选择",
        clear_title: str = "清除选择",
    ):
        self.opts: dict = {
            "type": type_,
            "icon": {
                "rect": rect_icon,
                "polygon": polygon_icon,
                "lineX": line_x_icon,
                "lineY": line_y_icon,
                "keep": keep_icon,
                "clear": clear_icon,
            },
            "title": {
                "rect": rect_title,
                "polygon": polygon_title,
                "lineX": line_x_title,
                "lineY": line_y_title,
                "keep": keep_title,
                "clear": clear_title,
            },
        }


class ToolBoxFeatureOpts(BasicOpts):
    def __init__(
        self,
        save_as_image: Union[
            ToolBoxFeatureSaveAsImageOpts, dict
        ] = ToolBoxFeatureSaveAsImageOpts(),
        restore: Union[ToolBoxFeatureRestoreOpts, dict] = ToolBoxFeatureRestoreOpts(),
        data_view: Union[
            ToolBoxFeatureDataViewOpts, dict
        ] = ToolBoxFeatureDataViewOpts(),
        data_zoom: Union[
            ToolBoxFeatureDataZoomOpts, dict
        ] = ToolBoxFeatureDataZoomOpts(),
        magic_type: Union[
            ToolBoxFeatureMagicTypeOpts, dict
        ] = ToolBoxFeatureMagicTypeOpts(),
        brush: Union[ToolBoxFeatureBrushOpts, dict] = None,
    ):
        self.opts: dict = {
            "saveAsImage": save_as_image,
            "restore": restore,
            "dataView": data_view,
            "dataZoom": data_zoom,
            "magicType": magic_type,
            "brush": brush,
        }


class ToolboxOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        orient: str = "horizontal",
        item_size: Numeric = 15,
        item_gap: Numeric = 10,
        pos_left: str = "80%",
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        feature: Union[ToolBoxFeatureOpts, dict] = ToolBoxFeatureOpts(),
    ):
        self.opts: dict = {
            "show": is_show,
            "orient": orient,
            "itemSize": item_size,
            "itemGap": item_gap,
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
            "feature": feature,
        }


class BrushOpts(BasicOpts):
    def __init__(
        self,
        tool_box: Optional[Sequence] = None,
        brush_link: Union[Sequence, str] = None,
        series_index: Union[Sequence, Numeric, str] = None,
        geo_index: Union[Sequence, Numeric, str] = None,
        x_axis_index: Union[Sequence, Numeric, str] = None,
        y_axis_index: Union[Sequence, Numeric, str] = None,
        brush_type: str = "rect",
        brush_mode: str = "single",
        transformable: bool = True,
        brush_style: Optional[dict] = None,
        throttle_type: str = "fixRate",
        throttle_delay: Numeric = 0,
        remove_on_click: bool = True,
        in_brush: Optional[dict] = None,
        out_of_brush: Optional[dict] = None,
        z: Numeric = 10000,
    ):
        if tool_box is None:
            tool_box = ["rect", "polygon", "keep", "clear"]

        if brush_style is None:
            brush_style = {
                "borderWidth": 1,
                "color": "rgba(120,140,180,0.3)",
                "borderColor": "rgba(120,140,180,0.8)",
            }

        self.opts: dict = {
            "toolbox": tool_box,
            "brushLink": brush_link,
            "seriesIndex": series_index,
            "geoIndex": geo_index,
            "xAxisIndex": x_axis_index,
            "yAxisIndex": y_axis_index,
            "brushType": brush_type,
            "brushMode": brush_mode,
            "transformable": transformable,
            "brushStyle": brush_style,
            "throttleType": throttle_type,
            "throttleDelay": throttle_delay,
            "removeOnClick": remove_on_click,
            "inBrush": in_brush,
            "outOfBrush": out_of_brush,
            "z": z,
        }


class TitleOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        title: Optional[str] = None,
        title_link: Optional[str] = None,
        title_target: Optional[str] = "blank",
        subtitle: Optional[str] = None,
        subtitle_link: Optional[str] = None,
        subtitle_target: Optional[str] = "blank",
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        padding: Union[Sequence, Numeric] = 5,
        item_gap: Numeric = 10,
        text_align: str = "auto",
        text_vertical_align: str = "auto",
        is_trigger_event: bool = False,
        title_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        subtitle_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        self.opts: Sequence = [
            {
                "show": is_show,
                "text": title,
                "link": title_link,
                "target": title_target,
                "subtext": subtitle,
                "sublink": subtitle_link,
                "subtarget": subtitle_target,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "padding": padding,
                "itemGap": item_gap,
                "textAlign": text_align,
                "textVerticalAlign": text_vertical_align,
                "triggerEvent": is_trigger_event,
                "textStyle": title_textstyle_opts,
                "subtextStyle": subtitle_textstyle_opts,
            }
        ]


class DataZoomOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        type_: str = "slider",
        is_disabled: bool = False,
        is_realtime: bool = True,
        is_show_detail: bool = True,
        is_show_data_shadow: bool = True,
        range_start: Union[Numeric, None] = 20,
        range_end: Union[Numeric, None] = 80,
        start_value: Union[int, str, None] = None,
        end_value: Union[int, str, None] = None,
        min_span: Union[int, None] = None,
        max_span: Union[int, None] = None,
        min_value_span: Union[int, str, None] = None,
        max_value_span: Union[int, str, None] = None,
        orient: str = "horizontal",
        xaxis_index: Union[int, Sequence[int], None] = None,
        yaxis_index: Union[int, Sequence[int], None] = None,
        radius_axis_index: Union[int, Sequence[int], None] = None,
        angle_axis_index: Union[int, Sequence[int], None] = None,
        is_zoom_lock: bool = False,
        throttle: Optional[int] = None,
        range_mode: Optional[Sequence] = None,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        filter_mode: str = "filter",
        is_zoom_on_mouse_wheel: bool = True,
        is_move_on_mouse_move: bool = True,
        is_move_on_mouse_wheel: bool = True,
        is_prevent_default_mouse_move: bool = True,
    ):
        self.opts: dict = {
            "show": is_show,
            "type": type_,
            "showDetail": is_show_detail,
            "showDataShadow": is_show_data_shadow,
            "realtime": is_realtime,
            "startValue": start_value,
            "endValue": end_value,
            "start": range_start,
            "end": range_end,
            "minSpan": min_span,
            "maxSpan": max_span,
            "minValueSpan": min_value_span,
            "maxValueSpan": max_value_span,
            "orient": orient,
            "xAxisIndex": xaxis_index,
            "yAxisIndex": yaxis_index,
            "radiusAxisIndex": radius_axis_index,
            "angleAxisIndex": angle_axis_index,
            "zoomLock": is_zoom_lock,
            "throttle": throttle,
            "rangeMode": range_mode,
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
            "filterMode": filter_mode,
        }

        # inside have some different configurations.
        if type_ == "inside":
            self.opts.update({
                "disabled": is_disabled,
                "zoomOnMouseWheel": is_zoom_on_mouse_wheel,
                "moveOnMouseMove": is_move_on_mouse_move,
                "moveOnMouseWheel": is_move_on_mouse_wheel,
                "preventDefaultMouseMove": is_prevent_default_mouse_move,
            })


class LegendOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        selected_mode: Union[str, bool, None] = None,
        selected_map: Optional[dict] = None,
        is_show: bool = True,
        pos_left: Union[str, Numeric, None] = None,
        pos_right: Union[str, Numeric, None] = None,
        pos_top: Union[str, Numeric, None] = None,
        pos_bottom: Union[str, Numeric, None] = None,
        orient: Optional[str] = None,
        align: Optional[str] = None,
        padding: int = 5,
        item_gap: int = 10,
        item_width: int = 25,
        item_height: int = 14,
        inactive_color: Optional[str] = None,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        legend_icon: Optional[str] = None,
        background_color: Optional[str] = "transparent",
        border_color: Optional[str] = "#ccc",
        border_width: Optional[int] = None,
        border_radius: Union[int, Sequence] = 0,
        page_button_item_gap: int = 5,
        page_button_gap: Optional[int] = None,
        page_button_position: str = "end",
        page_formatter: JSFunc = "{current}/{total}",
        page_icon: Optional[str] = None,
        page_icon_color: str = "#2f4554",
        page_icon_inactive_color: str = "#aaa",
        page_icon_size: Union[int, Sequence] = 15,
        is_page_animation: Optional[bool] = None,
        page_animation_duration_update: int = 800,
        selector: Union[bool, Sequence] = False,
        selector_position: str = "auto",
        selector_item_gap: int = 7,
        selector_button_gap: int = 10,
    ):
        self.opts: dict = {
            "type": type_,
            "selectedMode": selected_mode,
            "selected": selected_map,
            "show": is_show,
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
            "orient": orient,
            "align": align,
            "padding": padding,
            "itemGap": item_gap,
            "itemWidth": item_width,
            "itemHeight": item_height,
            "inactiveColor": inactive_color,
            "textStyle": textstyle_opts,
            "icon": legend_icon,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "borderRadius": border_radius,
            "pageButtonItemGap": page_button_item_gap,
            "pageButtonGap": page_button_gap,
            "pageButtonPosition": page_button_position,
            "pageFormatter": page_formatter,
            "pageIcon": page_icon,
            "pageIconColor": page_icon_color,
            "pageIconInactiveColor": page_icon_inactive_color,
            "pageIconSize": page_icon_size,
            "animation": is_page_animation,
            "animationDurationUpdate": page_animation_duration_update,
            "selector": selector,
            "selectorPosition": selector_position,
            "selectorItemGap": selector_item_gap,
            "selectorButtonGap": selector_button_gap,
        }


class VisualMapOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        type_: str = "color",
        min_: Numeric = 0,
        max_: Numeric = 100,
        range_: Sequence[Numeric] = None,
        range_text: Optional[Sequence] = None,
        range_color: Optional[Sequence[str]] = None,
        range_size: Optional[Sequence[int]] = None,
        range_opacity: Union[Numeric, Sequence[Numeric]] = None,
        orient: str = "vertical",
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        padding: Union[int, Sequence[int]] = 5,
        split_number: int = 5,
        series_index: Union[Numeric, Sequence, None] = None,
        is_hover_link: bool = True,
        dimension: Optional[Numeric] = None,
        is_calculable: bool = True,
        is_piecewise: bool = False,
        is_inverse: bool = False,
        precision: Optional[int] = None,
        pieces: Optional[Sequence] = None,
        out_of_range: Optional[dict] = None,
        item_width: int = 0,
        item_height: int = 0,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: int = 0,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        _inrange_op: dict = {}
        if type_ == "color":
            range_color = range_color or ["#50a3ba", "#eac763", "#d94e5d"]
            _inrange_op.update(color=range_color)
        elif type_ == "size":
            range_size = range_size or [20, 50]
            _inrange_op.update(symbolSize=range_size)
        if range_opacity is not None:
            _inrange_op.update(opacity=range_opacity)

        _visual_typ = "piecewise" if is_piecewise else "continuous"

        if is_piecewise and item_width == 0 and item_height == 0:
            item_width, item_height = 20, 14
        elif item_width == 0 and item_height == 0:
            item_width, item_height = 20, 140

        self.opts: dict = {
            "show": is_show,
            "type": _visual_typ,
            "min": min_,
            "max": max_,
            "text": range_text,
            "textStyle": textstyle_opts,
            "range": range_,
            "inRange": _inrange_op,
            "calculable": is_calculable,
            "inverse": is_inverse,
            "precision": precision,
            "splitNumber": split_number,
            "dimension": dimension,
            "seriesIndex": series_index,
            "hoverLink": is_hover_link,
            "orient": orient,
            "left": pos_left,
            "top": pos_top,
            "bottom": pos_bottom,
            "right": pos_right,
            "padding": padding,
            "showLabel": True,
            "itemWidth": item_width,
            "itemHeight": item_height,
            "outOfRange": out_of_range,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
        }
        if is_piecewise:
            self.opts.update(pieces=pieces)


class TooltipOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        trigger: str = "item",
        trigger_on: str = "mousemove|click",
        axis_pointer_type: str = "line",
        is_show_content: bool = True,
        is_always_show_content: bool = False,
        show_delay: Numeric = 0,
        hide_delay: Numeric = 100,
        is_enterable: bool = False,
        is_confine: bool = False,
        is_append_to_body: bool = False,
        transition_duration: Numeric = 0.4,
        position: Union[str, Sequence, JSFunc] = None,
        formatter: Optional[JSFunc] = None,
        value_formatter: Optional[JSFunc] = None,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Numeric = 0,
        padding: Numeric = 5,
        textstyle_opts: Optional[TextStyleOpts] = TextStyleOpts(font_size=14),
        extra_css_text: Optional[str] = None,
        order: str = "seriesAsc",
    ):
        self.opts: dict = {
            "show": is_show,
            "trigger": trigger,
            "triggerOn": trigger_on,
            "axisPointer": {"type": axis_pointer_type},
            "showContent": is_show_content,
            "alwaysShowContent": is_always_show_content,
            "showDelay": show_delay,
            "hideDelay": hide_delay,
            "enterable": is_enterable,
            "confine": is_confine,
            "appendToBody": is_append_to_body,
            "transitionDuration": transition_duration,
            "position": position,
            "formatter": formatter,
            "valueFormatter": value_formatter,
            "textStyle": textstyle_opts,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "padding": padding,
            "extraCssText": extra_css_text,
            "order": order,
        }


class AxisLineOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        is_on_zero: bool = True,
        on_zero_axis_index: int = 0,
        symbol: Optional[str] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "onZero": is_on_zero,
            "onZeroAxisIndex": on_zero_axis_index,
            "symbol": symbol,
            "lineStyle": linestyle_opts,
        }


class AxisTickOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        is_align_with_label: bool = False,
        is_inside: bool = False,
        length: Optional[Numeric] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "alignWithLabel": is_align_with_label,
            "inside": is_inside,
            "length": length,
            "lineStyle": linestyle_opts,
        }


class AxisPointerOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = False,
        link: Sequence[dict] = None,
        type_: str = "line",
        is_snap: Optional[bool] = None,
        is_trigger_tooltip: bool = True,
        trigger_on: str = "mousemove|click",
        label: Union[LabelOpts, dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "type": type_,
            "snap": is_snap,
            "link": link,
            "label": label,
            "lineStyle": linestyle_opts,
            "triggerTooltip": is_trigger_tooltip,
            "triggerOn": trigger_on,
        }


class AxisOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        name: Optional[str] = None,
        is_show: bool = True,
        is_scale: bool = False,
        is_inverse: bool = False,
        name_location: str = "end",
        name_gap: Numeric = 15,
        name_rotate: Optional[Numeric] = None,
        interval: Optional[Numeric] = None,
        grid_index: Numeric = 0,
        position: Optional[str] = None,
        offset: Numeric = 0,
        split_number: Numeric = 5,
        boundary_gap: Union[str, bool, None] = None,
        min_: Union[Numeric, str, None] = None,
        max_: Union[Numeric, str, None] = None,
        min_interval: Numeric = 0,
        max_interval: Optional[Numeric] = None,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        axistick_opts: Union[AxisTickOpts, dict, None] = None,
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        axispointer_opts: Union[AxisPointerOpts, dict, None] = None,
        name_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        splitarea_opts: Union[SplitAreaOpts, dict, None] = None,
        splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(is_show=True),
        minor_tick_opts: Union[MinorTickOpts, dict, None] = None,
        minor_split_line_opts: Union[MinorSplitLineOpts, dict, None] = None,
        animation_opts: Union[AnimationOpts, dict] = AnimationOpts(),
    ):
        self.opts: dict = {
            "type": type_,
            "name": name,
            "show": is_show,
            "scale": is_scale,
            "nameLocation": name_location,
            "nameGap": name_gap,
            "nameRotate": name_rotate,
            "interval": interval,
            "nameTextStyle": name_textstyle_opts,
            "gridIndex": grid_index,
            "axisLine": axisline_opts,
            "axisTick": axistick_opts,
            "axisLabel": axislabel_opts,
            "axisPointer": axispointer_opts,
            "inverse": is_inverse,
            "position": position,
            "offset": offset,
            "splitNumber": split_number,
            "boundaryGap": boundary_gap,
            "min": min_,
            "max": max_,
            "minInterval": min_interval,
            "maxInterval": max_interval,
            "splitLine": splitline_opts,
            "splitArea": splitarea_opts,
            "minorTick": minor_tick_opts,
            "minorSplitLine": minor_split_line_opts,
        }

        if animation_opts:
            self.opts.update(**animation_opts.opts)


class GridOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = False,
        z_level: Numeric = 0,
        z: Numeric = 2,
        pos_left: Union[Numeric, str, None] = None,
        pos_top: Union[Numeric, str, None] = None,
        pos_right: Union[Numeric, str, None] = None,
        pos_bottom: Union[Numeric, str, None] = None,
        width: Union[Numeric, str, None] = None,
        height: Union[Numeric, str, None] = None,
        is_contain_label: bool = False,
        background_color: str = "transparent",
        border_color: str = "#ccc",
        border_width: Numeric = 1,
        shadow_blur: Optional[Numeric] = None,
        shadow_color: Optional[str] = None,
        shadow_offset_x: Numeric = 0,
        shadow_offset_y: Numeric = 0,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "zlevel": z_level,
            "z": z,
            "left": pos_left,
            "top": pos_top,
            "right": pos_right,
            "bottom": pos_bottom,
            "width": width,
            "height": height,
            "containLabel": is_contain_label,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "shadowBlur": shadow_blur,
            "shadowColor": shadow_color,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "tooltip": tooltip_opts,
        }


class Grid3DOpts(BasicOpts):
    def __init__(
        self,
        is_show: Optional[bool] = None,
        width: Numeric = 200,
        height: Numeric = 100,
        depth: Numeric = 80,
        is_rotate: bool = False,
        rotate_speed: Numeric = 10,
        rotate_sensitivity: Numeric = 1,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        axistick_opts: Union[AxisTickOpts, dict, None] = None,
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        axispointer_opts: Union[AxisPointerOpts, dict, None] = None,
        splitarea_opts: Union[SplitAreaOpts, dict, None] = None,
        splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(is_show=True),
        environment: JSFunc = "auto",
        view_control_alpha: Numeric = 20,
        view_control_beta: Numeric = 40,
        view_control_min_alpha: Numeric = -90,
        view_control_max_alpha: Numeric = 90,
        view_control_min_beta: Optional[int] = None,
        view_control_max_beta: Optional[int] = None,
        z_level: Numeric = -10,
        pos_left: Union[str, Numeric] = "auto",
        pos_top: Union[str, Numeric] = "auto",
        pos_right: Union[str, Numeric] = "auto",
        pos_bottom: Union[str, Numeric] = "auto",
    ):
        self.opts: dict = {
            "show": is_show,
            "boxWidth": width,
            "boxHeight": height,
            "boxDepth": depth,
            "axisLine": axisline_opts,
            "axisTick": axistick_opts,
            "axisLabel": axislabel_opts,
            "axisPointer": axispointer_opts,
            "splitLine": splitline_opts,
            "splitArea": splitarea_opts,
            "environment": environment,
            "viewControl": {
                "autoRotate": is_rotate,
                "autoRotateSpeed": rotate_speed,
                "rotateSensitivity": rotate_sensitivity,
                "alpha": view_control_alpha,
                "beta": view_control_beta,
                "minAlpha": view_control_min_alpha,
                "maxAlpha": view_control_max_alpha,
                "minBeta": view_control_min_beta,
                "maxBeta": view_control_max_beta,
            },
            "zlevel": z_level,
            "left": pos_left,
            "top": pos_top,
            "right": pos_right,
            "bottom": pos_bottom,
        }


class Axis3DOpts(BasicOpts):
    def __init__(
        self,
        data: Optional[Sequence] = None,
        type_: Optional[str] = None,
        name: Optional[str] = None,
        is_show: bool = True,
        is_scale: bool = False,
        grid_3d_index: Numeric = 0,
        name_gap: Numeric = 20,
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        split_number: Optional[Numeric] = None,
        log_base: Numeric = 10,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        axistick_opts: Union[AxisTickOpts, dict, None] = None,
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        axispointer_opts: Union[AxisPointerOpts, dict, None] = None,
        splitarea_opts: Union[SplitAreaOpts, dict, None] = None,
        splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(is_show=True),
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "data": data,
            "name": name,
            "show": is_show,
            "scale": is_scale,
            "grid3DIndex": grid_3d_index,
            "nameGap": name_gap,
            "nameTextStyle": textstyle_opts,
            "splitNumber": split_number,
            "logBase": log_base,
            "type": type_,
            "min": min_,
            "max": max_,
            "axisLine": axisline_opts,
            "axisTick": axistick_opts,
            "axisLabel": axislabel_opts,
            "axisPointer": axispointer_opts,
            "splitLine": splitline_opts,
            "splitArea": splitarea_opts,
        }


class ParallelOpts(BasicOpts):
    def __init__(
        self,
        pos_left: str = "5%",
        pos_right: str = "13%",
        pos_bottom: str = "10%",
        pos_top: str = "20%",
        layout: Optional[str] = None,
        is_axis_expandable: bool = False,
        axis_expand_center: Optional[Numeric] = None,
        axis_expand_count: Numeric = 0,
        axis_expand_width: Numeric = 50,
        axis_expand_trigger_on: str = "click",
    ):
        self.opts: dict = {
            "left": pos_left,
            "right": pos_right,
            "bottom": pos_bottom,
            "top": pos_top,
            "layout": layout,
            "axisExpandable": is_axis_expandable,
            "axisExpandCenter": axis_expand_center,
            "axisExpandCount": axis_expand_count,
            "axisExpandWidth": axis_expand_width,
            "axisExpandTriggerOn": axis_expand_trigger_on,
        }


class ParallelAxisOpts(BasicOpts):
    def __init__(
        self,
        dim: Numeric,
        parallel_index: Numeric = 0,
        is_realtime: bool = True,
        name: Optional[str] = None,
        data: Sequence = None,
        type_: Optional[str] = None,
        name_location: str = "end",
        name_gap: Numeric = 15,
        name_rotate: Optional[int] = None,
        is_inverse: bool = False,
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        is_scale: bool = False,
        log_base: Numeric = 10,
        is_silent: bool = False,
        is_trigger_event: bool = False,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        axistick_opts: Union[AxisTickOpts, dict, None] = None,
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        minor_tick_opts: Union[MinorTickOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "dim": dim,
            "parallelIndex": parallel_index,
            "realtime": is_realtime,
            "name": name,
            "data": data,
            "type": type_,
            "name_location": name_location,
            "name_gap": name_gap,
            "name_rotate": name_rotate,
            "inverse": is_inverse,
            "min": min_,
            "max": max_,
            "scale": is_scale,
            "logBase": log_base,
            "silent": is_silent,
            "triggerEvent": is_trigger_event,
            "axisLine": axisline_opts,
            "axisTick": axistick_opts,
            "axisLabel": axislabel_opts,
            "minorTick": minor_tick_opts,
        }


class RadarIndicatorItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        min_: Optional[Numeric] = None,
        max_: Optional[Numeric] = None,
        color: Optional[str] = None,
    ):
        self.opts: dict = {"name": name, "max": max_, "min": min_, "color": color}


class CalendarDayLabelOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        first_day: int = 0,
        margin: Optional[int] = None,
        position: str = "start",
        name_map: Union[str, Sequence] = "en",
        label_color: str = "#000",
        label_font_style: str = "normal",
        label_font_weight: str = "normal",
        label_font_family: str = "sans-serif",
        label_font_size: int = 12,
        align: Optional[str] = None,
        vertical_align: Optional[str] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "firstDay": first_day,
            "margin": margin,
            "position": position,
            "nameMap": name_map,
            "color": label_color,
            "fontStyle": label_font_style,
            "fontWeight": label_font_weight,
            "fontFamily": label_font_family,
            "fontSize": label_font_size,
            "align": align,
            "verticalAlign": vertical_align,
        }


class CalendarMonthLabelOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        align: Optional[str] = None,
        margin: Optional[int] = None,
        position: str = "start",
        name_map: Union[str, Sequence] = "en",
        formatter: JSFunc = None,
        label_color: str = "#000",
        label_font_style: str = "normal",
        label_font_weight: str = "normal",
        label_font_family: str = "sans-serif",
        label_font_size: int = 12,
        vertical_align: Optional[str] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "align": align,
            "margin": margin,
            "position": position,
            "nameMap": name_map,
            "formatter": formatter,
            "color": label_color,
            "fontStyle": label_font_style,
            "fontWeight": label_font_weight,
            "fontFamily": label_font_family,
            "fontSize": label_font_size,
            "verticalAlign": vertical_align,
        }


class CalendarYearLabelOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        margin: Optional[int] = None,
        position: Optional[str] = None,
        formatter: JSFunc = None,
        label_color: str = "#000",
        label_font_style: str = "normal",
        label_font_weight: str = "normal",
        label_font_family: str = "sans-serif",
        label_font_size: int = 12,
        align: Optional[str] = None,
        vertical_align: Optional[str] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "margin": margin,
            "position": position,
            "formatter": formatter,
            "color": label_color,
            "fontStyle": label_font_style,
            "fontWeight": label_font_weight,
            "fontFamily": label_font_family,
            "fontSize": label_font_size,
            "align": align,
            "verticalAlign": vertical_align,
        }


class CalendarOpts(BasicOpts):
    def __init__(
        self,
        z_level: Numeric = 0,
        z: Numeric = 2,
        pos_left: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        width: Optional[str] = "auto",
        height: Optional[str] = None,
        orient: Optional[str] = "horizontal",
        range_: Union[str, Sequence, int] = None,
        cell_size: Union[int, Sequence] = 20,
        splitline_opts: Union[SplitLineOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        daylabel_opts: Union[CalendarDayLabelOpts, dict, None] = None,
        monthlabel_opts: Union[CalendarMonthLabelOpts, dict, None] = None,
        yearlabel_opts: Union[CalendarYearLabelOpts, dict, None] = None,
        is_silent: bool = False,
    ):
        self.opts: dict = {
            "zlevel": z_level,
            "z": z,
            "left": pos_left,
            "top": pos_top,
            "right": pos_right,
            "bottom": pos_bottom,
            "width": width,
            "height": height,
            "orient": orient,
            "range": range_,
            "cellSize": cell_size,
            "splitLine": splitline_opts,
            "itemStyle": itemstyle_opts,
            "dayLabel": daylabel_opts,
            "monthLabel": monthlabel_opts,
            "yearLabel": yearlabel_opts,
            "silent": is_silent,
        }


class SingleAxisOpts(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        max_: Union[str, Numeric, None] = None,
        min_: Union[str, Numeric, None] = None,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        width: Optional[str] = None,
        height: Optional[str] = None,
        orient: Optional[str] = None,
        type_: Optional[str] = None,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        axistick_opts: Union[AxisTickOpts, dict, None] = None,
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        axispointer_opts: Union[AxisPointerOpts, dict, None] = None,
        splitarea_opts: Union[SplitAreaOpts, dict, None] = None,
        splitline_opts: Union[SplitLineOpts, dict, None] = None,
        minor_tick_opts: Union[MinorTickOpts, dict, None] = None,
        minor_split_line_opts: Union[MinorSplitLineOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "max": max_,
            "min": min_,
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
            "width": width,
            "height": height,
            "orient": orient,
            "type": type_,
            "axisLine": axisline_opts,
            "axisTick": axistick_opts,
            "minorTick": minor_tick_opts,
            "axisLabel": axislabel_opts,
            "splitLine": splitline_opts,
            "minorSplitLine": minor_split_line_opts,
            "splitArea": splitarea_opts,
            "axisPointer": axispointer_opts,
            "tooltip": tooltip_opts,
        }


class RadiusAxisItem(BasicOpts):
    def __init__(
        self,
        value: Optional[str] = None,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"value": value, "textStyle": textstyle_opts}


class AngleAxisItem(RadiusAxisItem):
    def __init__(
        self,
        value: Optional[str] = None,
        textstyle_opts: Optional[TextStyleOpts] = None,
    ):
        super().__init__(value, textstyle_opts)


class RadiusAxisOpts(BasicOpts):
    def __init__(
        self,
        polar_index: Optional[int] = None,
        data: Optional[Sequence[Union[RadiusAxisItem, dict, str]]] = None,
        boundary_gap: Union[bool, Sequence] = None,
        type_: Optional[str] = None,
        name: Optional[str] = None,
        name_location: Optional[str] = None,
        name_gap: Numeric = 15,
        name_rotate: Optional[Numeric] = None,
        is_inverse: bool = False,
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        is_scale: bool = False,
        split_number: Numeric = 5,
        interval: Optional[Numeric] = None,
        min_interval: Numeric = 0,
        max_interval: Optional[Numeric] = None,
        splitline_opts: Union[SplitLineOpts, dict, None] = None,
        splitarea_opts: Union[SplitAreaOpts, dict, None] = None,
        axistick_opts: Union[AxisTickOpts, dict, None] = None,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        minor_tick_opts: Union[MinorTickOpts, dict, None] = None,
        minor_split_line_opts: Union[MinorSplitLineOpts, dict, None] = None,
        z: Optional[int] = None,
        z_level: Optional[int] = None,
    ):
        _data = []
        if data:
            for d in data:
                if isinstance(d, RadiusAxisItem):
                    d = d.opts
                _data.append(d)

        self.opts: dict = {
            "polarIndex": polar_index,
            "type": type_,
            "data": data,
            "boundaryGap": boundary_gap,
            "name": name,
            "nameLocation": name_location,
            "nameGap": name_gap,
            "nameRotate": name_rotate,
            "inverse": is_inverse,
            "min": min_,
            "max": max_,
            "scale": is_scale,
            "splitNumber": split_number,
            "interval": interval,
            "minInterval": min_interval,
            "maxInterval": max_interval,
            "splitLine": splitline_opts,
            "splitArea": splitarea_opts,
            "axisTick": axistick_opts,
            "axisLine": axisline_opts,
            "axisLabel": axislabel_opts,
            "minorTick": minor_tick_opts,
            "minorSplitLine": minor_split_line_opts,
            "z": z,
            "zlevel": z_level,
        }


class AngleAxisOpts(BasicOpts):
    def __init__(
        self,
        polar_index: Optional[int] = None,
        data: Optional[Sequence[Union[AngleAxisItem, Numeric, dict, str]]] = None,
        start_angle: Optional[Numeric] = 90,
        is_clockwise: bool = False,
        boundary_gap: Union[bool, Sequence, None] = None,
        type_: Optional[str] = None,
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        is_scale: bool = False,
        split_number: Numeric = 5,
        interval: Optional[Numeric] = None,
        splitline_opts: Union[SplitLineOpts, dict, None] = None,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        axistick_opts: Union[AxisTickOpts, dict, None] = None,
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        minor_tick_opts: Union[MinorTickOpts, dict, None] = None,
        minor_split_line_opts: Union[MinorSplitLineOpts, dict, None] = None,
        z: Optional[int] = None,
        z_level: Optional[int] = None,
    ):
        _data = []
        if data:
            for d in data:
                if isinstance(d, AngleAxisItem):
                    d = d.opts
                _data.append(d)

        self.opts: dict = {
            "polarIndex": polar_index,
            "startAngle": start_angle,
            "data": data,
            "clockwise": is_clockwise,
            "boundaryGap": boundary_gap,
            "type": type_,
            "min": min_,
            "max": max_,
            "scale": is_scale,
            "splitNumber": split_number,
            "interval": interval,
            "splitLine": splitline_opts,
            "axisLine": axisline_opts,
            "axisTick": axistick_opts,
            "axisLabel": axislabel_opts,
            "minorTick": minor_tick_opts,
            "minorSplitLine": minor_split_line_opts,
            "z": z,
            "zlevel": z_level,
        }


class PolarOpts(BasicOpts):
    def __init__(
        self,
        center: Optional[Sequence] = None,
        radius: Optional[Union[Sequence, str]] = None,
        tooltip_opts: TooltipOpts = None,
    ):
        self.opts: dict = {"center": center, "radius": radius, "tooltip": tooltip_opts}


class DatasetTransformOpts(BasicOpts):
    def __init__(
        self,
        type_: str = "filter",
        config: Optional[dict] = None,
        is_print: bool = False,
    ):
        self.opts: dict = {"type": type_, "config": config, "print": is_print}


class EmphasisOpts(BasicOpts):
    def __init__(
        self,
        is_disabled: bool = False,
        is_scale: bool = True,
        focus: str = "none",
        blur_scope: str = "coordinateSystem",
        label_opts: Union[LabelOpts, dict, None] = None,
        is_show_label_line: bool = False,
        label_linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        areastyle_opts: Union[AreaStyleOpts, dict, None] = None,
        end_label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "disabled": is_disabled,
            "scale": is_scale,
            "focus": focus,
            "blurScope": blur_scope,
            "label": label_opts,
            "labelLine": {
                "show": is_show_label_line,
                "lineStyle": label_linestyle_opts
            },
            "itemStyle": itemstyle_opts,
            "lineStyle": linestyle_opts,
            "areaStyle": areastyle_opts,
            "endLabel": end_label_opts,
        }


class Emphasis3DOpts(BasicOpts):
    def __init__(
        self,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "itemStyle": itemstyle_opts,
            "label": label_opts,
        }


class BlurOpts(BasicOpts):
    def __init__(
        self,
        label_opts: Union[LabelOpts, dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        is_show_label_line: bool = False,
        label_linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "label": label_opts,
            "lineStyle": linestyle_opts,
            "labelLine": {
                "show": is_show_label_line,
                "lineStyle": label_linestyle_opts
            },
            "itemStyle": itemstyle_opts,
        }


class SelectOpts(BasicOpts):
    def __init__(
            self,
            is_disabled: Optional[bool] = None,
            itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
            linestyle_opts: Union[LineStyleOpts, dict, None] = None,
            label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "disabled": is_disabled,
            "itemStyle": itemstyle_opts,
            "lineStyle": linestyle_opts,
            "label": label_opts,
        }


class TreeLeavesOpts(BasicOpts):
    def __init__(
        self,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        emphasis_opts: Union[EmphasisOpts, dict, None] = None,
        blur_opts: Union[BlurOpts, dict, None] = None,
        select_opts: Union[SelectOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "emphasis": emphasis_opts,
            "blur": blur_opts,
            "select": select_opts,
        }
