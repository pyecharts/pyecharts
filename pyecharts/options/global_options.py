from ..globals import CurrentConfig, RenderType, ThemeType
from ..options.series_options import (
    BasicOpts,
    JSFunc,
    LabelOpts,
    LineStyleOpts,
    Numeric,
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


class ToolBoxFeatureOpts(BasicOpts):
    def __init__(
        self,
        save_as_image: Optional[dict] = None,
        restore: Optional[dict] = None,
        data_view: Optional[dict] = None,
        data_zoom: Optional[dict] = None,
    ):
        if not save_as_image:
            save_as_image = {"show": True, "title": "save as image", "type": "png"}
        if not restore:
            restore = {"show": True, "title": "restore"}
        if not data_view:
            data_view = {"show": True, "title": "data view", "readOnly": False}
        if not data_zoom:
            data_zoom = {
                "show": True,
                "title": {"zoom": "data zoom", "back": "data zoom restore"},
            }

        self.opts: dict = {
            "saveAsImage": save_as_image,
            "restore": restore,
            "dataView": data_view,
            "dataZoom": data_zoom,
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
        range_start: Numeric = 20,
        range_end: Numeric = 80,
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
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
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
            "textStyle": textstyle_opts,
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
        pieces: Optional[Sequence] = None,
        out_of_range: Optional[Sequence] = None,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        _inrange_op: dict = {}
        if type_ == "color":
            range_color = range_color or ["#50a3ba", "#eac763", "#d94e5d"]
            _inrange_op.update(color=range_color)
        elif type_ == "size":
            range_size = range_size or [20, 50]
            _inrange_op.update(symbolSize=range_size)

        _visual_typ = "piecewise" if is_piecewise else "continuous"

        self.opts: dict = {
            "show": is_show,
            "type": _visual_typ,
            "min": min_,
            "max": max_,
            "text": range_text,
            "textStyle": textstyle_opts,
            "inRange": _inrange_op,
            "calculable": is_calculable,
            "splitNumber": split_number,
            "dimension": dimension,
            "seriesIndex": series_index,
            "orient": orient,
            "left": pos_left,
            "top": pos_top,
            "bottom": pos_bottom,
            "right": pos_right,
            "showLabel": True,
            "outOfRange": out_of_range,
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
        formatter: Optional[JSFunc] = None,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Numeric = 0,
        textstyle_opts: TextStyleOpts = TextStyleOpts(font_size=14),
    ):
        self.opts: dict = {
            "show": is_show,
            "trigger": trigger,
            "triggerOn": trigger_on,
            "axisPointer": {"type": axis_pointer_type},
            "formatter": formatter,
            "textStyle": textstyle_opts,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
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
        }


class GridOpts(BasicOpts):
    def __init__(
        self,
        pos_left: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        width: Union[Numeric, str, None] = None,
        height: Union[Numeric, str, None] = None,
    ):
        self.opts: dict = {
            "left": pos_left,
            "top": pos_top,
            "right": pos_right,
            "bottom": pos_bottom,
            "width": width,
            "height": height,
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


class CalendarOpts(BasicOpts):
    def __init__(
        self,
        pos_left: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        orient: Optional[str] = None,
        range_: Union[str, Sequence, int] = None,
        daylabel_opts: Union[LabelOpts, dict, None] = None,
        monthlabel_opts: Union[LabelOpts, dict, None] = None,
        yearlabel_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "left": pos_left,
            "top": pos_top,
            "right": pos_right,
            "bottom": pos_bottom,
            "orient": orient,
            "range": range_,
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
        splitline_opts: Union[SplitLineOpts, dict, None] = None,
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
            "splitLine": splitline_opts,
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
            "splitLine": splitline_opts,
            "axisLine": axisline_opts,
            "axisTick": axistick_opts,
            "axisLabel": axislabel_opts,
            "z": z,
        }
