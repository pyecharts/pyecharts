import json

from ..commons.types import Numeric, Optional, Sequence, Union
from ..globals import BMapType
from .global_options import TooltipOpts
from .series_options import BasicOpts, ItemStyleOpts, LabelOpts, LineStyleOpts


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


class BMapTypeControl(BasicOpts):
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


class BMapCopyrightType(BasicOpts):
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
