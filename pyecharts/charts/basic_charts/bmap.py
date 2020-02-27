from ... import options as opts
from ... import types
from ...charts.basic_charts.geo import GeoChartBase
from ...commons.utils import OrderedSet
from ...exceptions import NonexistentCoordinatesException
from ...globals import ChartType

BAIDU_MAP_API = "https://api.map.baidu.com/api?v=2.0&ak={}"
BAIDU_MAP_GETSCRIPT = "https://api.map.baidu.com/getscript?v=2.0&ak={}"


class BMap(GeoChartBase):
    """
    <<< Baidu coordinate system >>>

    Support scatter plot, line
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        is_ignore_nonexistent_coord: bool = False,
    ):
        super().__init__(init_opts=init_opts)
        self.js_dependencies.add("bmap")
        self._is_geo_chart = True
        self._coordinate_system: types.Optional[str] = "bmap"
        self.bmap_js_functions: OrderedSet = OrderedSet()
        self._is_ignore_nonexistent_coord = is_ignore_nonexistent_coord

    def _feed_data(self, data_pair: types.Sequence, type_: str) -> types.Sequence:
        result = []
        type_list = [ChartType.LINES, ChartType.CUSTOM]
        if type_ in type_list:
            result = data_pair
        else:
            for n, v in data_pair:
                try:
                    lng, lat = self.get_coordinate(n)
                    result.append({"name": n, "value": [lng, lat, v]})
                except TypeError as err:
                    if self._is_ignore_nonexistent_coord is not True:
                        raise NonexistentCoordinatesException(err, (n, v))
        return result

    def add_schema(
        self,
        baidu_ak: str,
        center: types.Sequence,
        zoom: types.Union[types.Numeric, str] = None,
        is_roam: bool = True,
        map_style: types.Optional[dict] = None,
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
        navigation_control_opts: types.BMapNavigationControl = None,
        overview_map_opts: types.BMapOverviewMapControl = None,
        scale_control_opts: types.BMapScaleControl = None,
        maptype_control_opts: types.BMapTypeControl = None,
        copyright_control_opts: types.BMapCopyrightType = None,
        geo_location_control_opts: types.BMapGeoLocationControl = None,
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
                fns = panel.get("functions")
                for fn in fns:
                    self.bmap_js_functions.add(fn)

        return self
