from typing import Optional, Union


class TitleOpts:
    def __init__(
        self,
        title: str,
        subtitle: str = "",
        title_left: str = "auto",
        title_top: str = "auto",
        title_color: Optional[str] = None,
        title_text_size: Optional[int, float] = None,
        subtitle_color: Optional[str] = None,
        subtitle_text_size: Optional[int, float] = None,
    ):
        self.opts = (
            [
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
            ],
        )


class DataZoomOpts:
    def __init__(
        self,
        is_show: bool = False,
        type: str = "slider",
        range_start: Union[int, float] = 50,
        range_end: Union[int, float] = 100,
        orient: str = "horizontal",
        xaxis_index: int = 0,
        yaxis_index: int = 0,
    ):
        self.opts = {
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
        selected_mode: str,
        is_show: bool = True,
        left: Optional[str] = None,
        top: Optional[str] = None,
        orient: Optional[str] = None,
        text_size: Optional[float, int] = None,
        text_color: Optional[str] = None,
    ):
        self.opts = {
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
        type: str = "color",
        range_min: Union[int, float] = 0,
        range_max: Union[int, float] = 100,
        text_color: Optional[str] = None,
        range_text: Union[list, tuple] = None,
        range_color=None,
        range_size=None,
        orient="vertical",
        visual_pos="left",
        visual_top="bottom",
        visual_split_number=5,
        visual_dimension=None,
        is_calculable=True,
        is_piecewise=False,
        pieces=None,
    ):

        _inrange_op = {}
        if type == "color":
            range_color = ["#50a3ba", "#eac763", "#d94e5d"]
            if range_color and len(range_color) >= 2:
                range_color = range_color
            _inrange_op.update(color=range_color)

        if type == "size":
            range_size = [20, 50]
            if range_size:
                if len(range_size) >= 2:
                    range_size = range_size
            _inrange_op.update(symbolSize=range_size)

        _type = "piecewise" if is_piecewise else "continuous"

        self.ops = {
            "type": _type,
            "min": range_min,
            "max": range_max,
            "text": range_text,
            "textStyle": {"color": text_color},
            "inRange": _inrange_op,
            "calculable": is_calculable,
            "splitNumber": visual_split_number,
            "dimension": visual_dimension,
            "orient": orient,
            "left": visual_pos,
            "top": visual_top,
            "showLabel": True,
        }
        if is_piecewise:
            self.ops.update(pieces=pieces)
