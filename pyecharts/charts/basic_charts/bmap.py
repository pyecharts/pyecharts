from ... import options as opts
from ...charts.basic_charts.geo import GeoChartBase
from ...commons import utils
from ...commons.types import Optional, Sequence, Union

BAIDU_MAP_API = "http://api.map.baidu.com/api?v=2.0&ak={}"
BAIDU_MAP_GETSCRIPT = "http://api.map.baidu.com/getscript?v=2.0&ak={}"


class BMap(GeoChartBase):
    """
    <<< Baidu coordinate system >>>
    Support scatter plot, line
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.js_dependencies.add("bmap")
        self._is_geo_chart = True
        self._coordinate_system: Optional[str] = "bmap"
        self.js_bmap_functions: utils.OrderedSet = utils.OrderedSet()

    def add_schema(
        self,
        baidu_ak: str,
        center: Sequence,
        zoom: Optional[int] = None,
        is_roam: bool = True,
        map_style: Optional[dict] = None,
    ):
        self.js_dependencies.add(
            BAIDU_MAP_API.format(baidu_ak), BAIDU_MAP_GETSCRIPT.format(baidu_ak)
        )
        self.options.update(
            bmap={
                "center": center,
                "zoom": zoom,
                "roam": is_roam,
                "mapStyle": map_style,
            }
        )
        return self

    def add_control_panel(
        self,
        navigation_control_opts: Union[opts.BMapNavigationControlOpts, None] = None,
        overview_map_opts: Union[opts.BMapOverviewMapControlOpts, None] = None,
        scale_control_opts: Union[opts.BMapScaleControlOpts, None] = None,
        maptype_control_opts: Union[opts.BMapTypeControl, None] = None,
        copyright_control_opts: Union[opts.BMapCopyrightType, None] = None,
        geo_location_control_opts: Union[opts.BMapGeoLocationControlOpts, None] = None,
    ):
        panel_options = [
            navigation_control_opts,
            overview_map_opts,
            scale_control_opts,
            maptype_control_opts,
            copyright_control_opts,
            geo_location_control_opts,
        ]

        for panel in panel_options:
            if panel is not None:
                fns = panel.opts.get("functions")
                for fn in fns:
                    self.add_js_funcs(fn)

        return self

    def add_js_funcs(self, *fns: Sequence):
        for fn in fns:
            self.js_bmap_functions.add(fn)
