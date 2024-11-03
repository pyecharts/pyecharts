from ... import options as opts
from ... import types
from ...charts.basic_charts.geo import GeoChartBase
from ...commons.utils import OrderedSet, JsCode
from ...exceptions import NonexistentCoordinatesException
from ...globals import ChartType

AMAP_API = "https://webapi.amap.com/maps?v=2.0&key={}&plugin=AMap.Scale,AMap.ToolBar"


class AMap(GeoChartBase):
    """
    <<< AMap(GaoDe) coordinate system >>>

    Support scatter plot, line.
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        is_ignore_nonexistent_coord: bool = False,
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.js_dependencies.add("amap")
        self._is_geo_chart = True
        self._coordinate_system: types.Optional[str] = "amap"
        self.amap_js_functions: OrderedSet = OrderedSet()
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
        amap_ak: str,
        center: types.Sequence,
        zoom: types.Union[types.Numeric, str] = None,
        is_enable_resize: bool = True,
        map_style: types.Optional[dict] = None,
        is_render_on_map: bool = True,
        is_layer_interactive: bool = True,
        is_large: bool = False,
    ):
        self.js_dependencies.add(AMAP_API.format(amap_ak))
        self.options.update(
            amap={
                "center": center,
                "viewMode": "3D",  # default
                "zoom": zoom,
                "resizeEnable": is_enable_resize,
                "mapStyle": map_style,
                "renderOnMoving": is_render_on_map,
                "echartsLayerInteractive": is_layer_interactive,
                "largeMode": is_large,
            }
        )
        if is_layer_interactive:
            self.amap_js_functions.add(
                "amapComponent.setEChartsLayerInteractive(true);"
            )

        return self

    def add_control_panel(
        self,
        is_add_satellite_layer: bool = False,
        is_add_road_net_layer: bool = False,
    ):
        if is_add_satellite_layer:
            self.amap_js_functions.add(
                "amap.add(new AMap.TileLayer.Satellite());",
            )
        if is_add_road_net_layer:
            self.amap_js_functions.add(
                "amap.add(new AMap.TileLayer.RoadNet());",
            )

        return self
