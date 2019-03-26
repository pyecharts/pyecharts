# coding=utf-8
from ..commons.types import List, Numeric, Optional, Sequence, Union


class LabelOpts:
    def __init__(
        self,
        is_show: bool = True,
        position: Union[str, Sequence] = "top",
        color: Optional[str] = None,
        font_size: Numeric = 12,
        font_style: Optional[str] = None,
        font_weight: Optional[str] = None,
        font_family: Optional[str] = None,
        align: Optional[str] = None,
        formatter: Optional[str] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "position": position,
            "color": color,
            "fontSize": font_size,
            "fontStyle": font_style,
            "fontWeight": font_weight,
            "fontFamily": font_family,
            "align": align,
            "formatter": formatter,
        }

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
            "curveness": curve,
            "type": type_,
            "color": color,
        }


class SplitLineOpts:
    def __init__(
        self, is_show: bool = False, linestyle_opts: LineStyleOpts = LineStyleOpts()
    ):
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts

        self.opts: dict = {"show": is_show, "lineStyle": linestyle_opts}


class AxisLineOpts:
    def __init__(
        self, is_show: bool = True, linestyle_opts: LineStyleOpts = LineStyleOpts()
    ):
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts

        self.opts: dict = {"show": is_show, "lineStyle": linestyle_opts}


class MarkPointItem:
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
        data: List[Union[MarkPointItem, dict]] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[None, Numeric] = None,
        label_opts: LabelOpts = LabelOpts(position="inside", color="#fff"),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        _data = []
        if data:
            for d in data:
                if isinstance(d, dict):
                    _data.append(d)
                else:
                    _data.append(d.opts)

        self.opts: dict = {
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
            "data": _data,
        }


class MarkLineItem:
    def __init__(
        self,
        name: Optional[str] = None,
        type_: Optional[str] = None,
        xaxis: Union[str, Numeric, None] = None,
        yaxis: Union[str, Numeric, None] = None,
        coord: Optional[Sequence] = None,
        symbol: Optional[str] = None,
        symbol_size: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "name": name,
            "type": type_,
            "xAxis": xaxis,
            "yAxis": yaxis,
            "coord": coord,
            "symbol": symbol,
            "symbolSize": symbol_size,
        }


class MarkLineOpts:
    def __init__(
        self,
        data: List[Union[MarkLineItem, dict]] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[None, Numeric] = None,
        label_opts: LabelOpts = LabelOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        _data = []
        if data:
            for d in data:
                if isinstance(d, dict):
                    _data.append(d)
                else:
                    _data.append(d.opts)

        self.opts: dict = {
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
            "data": _data,
        }


# TODO
class MarkAreaOpts:
    pass


# TODO
class MarkAreaItem:
    pass


class EffectOpts:
    def __init__(
        self, brush_type: str = "stroke", scale: Numeric = 2.5, period: Numeric = 4
    ):
        self.opts: dict = {"brushType": brush_type, "scale": scale, "period": period}


class AreaStyleOpts:
    def __init__(self, opacity: Optional[Numeric] = 0, color: Optional[str] = None):
        self.opts: dict = {"opacity": opacity, "color": color}


class SplitAreaOpts:
    def __init__(self, is_show=True, areastyle_opts: AreaStyleOpts = AreaStyleOpts()):
        if isinstance(areastyle_opts, AreaStyleOpts):
            areastyle_opts = areastyle_opts.opts

        self.opts: dict = {"show": is_show, "areaStyle": areastyle_opts}


class ItemStyleOpts:
    def __init__(
        self,
        color: Optional[str] = None,
        border_color: Optional[str] = None,
        opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "color": color,
            "borderColor": border_color,
            "opacity": opacity,
        }


class TextStyleOpts:
    def __init__(
        self,
        color: Optional[str] = None,
        font_style: Optional[str] = None,
        font_weight: Optional[str] = None,
        font_family: Optional[str] = None,
        font_size: Optional[Numeric] = None,
        line_height: Optional[str] = None,
    ):
        self.opts: dict = {
            "color": color,
            "fontStyle": font_style,
            "fontWeight": font_weight,
            "fontFamily": font_family,
            "fontSize": font_size,
            "lineHeight": line_height,
        }


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


class GraphNode:
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
        label_opts: Optional[LabelOpts] = None,
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        self.opts: dict = {
            "name": name,
            "x": x,
            "y": y,
            "fixed": is_fixed,
            "value": value,
            "category": category,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
        }


class GraphLink:
    def __init__(
        self,
        source: Union[str, int, None] = None,
        target: Union[str, int, None] = None,
        value: Optional[Numeric] = None,
        symbol: Union[str, Sequence, None] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        linestyle_opts: Optional[LineStyleOpts] = None,
        label_opts: Optional[LabelOpts] = None,
    ):
        if isinstance(linestyle_opts, LineStyleOpts):
            linestyle_opts = linestyle_opts.opts
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        self.opts: dict = {
            "source": source,
            "target": target,
            "value": value,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "lineStyle": linestyle_opts,
            "label": label_opts,
        }


class GraphCategory:
    def __init__(
        self,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        label_opts: Optional[LabelOpts] = None,
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        self.opts: dict = {
            "name": name,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
        }
