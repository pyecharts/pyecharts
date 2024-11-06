from ... import options as opts
from ... import types
from ...charts.basic_charts.geo import GeoChartBase
from ...commons.utils import OrderedSet, JsCode
from ...exceptions import NonexistentCoordinatesException
from ...globals import ChartType


class LMap(GeoChartBase):
    """
    <<< LMap(leaflet) coordinate system >>>

    Support scatter plot, line.
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        is_ignore_nonexistent_coord: bool = False,
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.js_dependencies.add("lmap-css")
        self.js_dependencies.add("lmap-src")
        self.js_dependencies.add("lmap")
        self._is_geo_chart = True
        self._coordinate_system: types.Optional[str] = "lmap"
        self.lmap_js_functions: OrderedSet = OrderedSet()
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
        center: types.Sequence,
        zoom: types.Union[types.Numeric, str] = None,
        is_enable_resize: bool = True,
        is_render_on_map: bool = True,
        is_layer_interactive: bool = True,
        is_large: bool = False,
    ):
        self.options.update(
            lmap={
                "center": center,
                "zoom": zoom,
                "resizeEnable": is_enable_resize,
                "renderOnMoving": is_render_on_map,
                "echartsLayerInteractive": is_layer_interactive,
                "largeMode": is_large,
            }
        )

        return self
