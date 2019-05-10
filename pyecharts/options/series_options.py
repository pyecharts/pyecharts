from ..commons.types import Any, JSFunc, Numeric, Optional, Sequence, Tuple, Union


class BasicOpts:
    __slots__ = ("opts",)

    def update(self, **kwargs):
        self.opts.update(kwargs)

    def get(self, key: str) -> Any:
        return self.opts.get(key)


class ItemStyleOpts(BasicOpts):
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


class TextStyleOpts(BasicOpts):
    def __init__(
        self,
        color: Optional[str] = None,
        font_style: Optional[str] = None,
        font_weight: Optional[str] = None,
        font_family: Optional[str] = None,
        font_size: Optional[Numeric] = None,
        align: Optional[str] = None,
        vertical_align: Optional[str] = None,
        line_height: Optional[str] = None,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Optional[Numeric] = None,
        border_radius: Union[Numeric, Sequence, None] = None,
        padding: Union[Numeric, Sequence, None] = None,
        shadow_color: Optional[str] = None,
        shadow_blur: Optional[Numeric] = None,
        width: Optional[str] = None,
        height: Optional[str] = None,
        rich: Optional[dict] = None,
    ):
        self.opts: dict = {
            "color": color,
            "fontStyle": font_style,
            "fontWeight": font_weight,
            "fontFamily": font_family,
            "fontSize": font_size,
            "align": align,
            "verticalAlign": vertical_align,
            "lineHeight": line_height,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "borderRadius": border_radius,
            "padding": padding,
            "shadowColor": shadow_color,
            "shadowBlur": shadow_blur,
            "width": width,
            "height": height,
            "rich": rich,
        }


class LabelOpts(BasicOpts):
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
        margin: Optional[Numeric] = 8,
        horizontal_align: Optional[str] = None,
        vertical_align: Optional[str] = None,
        formatter: Optional[JSFunc] = None,
        background_color: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: Optional[Numeric] = None,
        border_radius: Optional[Numeric] = None,
        rich: Optional[dict] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "position": position,
            "color": color,
            "rotate": rotate,
            "margin": margin,
            "fontSize": font_size,
            "fontStyle": font_style,
            "fontWeight": font_weight,
            "fontFamily": font_family,
            "align": horizontal_align,
            "verticalAlign": vertical_align,
            "formatter": formatter,
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
            "borderRadius": border_radius,
            "rich": rich,
        }


class LineStyleOpts(BasicOpts):
    def __init__(
        self,
        width: Numeric = 1,
        opacity: Numeric = 1,
        curve: Numeric = 0,
        type_: str = "solid",
        color: Union[str, Sequence, None] = None,
    ):
        self.opts: dict = {
            "width": width,
            "opacity": opacity,
            "curveness": curve,
            "type": type_,
            "color": color,
        }


class SplitLineOpts(BasicOpts):
    def __init__(
        self, is_show: bool = False, linestyle_opts: LineStyleOpts = LineStyleOpts()
    ):
        self.opts: dict = {"show": is_show, "lineStyle": linestyle_opts}


class MarkPointItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        type_: Optional[str] = None,
        value_index: Optional[Numeric] = None,
        value_dim: Optional[str] = None,
        coord: Optional[Sequence] = None,
        x: Optional[Numeric] = None,
        y: Optional[Numeric] = None,
        value: Optional[Numeric] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
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


class MarkPointOpts(BasicOpts):
    def __init__(
        self,
        data: Sequence[Union[MarkPointItem, dict]] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[None, Numeric] = None,
        label_opts: LabelOpts = LabelOpts(position="inside", color="#fff"),
    ):
        self.opts: dict = {
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
            "data": data,
        }


class MarkLineItem(BasicOpts):
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


class MarkLineOpts(BasicOpts):
    def __init__(
        self,
        is_silent: bool = False,
        data: Sequence[Union[MarkLineItem, dict]] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[None, Numeric] = None,
        precision: int = 2,
        label_opts: LabelOpts = LabelOpts(),
    ):
        self.opts: dict = {
            "silent": is_silent,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "precision": precision,
            "label": label_opts,
            "data": data,
        }


class MarkAreaItem(BasicOpts):
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
        self.opts: Sequence = [
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


class MarkAreaOpts(BasicOpts):
    def __init__(
        self,
        is_silent: bool = False,
        label_opts: LabelOpts = LabelOpts(),
        data: Sequence[Union[MarkAreaItem, dict]] = None,
    ):
        self.opts: dict = {"silent": is_silent, "label": label_opts, "data": data}


class EffectOpts(BasicOpts):
    def __init__(
        self,
        is_show: bool = True,
        brush_type: str = "stroke",
        scale: Numeric = 2.5,
        period: Numeric = 4,
        color: Optional[str] = None,
        symbol: Optional[str] = None,
        symbol_size: Optional[Numeric] = None,
        trail_length: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "show": is_show,
            "brushType": brush_type,
            "scale": scale,
            "period": period,
            "color": color,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "trailLength": trail_length,
        }


class AreaStyleOpts(BasicOpts):
    def __init__(self, opacity: Optional[Numeric] = 0, color: Optional[str] = None):
        self.opts: dict = {"opacity": opacity, "color": color}


class SplitAreaOpts(BasicOpts):
    def __init__(self, is_show=True, areastyle_opts: AreaStyleOpts = AreaStyleOpts()):
        self.opts: dict = {"show": is_show, "areaStyle": areastyle_opts}
