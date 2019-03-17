# coding=utf-8

from ..types import Optional, Union, List, Numeric


class LabelOpts:
    def __init__(
        self,
        is_show: bool = True,
        position: Optional[str] = None,
        text_color: Optional[str] = None,
        text_size: Numeric = 12,
        formatter=None,
    ):
        self.opts: dict = {
            "show": is_show,
            "position": position,
            "text_color": text_color,
            "text_size": text_size,
            "formatter": formatter,
        }

        # 特殊的 hack 实现应该放到具体的文件中
        # if chart_type != "graph":
        #     if formatter is None:
        #         if chart_type == "pie":
        #             formatter = "{b}: {d}%"

        # position = "outside" if chart_type in ["pie", "graph"] else "top"


class LineStyleOpts:
    def __init__(
        self,
        width: Numeric = 1,
        opacity: Numeric = 1,
        curve: Numeric = 0,
        type_: str = "solid",
        color: Optional[str] = None,
    ):

        # if line_color is None and type == "graph":
        #     line_color = "#aaa"

        self.opts: dict = {
            "width": width,
            "opacity": opacity,
            "curve": curve,
            "type": type_,
            "color": color,
        }


class SplitLineOpts:
    def __init__(
        self, is_show: bool = False, linestyle_opts: LineStyleOpts = LineStyleOpts()
    ):
        self.opts: dict = {"show": is_show, "lineStyle": linestyle_opts.opts}


class AxisLineOpts:
    def __init__(
        self, is_show: bool = True, line_style: LineStyleOpts = LineStyleOpts()
    ):
        self.opts: dict = {"show": is_show, "lineStyle": line_style}


class MarkPointData:
    def __init__(
        self,
        name: Optional[str] = None,
        type_: Optional[str] = None,
        value_index: Optional[Numeric] = None,
        value_dim: Optional[str] = None,
        coord: Optional[List] = None,
        x: Optional[Numeric] = None,
        y: Optional[Numeric] = None,
        value: Optional[Numeric] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, List] = None,
    ):
        self.opts: dict = {
            "name": name,
            "type": type_,
            "valueIndex": value_index,
            "valueDim": value_dim,
            "coord": coord,
            "x": x,
            "y": y,
            "value": value,
            "symbol": symbol,
            "symbol_size": symbol_size,
        }


class MarkPointOpts:
    def __init__(
        self,
        data: List[MarkPointData] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[None, Numeric] = None,
        label: LabelOpts = LabelOpts(),
    ):
        if data:
            data = [d.opts for d in data]
        self.opts: dict = {
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label.opts,
            "data": data,
        }


class MarkLineOpts:
    def __init__(self):
        self.opts: dict = {}


class EffectOpts:
    def __init__(
        self, brush_type: str = "stroke", scale: Numeric = 2.5, period: Numeric = 4
    ):
        self.opts: dict = {"brushType": brush_type, "scale": scale, "period": period}


class AreaStyleOpts:
    def __init__(self, opacity: Optional[Numeric] = 0, color: Optional[str] = None):
        self.opts: dict = {"opacity": opacity, "color": color}


class SplitAreaOpt:
    def __init__(self, is_show=True, area_style: AreaStyleOpts = AreaStyleOpts()):
        self.opts: dict = {"show": is_show, "areaStyle": area_style}


# def symbol(type=None, symbol="", **kwargs):
#     """
#
#     :param symbol:
#         标记类型, 有'rect', 'roundRect', 'triangle', 'diamond',
#          'pin', 'arrow'可选
#     :param kwargs:
#     """
#     if symbol is None:  # Radar
#         symbol = "none"
#     elif type == "line" and symbol == "":  # Line
#         symbol = "emptyCircle"
#     elif symbol not in SYMBOLS:
#         symbol = "circle"
#     return symbol


# import random
#
# SYMBOLS = ("rect", "roundRect", "triangle", "diamond", "pin", "arrow")
#
#
# def color(colorlst=None, is_random=False, label_color=None, **kwargs):
#     if colorlst is None:
#         colorlst = []
#     if label_color:
#         for color in reversed(list(label_color)):
#             colorlst.insert(0, color)
#     if is_random:
#         random.shuffle(colorlst)
#     return colorlst
#
#
# def grid(
#     grid_width=None,
#     grid_height=None,
#     grid_top=None,
#     grid_bottom=None,
#     grid_left=None,
#     grid_right=None,
# ):
#     _grid = {}
#     if grid_width is not None:
#         _grid.update(width=grid_width)
#     if grid_height is not None:
#         _grid.update(height=grid_height)
#     if grid_top is not None:
#         _grid.update(top=grid_top)
#     if grid_bottom is not None:
#         _grid.update(bottom=grid_bottom)
#     if grid_left is not None:
#         _grid.update(left=grid_left)
#     if grid_right is not None:
#         _grid.update(right=grid_right)
#     return _grid
#
#
# def calendar(calendar_date_range=None, calendar_cell_size=None, **kwargs):
#     if calendar_cell_size is None:
#         calendar_cell_size = ["auto", 20]
#
#     _calendar = {"range": calendar_date_range, "cellSize": calendar_cell_size}
#     return _calendar
