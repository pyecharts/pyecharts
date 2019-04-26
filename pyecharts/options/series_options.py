# coding=utf-8
from ..commons.types import JSFunc, List, Numeric, Optional, Sequence, Tuple, Union


class ItemStyleOpts:
    def __init__(
        self,
        color: Optional[str] = None,
        color0: Optional[str] = None,
        border_color: Optional[str] = None,
        border_color0: Optional[str] = None,
        border_width: Optional[Numeric] = None,
        opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "color": color,
            "color0": color0,
            "borderColor": border_color,
            "borderColor0": border_color0,
            "borderWidth": border_width,
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
        rotate: Optional[Numeric] = None,
        horizontal_align: Optional[str] = None,
        vertical_align: Optional[str] = None,
        formatter: Union[str, JSFunc, None] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "position": position,
            "color": color,
            "rotate": rotate,
            "fontSize": font_size,
            "fontStyle": font_style,
            "fontWeight": font_weight,
            "fontFamily": font_family,
            "align": horizontal_align,
            "verticalAlign": vertical_align,
            "formatter": formatter,
        }


class LineStyleOpts:
    def __init__(
        self,
        width: Numeric = 1,
        opacity: Numeric = 1,
        curve: Numeric = 0,
        type_: str = "solid",
        color: Optional[str] = None,
    ):
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
        x: Union[str, Numeric, None] = None,
        y: Union[str, Numeric, None] = None,
        value_index: Optional[Numeric] = None,
        value_dim: Optional[str] = None,
        coord: Optional[Sequence] = None,
        symbol: Optional[str] = None,
        symbol_size: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "name": name,
            "type": type_,
            "valueIndex": value_index,
            "valueDim": value_dim,
            "xAxis": x,
            "yAxis": y,
            "coord": coord,
            "symbol": symbol,
            "symbolSize": symbol_size,
        }


class MarkLineOpts:
    def __init__(
        self,
        is_silent: bool = False,
        data: List[Union[MarkLineItem, dict]] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[None, Numeric] = None,
        precision: int = 2,
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
            "silent": is_silent,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "precision": precision,
            "label": label_opts,
            "data": _data,
        }


class MarkAreaItem:
    def __init__(
        self,
        name: Optional[str] = None,
        type_: Tuple[Optional[str], Optional[str]] = (None, None),
        value_index: Tuple[Optional[Numeric], Optional[Numeric]] = (None, None),
        value_dim: Tuple[Optional[str], Optional[str]] = (None, None),
        x: Tuple[Union[str, Numeric, None], Union[str, Numeric, None]] = (None, None),
        y: Tuple[Union[str, Numeric, None], Union[str, Numeric, None]] = (None, None),
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(itemstyle_opts, ItemStyleOpts):
            itemstyle_opts = itemstyle_opts.opts
        self.opts: List = [
            {
                "name": name,
                "type": type_[0],
                "valueIndex": value_index[0],
                "valueDim": value_dim[0],
                "xAxis": x[0],
                "yAxis": y[0],
                "label": label_opts,
                "itemStyle": itemstyle_opts,
            },
            {
                "type": type_[1],
                "valueIndex": value_index[1],
                "valueDim": value_dim[1],
                "xAxis": x[1],
                "yAxis": y[1],
            },
        ]


class MarkAreaOpts:
    def __init__(
        self,
        is_silent: bool = False,
        label_opts: LabelOpts = LabelOpts(),
        data: List[Union[MarkAreaItem, dict]] = None,
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

        self.opts: dict = {"silent": is_silent, "label": label_opts, "data": _data}


class EffectOpts:
    def __init__(
        self,
        is_show: bool = True,
        brush_type: str = "stroke",
        scale: Numeric = 2.5,
        period: Numeric = 4,
        color: Optional[str] = None,
        symbol: Optional[str] = None,
        symbol_size: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "brushType": brush_type,
            "scale": scale,
            "period": period,
            "color": color,
            "symbol": symbol,
            "symbolSize": symbol_size,
        }


class AreaStyleOpts:
    def __init__(self, opacity: Optional[Numeric] = 0, color: Optional[str] = None):
        self.opts: dict = {"opacity": opacity, "color": color}


class SplitAreaOpts:
    def __init__(self, is_show=True, areastyle_opts: AreaStyleOpts = AreaStyleOpts()):
        if isinstance(areastyle_opts, AreaStyleOpts):
            areastyle_opts = areastyle_opts.opts

        self.opts: dict = {"show": is_show, "areaStyle": areastyle_opts}


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


class TreeItem:
    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Numeric] = None,
        label_opts: Optional[LabelOpts] = None,
        children: Optional[Sequence] = None,
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        self.opts: dict = {
            "name": name,
            "value": value,
            "children": children,
            "label": label_opts,
        }
