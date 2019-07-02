import simplejson as json

from ..globals import BMapType
from .global_options import TooltipOpts
from .series_options import (
    BasicOpts,
    ItemStyleOpts,
    JSFunc,
    LabelOpts,
    LineStyleOpts,
    Numeric,
    Optional,
    Sequence,
    Union,
)


class SunburstItem(BasicOpts):
    def __init__(
        self,
        value: Optional[Numeric] = None,
        name: Optional[str] = None,
        link: Optional[str] = None,
        target: Optional[str] = "blank",
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        children: Optional[Sequence] = None,
    ):
        self.opts: dict = {
            "value": value,
            "name": name,
            "link": link,
            "target": target,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "children": children,
        }


class GraphNode(BasicOpts):
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
        label_opts: Union[LabelOpts, dict, None] = None,
    ):
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


class GraphLink(BasicOpts):
    def __init__(
        self,
        source: Union[str, int, None] = None,
        target: Union[str, int, None] = None,
        value: Optional[Numeric] = None,
        symbol: Union[str, Sequence, None] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "source": source,
            "target": target,
            "value": value,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "lineStyle": linestyle_opts,
            "label": label_opts,
        }


class GraphCategory(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
        symbol_size: Union[Numeric, Sequence, None] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "symbol": symbol,
            "symbolSize": symbol_size,
            "label": label_opts,
        }


class TreeItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Numeric] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        children: Optional[Sequence] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "children": children,
            "label": label_opts,
        }


class BMapNavigationControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_TOP_LEFT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 10,
        type_: Numeric = BMapType.NAVIGATION_CONTROL_LARGE,
        is_show_zoom_info: bool = False,
        is_enable_geo_location: bool = False,
    ):
        bmap_nav_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "type": type_,
                "showZoomInfo": is_show_zoom_info,
                "enableGeolocation": is_enable_geo_location,
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.NavigationControl({}));".format(
                    bmap_nav_config
                )
            ]
        }


class BMapOverviewMapControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_RIGHT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 50,
        is_open: bool = False,
    ):
        bmap_overview_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "isOpen": is_open,
            }
        )

        self.opts: dict = {
            "functions": [
                "var overview = new BMap.OverviewMapControl({});".format(
                    bmap_overview_config
                ),
                "bmap.addControl(overview);",
            ]
        }


class BMapScaleControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 80,
        offset_height: Numeric = 21,
    ):
        bmap_scale_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.ScaleControl({}));".format(bmap_scale_config)
            ]
        }


class BMapTypeControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_TOP_RIGHT,
        type_: Numeric = BMapType.MAPTYPE_CONTROL_HORIZONTAL,
    ):
        bmap_type_config = json.dumps({"anchor": position, "type": type_})

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.MapTypeControl({}));".format(bmap_type_config)
            ]
        }


class BMapCopyrightTypeOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 2,
        offset_height: Numeric = 2,
        copyright_: str = "",
    ):
        bmap_copyright_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
            }
        )

        bmap_copyright_content_config = json.dumps({"id": 1, "content": copyright_})

        self.opts: dict = {
            "functions": [
                "var copyright = new BMap.CopyrightControl({});".format(
                    bmap_copyright_config
                ),
                "copyright.addCopyright({});".format(bmap_copyright_content_config),
                "bmap.addControl(copyright);",
            ]
        }


class BMapGeoLocationControlOpts(BasicOpts):
    def __init__(
        self,
        position: Numeric = BMapType.ANCHOR_BOTTOM_LEFT,
        offset_width: Numeric = 10,
        offset_height: Numeric = 10,
        is_show_address_bar: bool = True,
        is_enable_auto_location: bool = False,
    ):
        bmap_geo_location_config = json.dumps(
            {
                "anchor": position,
                "offset": {"width": offset_width, "height": offset_height},
                "showAddressBar": is_show_address_bar,
                "enableAutoLocation": is_enable_auto_location,
            }
        )

        self.opts: dict = {
            "functions": [
                "bmap.addControl(new BMap.GeolocationControl({}))".format(
                    bmap_geo_location_config
                )
            ]
        }


class BarItem(BasicOpts):
    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Numeric] = None,
        label_opts: Union[LabelOpts, dict, None] = None,
        itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
        tooltip_opts: Union[TooltipOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "name": name,
            "value": value,
            "label": label_opts,
            "itemStyle": itemstyle_opts,
            "tooltip": tooltip_opts,
        }


class ComponentTitleOpts:
    def __init__(
        self,
        title: str = "",
        subtitle: str = "",
        title_style: Optional[dict] = None,
        subtitle_style: Optional[dict] = None,
    ):
        self.title = title.replace("\n", "<br/>")
        self.subtitle = subtitle.replace("\n", "<br/>")
        self.title_style: str = ""
        self.subtitle_style: str = ""
        title_style = title_style or {"style": "font-size: 18px; font-weight:bold;"}
        subtitle_style = subtitle_style or {"style": "font-size: 12px;"}
        self._convert_dict_to_string(title_style, subtitle_style)

    def _convert_dict_to_string(self, title_style: dict, subtitle_style: dict):
        for k, v in title_style.items():
            self.title_style += '{}="{}" '.format(k, v)
        for k, v in subtitle_style.items():
            self.subtitle_style += '{}="{}" '.format(k, v)


class PageLayoutOpts(BasicOpts):
    def __init__(
        self,
        justify_content: Optional[str] = None,
        margin: Optional[str] = None,
        display: Optional[str] = None,
        flex_wrap: Optional[str] = None,
    ):
        self.opts: dict = {
            "justify-content": justify_content,
            "margin": margin,
            "display": display,
            "flex-wrap": flex_wrap,
        }


class BaseGraphic(BasicOpts):
    pass


class GraphicShapeOpts(BaseGraphic):
    def __init__(
        self,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        width: Numeric = 0,
        height: Numeric = 0,
        r: Union[Sequence, Numeric, None] = None,
    ):
        self.opts: dict = {
            "x": pos_x,
            "y": pos_y,
            "width": width,
            "height": height,
            "r": r,
        }


class GraphicBasicStyleOpts(BaseGraphic):
    def __init__(
        self,
        fill: str = "#000",
        stroke: Optional[str] = None,
        line_width: Numeric = 0,
        shadow_blur: Optional[Numeric] = None,
        shadow_offset_x: Optional[Numeric] = None,
        shadow_offset_y: Optional[Numeric] = None,
        shadow_color: Optional[str] = None,
    ):
        self.opts: dict = {
            "fill": fill,
            "stroke": stroke,
            "line_width": line_width,
            "shadowBlur": shadow_blur,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "shadowColor": shadow_color,
        }


class GraphicImageStyleOpts(BaseGraphic):
    def __init__(
        self,
        image: Optional[str] = None,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        width: Numeric = 0,
        height: Numeric = 0,
        opacity: Numeric = 1,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "image": image,
            "x": pos_x,
            "y": pos_y,
            "width": width,
            "height": height,
            "opacity": opacity,
        }

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(graphic_basicstyle_opts.opts)
            else:
                self.opts.update(graphic_basicstyle_opts)


class GraphicTextStyleOpts(BaseGraphic):
    def __init__(
        self,
        text: Optional[JSFunc] = None,
        pos_x: Numeric = 0,
        pos_y: Numeric = 0,
        font: Optional[str] = None,
        text_align: str = "left",
        text_vertical_align: Optional[str] = None,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {
            "text": text,
            "x": pos_x,
            "y": pos_y,
            "font": font,
            "textAlign": text_align,
            "textVerticalAlign": text_vertical_align,
        }

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(graphic_basicstyle_opts.opts)
            else:
                self.opts.update(graphic_basicstyle_opts)


class GraphicItem(BaseGraphic):
    def __init__(
        self,
        id_: Optional[str] = None,
        action: str = "merge",
        position: [Sequence, Numeric, None] = None,
        rotation: Union[Numeric, JSFunc, None] = 0,
        scale: Union[Sequence, Numeric, None] = None,
        origin: Union[Numeric, Sequence, None] = None,
        left: Union[Numeric, str, None] = None,
        right: Union[Numeric, str, None] = None,
        top: Union[Numeric, str, None] = None,
        bottom: Union[Numeric, str, None] = None,
        bounding: str = "all",
        z: Numeric = 0,
        z_level: Numeric = 0,
        is_silent: bool = False,
        is_invisible: bool = False,
        is_ignore: bool = False,
        cursor: str = "pointer",
        is_draggable: bool = False,
        is_progressive: bool = False,
        width: Numeric = 0,
        height: Numeric = 0,
    ):
        self.opts: dict = {
            "id": id_,
            "$action": action,
            "position": position,
            "rotation": rotation,
            "scale": scale,
            "origin": origin,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "bounding": bounding,
            "z": z,
            "zlevel": z_level,
            "silent": is_silent,
            "invisible": is_invisible,
            "ignore": is_ignore,
            "cursor": cursor,
            "draggable": is_draggable,
            "progressive": is_progressive,
            "width": width,
            "height": height,
        }


class GraphicGroup(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        is_diff_children_by_name: bool = False,
        children: Optional[Sequence[BaseGraphic]] = None,
    ):
        self.opts: dict = {
            "type": "group",
            "diffChildrenByName": is_diff_children_by_name,
            "children": children,
        }

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)


class GraphicImage(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_imagestyle_opts: Union[GraphicImageStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "image"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_imagestyle_opts:
            if isinstance(graphic_imagestyle_opts, GraphicImageStyleOpts):
                self.opts.update(style=graphic_imagestyle_opts.opts)
            else:
                self.opts.update(style=graphic_imagestyle_opts)


class GraphicText(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_textstyle_opts: Union[GraphicTextStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "text"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_textstyle_opts:
            if isinstance(graphic_textstyle_opts, GraphicTextStyleOpts):
                self.opts.update(style=graphic_textstyle_opts.opts)
            else:
                self.opts.update(style=graphic_textstyle_opts)


class GraphicRect(BaseGraphic):
    def __init__(
        self,
        graphic_item: Union[GraphicItem, dict, None] = None,
        graphic_shape_opts: Union[GraphicShapeOpts, dict, None] = None,
        graphic_basicstyle_opts: Union[GraphicBasicStyleOpts, dict, None] = None,
    ):
        self.opts: dict = {"type": "rect"}

        if graphic_item:
            if isinstance(graphic_item, GraphicItem):
                self.opts.update(graphic_item.opts)
            else:
                self.opts.update(graphic_item)

        if graphic_shape_opts:
            if isinstance(graphic_shape_opts, GraphicShapeOpts):
                self.opts.update(shape=graphic_shape_opts.opts)
            else:
                self.opts.update(graphic_shape_opts)

        if graphic_basicstyle_opts:
            if isinstance(graphic_basicstyle_opts, GraphicBasicStyleOpts):
                self.opts.update(style=graphic_basicstyle_opts.opts)
            else:
                self.opts.update(style=graphic_basicstyle_opts)
