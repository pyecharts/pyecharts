from ..globals import CurrentConfig, RenderType, ThemeType
from ..options.series_options import (
    BasicOpts,
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


class AnimationOpts(BasicOpts):
    def __init__(
        self,
        animation: bool = True,
        animation_threshold: Numeric = 2000,
        animation_duration: Union[Numeric, JSFunc] = 1000,
        animation_easing: Union[str] = "cubicOut",
        animation_delay: Union[Numeric, JSFunc] = 0,
        animation_duration_update: Union[Numeric, JSFunc] = 300,
        animation_easing_update: Union[Numeric] = "cubicOut",
        animation_delay_update: Union[Numeric, JSFunc] = 0,
    ):
        self.opts: dict = {
            "animation": animation,
            "animationThreshold": animation_threshold,
            "animationDuration": animation_duration,
            "animationEasing": animation_easing,
            "animationDelay": animation_delay,
            "animationDurationUpdate": animation_duration_update,
            "animationEasingUpdate": animation_easing_update,
            "animationDelayUpdate": animation_delay_update,
        }


class InitOpts(BasicOpts):
    def __init__(
        self,
        width: str = "900px",
        height: str = "500px",
        chart_id: Optional[str] = None,
        renderer: str = RenderType.CANVAS,
        page_title: str = CurrentConfig.PAGE_TITLE,
        theme: str = ThemeType.WHITE,
        bg_color: Union[str, dict] = None,
        js_host: str = "",
        animation_opts: Union[AnimationOpts, dict] = AnimationOpts(),
    ):
        self.opts: dict = {
            "width": width,
            "height": height,
            "chart_id": chart_id,
            "renderer": renderer,
            "page_title": page_title,
            "theme": theme,
            "bg_color": bg_color,
            "js_host": js_host,
            "animationOpts": animation_opts,
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
        xaxis_index: Union[Numeric, Sequence, bool] = False,
        yaxis_index: Union[Numeric, Sequence, bool] = False,
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
        brush: Union[ToolBoxFeatureBrushOpts, dict] = ToolBoxFeatureBrushOpts(),
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
        out_of_brush: dict = None,
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
            "outOfBrush": out_of_brush,
        }


class TitleOpts(BasicOpts):
    def __init__(
        self,
        title: Optional[str] = None,
        title_link: Optional[str] = None,
        title_target: Optional[str] = None,
        subtitle: Optional[str] = None,
        subtitle_link: Optional[str] = None,
        subtitle_target: Optional[str] = None,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        padding: Union[Sequence, Numeric] = 5,
        item_gap: Numeric = 10,
        title_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        subtitle_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        self.opts: Sequence = [
            {
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
                "textStyle": title_textstyle_opts,
                "subtextStyle": subtitle_textstyle_opts,
            }
        ]


class DataZoomOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        type_: str = "slider",
        is_realtime: bool = True,
        range_start: Union[Numeric, None] = 20,
        range_end: Union[Numeric, None] = 80,
        start_value: Union[int, str, None] = None,
        end_value: Union[int, str, None] = None,
        orient: str = "horizontal",
        xaxis_index: Union[int, Sequence[int], None] = None,
        yaxis_index: Union[int, Sequence[int], None] = None,
        is_zoom_lock: bool = False,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        filter_mode: str = "filter",
    ):
        self.opts: dict = {
            "show": is_show,
            "type": type_,
            "realtime": is_realtime,
            "startValue": start_value,
            "endValue": end_value,
            "start": range_start,
            "end": range_end,
            "orient": orient,
            "xAxisIndex": xaxis_index,
            "yAxisIndex": yaxis_index,
            "zoomLock": is_zoom_lock,
            "left": pos_left,
            "right": pos_right,
            "top": pos_top,
            "bottom": pos_bottom,
            "filterMode": filter_mode,
        }


class LegendOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        selected_mode: Union[str, bool, None] = None,
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
    ):
        self.opts: dict = {
            "type": type_,
            "selectedMode": selected_mode,
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
        }


class VisualMapOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        type_: str = "color",
        min_: Numeric = 0,
        max_: Numeric = 100,
        range_text: Optional[Sequence] = None,
        range_color: Optional[Sequence[str]] = None,
        range_size: Optional[Sequence[int]] = None,
        range_opacity: Optional[Numeric] = None,
        orient: str = "vertical",
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        split_number: int = 5,
        series_index: Union[Numeric, Sequence, None] = None,
        dimension: Optional[Numeric] = None,
        is_calculable: bool = True,
        is_piecewise: bool = False,
        is_inverse: bool = False,
        precision: Optional[int] = None,
        pieces: Optional[Sequence] = None,
        out_of_range: Optional[Sequence] = None,
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
            "inRange": _inrange_op,
            "calculable": is_calculable,
            "inverse": is_inverse,
            "precision": precision,
            "splitNumber": split_number,
            "dimension": dimension,
            "seriesIndex": series_index,
            "orient": orient,
            "left": pos_left,
            "top": pos_top,
            "bottom": pos_bottom,
            "right": pos_right,
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
        position: Union[str, Sequence, JSFunc] = None,
        formatter: Optional[JSFunc] = None,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Numeric = 0,
        padding: Numeric = 5,
        textstyle_opts: TextStyleOpts = TextStyleOpts(font_size=14),
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
            "position": position,
            "formatter": formatter,
            "textStyle": textstyle_opts,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "padding": padding,
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
        label: Union[LabelOpts, dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "type": type_,
            "link": link,
            "label": label,
            "lineStyle": linestyle_opts,
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
        splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(),
        minor_tick_opts: Union[MinorTickOpts, dict, None] = None,
        minor_split_line_opts: Union[MinorSplitLineOpts, dict, None] = None,
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
            "tooltip": tooltip_opts,
        }


class Grid3DOpts(BasicOpts):
    def __init__(
        self,
        width: Numeric = 200,
        height: Numeric = 100,
        depth: Numeric = 80,
        is_rotate: bool = False,
        rotate_speed: Numeric = 10,
        rotate_sensitivity: Numeric = 1,
    ):
        self.opts: dict = {
            "boxWidth": width,
            "boxHeight": height,
            "boxDepth": depth,
            "viewControl": {
                "autoRotate": is_rotate,
                "autoRotateSpeed": rotate_speed,
                "rotateSensitivity": rotate_sensitivity,
            },
        }


class Axis3DOpts(BasicOpts):
    def __init__(
        self,
        data: Optional[Sequence] = None,
        type_: Optional[str] = None,
        name: Optional[str] = None,
        name_gap: Numeric = 20,
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        splitnum: Optional[Numeric] = None,
        interval: Optional[Numeric] = None,
        margin: Numeric = 8,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "data": data,
            "name": name,
            "nameGap": name_gap,
            "nameTextStyle": textstyle_opts,
            "splitNum": splitnum,
            "type": type_,
            "min": min_,
            "max": max_,
            "axisLabel": {"margin": margin, "interval": interval},
        }


class ParallelOpts(BasicOpts):
    def __init__(
        self,
        pos_left: str = "5%",
        pos_right: str = "13%",
        pos_bottom: str = "10%",
        pos_top: str = "20%",
        layout: Optional[str] = None,
    ):
        self.opts: dict = {
            "left": pos_left,
            "right": pos_right,
            "bottom": pos_bottom,
            "top": pos_top,
            "layout": layout,
        }


class ParallelAxisOpts(BasicOpts):
    def __init__(
        self,
        dim: Numeric,
        name: str,
        data: Sequence = None,
        type_: Optional[str] = None,
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        is_scale: bool = False,
    ):
        self.opts: dict = {
            "dim": dim,
            "name": name,
            "data": data,
            "type": type_,
            "min": min_,
            "max": max_,
            "scale": is_scale,
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
    ):
        self.opts: dict = {
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
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        is_scale: bool = False,
        interval: Optional[Numeric] = None,
        splitline_opts: Union[SplitLineOpts, dict, None] = None,
        splitarea_opts: Union[SplitAreaOpts, dict, None] = None,
        axistick_opts: Union[AxisTickOpts, dict, None] = None,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        axislabel_opts: Union[LabelOpts, dict, None] = None,
        z: Optional[int] = None,
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
            "min": min_,
            "max": max_,
            "scale": is_scale,
            "interval": interval,
            "splitLine": splitline_opts,
            "splitArea": splitarea_opts,
            "axisTick": axistick_opts,
            "axisLine": axisline_opts,
            "axisLabel": axislabel_opts,
            "z": z,
        }


class AngleAxisOpts(BasicOpts):
    def __init__(
        self,
        polar_index: Optional[int] = None,
        data: Optional[Sequence[Union[AngleAxisItem, Numeric, dict, str]]] = None,
        start_angle: Optional[Numeric] = None,
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
        z: Optional[int] = None,
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
            "z": z,
        }


class PolarOpts(BasicOpts):
    def __init__(
        self,
        center: Optional[Sequence] = None,
        radius: Optional[Union[Sequence, str]] = None,
        tooltip_opts: TooltipOpts = None,
    ):
        self.opts: dict = {"center": center, "radius": radius, "tooltip": tooltip_opts}
