import simplejson as json

from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...datasets import COORDINATES
from ...exceptions import NonexistentCoordinatesException
from ...globals import ChartType


class GeoChartBase(Chart):
    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.set_global_opts()
        self._coordinates = COORDINATES
        self._zlevel = 1
        self._coordinate_system: types.Optional[str] = None
        self._chart_type = ChartType.GEO

    def add_coordinate(
        self, name: str, longitude: types.Numeric, latitude: types.Numeric
    ):
        self._coordinates.update({name: [longitude, latitude]})
        return self

    def add_coordinate_json(self, json_file: str):
        with open(json_file, "r", encoding="utf-8") as f:
            json_reader = json.load(f)
            for k, v in json_reader.items():
                self.add_coordinate(k, v[0], v[1])
        return self

    def get_coordinate(self, name: str) -> types.Optional[types.Sequence]:
        if name in self._coordinates:
            return self._coordinates[name]

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence,
        type_: str = "scatter",
        *,
        is_selected: bool = True,
        symbol: types.Optional[str] = None,
        symbol_size: types.Numeric = 12,
        blur_size: types.Numeric = 20,
        point_size: types.Numeric = 20,
        color: types.Optional[str] = None,
        is_polyline: bool = False,
        is_large: bool = False,
        large_threshold: types.Numeric = 2000,
        progressive: types.Numeric = 400,
        progressive_threshold: types.Numeric = 3000,
        label_opts: types.Label = opts.LabelOpts(),
        effect_opts: types.Effect = opts.EffectOpts(),
        linestyle_opts: types.LineStyle = opts.LineStyleOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        render_item: types.JsCode = None,
        encode: types.Union[types.JsCode, dict] = None,
    ):
        self._zlevel += 1
        data = self._feed_data(data_pair, type_)

        self._append_color(color)
        self._append_legend(series_name, is_selected)

        if type_ == ChartType.SCATTER:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": self._coordinate_system,
                    "symbol": symbol,
                    "symbolSize": symbol_size,
                    "data": data,
                    "label": label_opts,
                    "tooltip": tooltip_opts,
                    "itemStyle": itemstyle_opts,
                }
            )

        elif type_ == ChartType.EFFECT_SCATTER:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": self._coordinate_system,
                    "showEffectOn": "render",
                    "rippleEffect": effect_opts,
                    "symbol": symbol,
                    "symbolSize": symbol_size,
                    "data": data,
                    "label": label_opts,
                    "tooltip": tooltip_opts,
                    "itemStyle": itemstyle_opts,
                }
            )

        elif type_ == ChartType.HEATMAP:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": self._coordinate_system,
                    "data": data,
                    "tooltip": tooltip_opts,
                    "itemStyle": itemstyle_opts,
                    "pointSize": point_size,
                    "blurSize": blur_size,
                }
            )

        elif type_ == ChartType.LINES:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": self._coordinate_system,
                    "zlevel": self._zlevel,
                    "progressive": progressive,
                    "progressiveThreshold": progressive_threshold,
                    "effect": effect_opts,
                    "symbol": symbol or ["none", "arrow"],
                    "polyline": is_polyline,
                    "large": is_large,
                    "largeThreshold": large_threshold,
                    "symbolSize": symbol_size,
                    "data": data,
                    "lineStyle": linestyle_opts,
                    "tooltip": tooltip_opts,
                    "itemStyle": itemstyle_opts,
                    "label": label_opts,
                }
            )
        elif type_ == ChartType.CUSTOM:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": self._coordinate_system,
                    "renderItem": render_item,
                    "emphasis": {"itemStyle": itemstyle_opts},
                    "encode": encode,
                    "data": data,
                }
            )
        return self


class Geo(GeoChartBase):
    """
    <<< geo coordinate system >>>

    support scatter plot and line
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        is_ignore_nonexistent_coord: bool = False,
    ):
        super().__init__(init_opts=init_opts)
        self._coordinate_system: types.Optional[str] = "geo"
        self._is_ignore_nonexistent_coord = is_ignore_nonexistent_coord

    def _feed_data(self, data_pair: types.Sequence, type_: str) -> types.Sequence:
        result = []
        for n, v in data_pair:
            try:
                if type_ == ChartType.LINES:
                    f, t = self.get_coordinate(n), self.get_coordinate(v)
                    result.append({"name": "{}->{}".format(n, v), "coords": [f, t]})
                else:
                    lng, lat = self.get_coordinate(n)
                    result.append({"name": n, "value": [lng, lat, v]})
            except TypeError as err:
                if self._is_ignore_nonexistent_coord is not True:
                    raise NonexistentCoordinatesException(err, (n, v))
        return result

    def add_schema(
        self,
        maptype: str = "china",
        is_roam: bool = True,
        zoom: types.Optional[types.Numeric] = None,
        center: types.Optional[types.Sequence] = None,
        aspect_scale: types.Numeric = 0.75,
        bounding_coords: types.Optional[types.Sequence[types.Numeric]] = None,
        min_scale_limit: types.Optional[types.Numeric] = None,
        max_scale_limit: types.Optional[types.Numeric] = None,
        name_property: str = "name",
        selected_mode: types.Union[bool, str] = False,
        layout_center: types.Optional[types.Sequence[str]] = None,
        layout_size: types.Union[str, types.Numeric] = None,
        label_opts: types.Label = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_itemstyle_opts: types.ItemStyle = None,
        emphasis_label_opts: types.Label = None,
    ):
        self.js_dependencies.add(maptype)
        if center:
            assert len(center) == 2

        scale_limit: types.Optional[dict] = {
            "min": min_scale_limit,
            "max": max_scale_limit,
        }
        if min_scale_limit is None and max_scale_limit is None:
            scale_limit = None

        self.options.update(
            geo={
                "map": maptype,
                "zoom": zoom,
                "center": center,
                "roam": is_roam,
                "aspectScale": aspect_scale,
                "boundingCoords": bounding_coords,
                "scaleLimit": scale_limit,
                "nameProperty": name_property,
                "selectedMode": selected_mode,
                "layoutCenter": layout_center,
                "layoutSize": layout_size,
                "label": label_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": {
                    "itemStyle": emphasis_itemstyle_opts,
                    "label": emphasis_label_opts,
                },
            }
        )
        return self
