# coding=utf-8

from pyecharts.commons.types import *
from pyecharts.commons.consts import *
from pyecharts.options.series_options import *


class InitOpts:
    def __init__(
        self,
        width: str = "800px",
        height: str = "400px",
        renderer: str = RENDER_TYPE.canvas,
        page_title: str = PAGE_TITLE,
        theme: str = "white",
        bg_color: Optional[str] = None,
        js_host: str = "",
    ):
        self.width = width
        self.height = height
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
        title_left: Optional[str] = None,
        title_top: Optional[str] = None,
        title_color: Optional[str] = None,
        title_text_size: Union[None, Numeric] = None,
        subtitle_color: Optional[str] = None,
        subtitle_text_size: Union[None, Numeric] = None,
    ):
        self.opts: List = [
            {
                "text": title,
                "subtext": subtitle,
                "left": title_left,
                "top": title_top,
                "textStyle": {"color": title_color, "fontSize": title_text_size},
                "subtextStyle": {
                    "color": subtitle_color,
                    "fontSize": subtitle_text_size,
                },
            }
        ]


class DataZoomOpts:
    def __init__(
        self,
        is_show: bool = False,
        type: str = "slider",
        range_start: Numeric = 50,
        range_end: Numeric = 100,
        orient: str = "horizontal",
        xaxis_index: int = 0,
        yaxis_index: int = 0,
    ):
        self.opts: dict = {
            "show": is_show,
            "type": type,
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
        text_size: Union[None, Numeric] = None,
        text_color: Optional[str] = None,
    ):
        self.opts: dict = {
            "selectedMode": selected_mode,
            "show": is_show,
            "left": left,
            "top": top,
            "orient": orient,
            "textStyle": {"fontSize": text_size, "color": text_color},
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
        text_color: Optional[str] = None,
        orient: str = "vertical",
        pos_left: str = "left",
        pos_top: str = "bottom",
        split_number: int = 5,
        dimension=None,
        is_calculable: bool = True,
        is_piecewise: bool = False,
        pieces=None,
    ):

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
            "textStyle": {"color": text_color},
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
        text_color: Optional[str] = None,
        text_size: Numeric = 14,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Numeric = 0,
    ):
        self.opts: dict = {
            "trigger": trigger,
            "triggerOn": trigger_on,
            "axisPointer": {"type": axis_pointer_type},
            "formatter": formatter,
            "textStyle": {"color": text_color, "fontSize": text_size},
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
        }


class AxisOpts:
    def __init__(
        self,
        name: Optional[str] = None,
        visibility: bool = True,
        name_location: str = "end",
        name_gap: Numeric = 15,
        name_size: Numeric = 12,
        position: Optional[str] = None,
        boundary_gap: Optional[str] = None,
        label_alignment: Optional[str] = None,
        inverse: Optional[str] = None,
        is_split_line: bool = True,
        min_: Union[None, Numeric] = None,
        max_: Union[None, Numeric] = None,
        type_: str = "value",
        line_style: LineStyleOpts = LineStyleOpts(),
    ):
        self.opts: dict = {
            "name": name,
            "show": visibility,
            "nameLocation": name_location,
            "nameGap": name_gap,
            "nameTextStyle": {"fontSize": name_size},
            "axisTick": {"alignWithLabel": label_alignment},
            "inverse": inverse,
            "position": position,
            "boundaryGap": boundary_gap,
            "min": min_,
            "max": max_,
            "type": type_,
            "splitLine": {"show": is_split_line},
            "axisLine": {"lineStyle": line_style.opts},
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
