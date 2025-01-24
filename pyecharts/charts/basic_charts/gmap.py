from ... import options as opts
from ... import types
from ...charts.basic_charts.geo import GeoChartBase
from ...commons.utils import OrderedSet, JsCode
from ...exceptions import NonexistentCoordinatesException
from ...globals import ChartType

GMAP_API = "https://maps.googleapis.com/maps/api/js?key={}"


class GMap(GeoChartBase):
    """
    <<< GMap(Google Map) coordinate system >>>

    Support scatter plot, line.
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        is_ignore_nonexistent_coord: bool = False,
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.js_dependencies.add("gmap")
        self._is_geo_chart = True
        self._coordinate_system: types.Optional[str] = "gmap"
        self.gmap_js_functions: OrderedSet = OrderedSet()
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
        gmap_ak: str,
        center: types.Sequence,
        zoom: types.Union[types.Numeric, str] = None,
        is_render_on_map: bool = True,
        z_index: types.Optional[int] = None,
        is_roam: bool = True,
    ):
        self.js_dependencies.add(GMAP_API.format(gmap_ak))
        self.options.update(
            gmap={
                "center": center,
                "zoom": zoom,
                "renderOnMoving": is_render_on_map,
                "echartsLayerZIndex": z_index,
                "roam": is_roam
            }
        )
        return self

    def add_control_panel(
        self,
        is_add_traffic_layer: bool = False,
    ):
        if is_add_traffic_layer:
            self.gmap_js_functions.add(
                "var trafficLayer = new google.maps.TrafficLayer(); "
                "trafficLayer.setMap(gmap);"
            )

        return self
