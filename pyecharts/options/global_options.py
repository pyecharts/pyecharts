# coding=utf-8
import uuid

from ..consts import *
from ..options.series_options import *


class InitOpts:
    def __init__(
        self,
        width: str = "800px",
        height: str = "400px",
        chart_id: str = uuid.uuid4().hex,
        renderer: str = RENDER_TYPE.CANVAS,
        page_title: str = "Awesome-pyecharts",
        theme: str = "white",
        bg_color: Optional[str] = None,
        js_host: str = "",
    ):
        self.width = width
        self.height = height
        self.chart_id = chart_id
        self.renderer = renderer
        self.page_title = page_title
        self.theme = theme
        self.bg_color = bg_color
        self.js_host = js_host


class ToolboxOpst:
    def __init__(
        self,
        is_show: bool = True,
        orient: Optional[str] = None,
        pos_left: str = "95%",
        pos_top: Optional[str] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "orient": orient,
            "left": pos_left,
            "top": pos_top,
            "feature": {
                "saveAsImage": {"show": True, "title": "save as image"},
                "restore": {"show": True, "title": "restore"},
                "dataView": {"show": True, "title": "data view"},
            },
        }


class TitleOpts:
    def __init__(
        self,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        pos_left: Optional[str] = None,
        pos_right: Optional[str] = None,
        pos_top: Optional[str] = None,
        pos_bottom: Optional[str] = None,
        title_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        subtitle_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        if isinstance(title_textstyle_opts, TextStyleOpts):
            title_textstyle_opts = title_textstyle_opts.opts
        if isinstance(subtitle_textstyle_opts, TextStyleOpts):
            subtitle_textstyle_opts = subtitle_textstyle_opts.opts

        self.opts: List = [
            {
                "text": title,
                "subtext": subtitle,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "textStyle": title_textstyle_opts,
                "subtextStyle": subtitle_textstyle_opts,
            }
        ]


class DataZoomOpts:
    def __init__(
        self,
        is_show: bool = True,
        type_: str = "slider",
        range_start: Numeric = 40,
        range_end: Numeric = 80,
        orient: str = "horizontal",
        xaxis_index: int = 0,
        yaxis_index: int = 0,
    ):
        self.opts: dict = {
            "show": is_show,
            "type": type_,
            "start": range_start,
            "end": range_end,
            "orient": orient,
            "xAxisIndex": xaxis_index,
            "yAxisIndex": yaxis_index,
        }


class LegendOpts:
    def __init__(
        self,
        selected_mode: Optional[str] = None,
        is_show: bool = True,
        left: Optional[str] = None,
        top: Optional[str] = None,
        orient: Optional[str] = None,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        if isinstance(textstyle_opts, TextStyleOpts):
            textstyle_opts = textstyle_opts.opts

        self.opts: dict = {
            "selectedMode": selected_mode,
            "show": is_show,
            "left": left,
            "top": top,
            "orient": orient,
            "textStyle": textstyle_opts,
        }


class VisualMapOpts:
    def __init__(
        self,
        type_: str = "color",
        min_: Union[int, float] = 0,
        max_: Union[int, float] = 100,
        range_text: Union[list, tuple] = None,
        range_color: Union[List[str]] = None,
        range_size: Union[List[int]] = None,
        orient: str = "vertical",
        pos_left: str = "left",
        pos_top: str = "bottom",
        split_number: int = 5,
        dimension=None,
        is_calculable: bool = True,
        is_piecewise: bool = False,
        pieces=None,
        textstyle_opts: Union[TextStyleOpts, dict, None] = None,
    ):
        if isinstance(textstyle_opts, TextStyleOpts):
            textstyle_opts = textstyle_opts.opts
        _inrange_op = {}
        if type_ == "color":
            range_color = range_color or ["#50a3ba", "#eac763", "#d94e5d"]
            _inrange_op.update(color=range_color)
        elif type_ == "size":
            range_size = range_size or [20, 50]
            _inrange_op.update(symbolSize=range_size)

        _visual_typ = "piecewise" if is_piecewise else "continuous"

        self.ops: dict = {
            "type": _visual_typ,
            "min": min_,
            "max": max_,
            "text": range_text,
            "textStyle": textstyle_opts,
            "inRange": _inrange_op,
            "calculable": is_calculable,
            "splitNumber": split_number,
            "dimension": dimension,
            "orient": orient,
            "left": pos_left,
            "top": pos_top,
            "showLabel": True,
        }
        if is_piecewise:
            self.ops.update(pieces=pieces)


class TooltipOpts:
    def __init__(
        self,
        trigger: str = "item",
        trigger_on: str = "mousemove|click",
        axis_pointer_type: str = "line",
        formatter: Optional[str] = None,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Numeric = 0,
        textstyle_opts: TextStyleOpts = TextStyleOpts(font_size=14),
    ):
        if isinstance(textstyle_opts, TextStyleOpts):
            textstyle_opts = textstyle_opts.opts

        self.opts: dict = {
            "trigger": trigger,
            "triggerOn": trigger_on,
            "axisPointer": {"type": axis_pointer_type},
            "formatter": formatter,
            "textStyle": textstyle_opts,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
        }


class AxisOpts:
    def __init__(
        self,
        name: Optional[str] = None,
        is_show: bool = True,
        is_scale: bool = False,
        name_location: str = "end",
        name_gap: Numeric = 15,
        grid_index: Numeric = 0,
        position: Optional[str] = None,
        boundary_gap: Optional[str] = None,
        label_alignment: Optional[str] = None,
        inverse: Optional[str] = None,
        min_: Union[None, Numeric] = None,
        max_: Union[None, Numeric] = None,
        type_: Optional[str] = None,
        name_textstyle_opts: Union[TextStyleOpts, dict, None] = None,
        splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(),
        linestyle_opts: Union[LineStyleOpts, dict] = LineStyleOpts(),
    ):
        if isinstance(name_textstyle_opts, TextStyleOpts):
            name_textstyle_opts = name_textstyle_opts.opts
        if isinstance(splitline_opts, SplitLineOpts):
            splitline_opts = splitline_opts.opts
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts

        self.opts: dict = {
            "name": name,
            "show": is_show,
            "scale": is_scale,
            "nameLocation": name_location,
            "nameGap": name_gap,
            "nameTextStyle": name_textstyle_opts,
            "gridIndex": grid_index,
            "axisTick": {"alignWithLabel": label_alignment},
            "inverse": inverse,
            "position": position,
            "boundaryGap": boundary_gap,
            "min": min_,
            "max": max_,
            "type": type_,
            "splitLine": splitline_opts,
            "axisLine": {"lineStyle": linestyle_opts},
        }

        # if is_convert:
        #     xaxis_type, yaxis_type = _yAxis["type"], _xAxis["type"]
        #     _xAxis["type"] = xaxis_type
        #     _yAxis.update(data=x_axis, type=yaxis_type)
        # else:
        #     _xAxis["data"] = x_axis
        #
        # # 强制分割数值轴，在多 x、y 轴中可以使用强制分割使标刻线对齐
        # if xaxis_force_interval is not None:
        #     _xAxis["interval"] = xaxis_force_interval
        # if yaxis_force_interval is not None:
        #     _yAxis["interval"] = yaxis_force_interval


class GridOpts:
    def __init__(
        self,
        left: Optional[str] = None,
        top: Optional[str] = None,
        right: Optional[str] = None,
        bottom: Optional[str] = None,
        width: Optional[Numeric] = None,
        height: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "left": left,
            "top": top,
            "right": right,
            "bottom": bottom,
            "width": width,
            "height": height,
        }


class Grid3DOpts:
    def __init__(
        self,
        width: Numeric = 100,
        height: Numeric = 100,
        depth: Numeric = 100,
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


class Axis3DOpts:
    def __init__(
        self,
        type_: Optional[str] = None,
        name: str = "",
        name_size: Numeric = 16,
        name_gap: Numeric = 20,
        min_=None,
        max_=None,
        interval: Optional[str] = None,
        margin: Numeric = 8,
    ):
        self.opts: dict = {
            "name": name,
            "nameGap": name_gap,
            "nameTextStyle": {"fontSize": name_size},
            "type": type_,
            "min": min_,
            "max": max_,
            "axisLabel": {"margin": margin, "interval": interval},
        }


class ParallelOpts:
    def __init__(
        self,
        left: str = "5%",
        right: str = "13%",
        bottom: str = "10%",
        top: str = "20%",
        layout: Optional[str] = None,
    ):
        self.opts: dict = {
            "left": left,
            "right": right,
            "bottom": bottom,
            "top": top,
            "layout": layout,
        }


class ParallelAxisOpts:
    def __init__(
        self,
        dim: Numeric,
        name: str,
        type_: Optional[str] = None,
        min_: Union[str, Numeric, None] = None,
        max_: Union[str, Numeric, None] = None,
        is_scale: bool = False,
    ):
        self.opts: dict = {
            "dim": dim,
            "name": name,
            "type": type_,
            "min": min_,
            "max": max_,
            "scale": is_scale,
        }
