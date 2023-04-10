from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class MapMixin:
    """
    <<< Map >>>

    Map are mainly used for visualization of geographic area data.
    """

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence[types.Union[types.Sequence, opts.MapItem, dict]],
        maptype: str = "china",
        *,
        is_roam: bool = True,
        center: types.Optional[types.Sequence] = None,
        aspect_scale: types.Numeric = 0.75,
        bounding_coords: types.Optional[types.Sequence[types.Numeric]] = None,
        min_scale_limit: types.Optional[types.Numeric] = None,
        max_scale_limit: types.Optional[types.Numeric] = None,
        name_property: str = "name",
        selected_mode: types.Union[bool, str] = False,
        zoom: types.Optional[types.Numeric] = 1,
        name_map: types.Optional[dict] = None,
        symbol: types.Optional[str] = None,
        map_value_calculation: str = "sum",
        is_map_symbol_show: bool = True,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
        pos_left: types.Optional[types.Union[str, types.Numeric]] = None,
        pos_top: types.Optional[types.Union[str, types.Numeric]] = None,
        pos_right: types.Optional[types.Union[str, types.Numeric]] = None,
        pos_bottom: types.Optional[types.Union[str, types.Numeric]] = None,
        geo_index: types.Optional[types.Numeric] = None,
        series_layout_by: str = "column",
        dataset_index: types.Optional[types.Numeric] = 0,
        layout_center: types.Optional[types.Sequence[str]] = None,
        layout_size: types.Union[str, types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_label_opts: types.Label = None,
        emphasis_itemstyle_opts: types.ItemStyle = None,
    ):
        self.js_dependencies.add(maptype)
        self._geo_json_name = maptype

        if isinstance(data_pair[0], opts.MapItem):
            data = data_pair
        else:
            data = [{"name": n, "value": v} for n, v in data_pair]

        scale_limit: types.Optional[dict] = {
            "min": min_scale_limit,
            "max": max_scale_limit,
        }
        if min_scale_limit is None and max_scale_limit is None:
            scale_limit = None

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.MAP,
                "name": series_name,
                "symbol": symbol,
                "label": label_opts,
                "map": maptype,
                "data": data,
                "roam": is_roam,
                "aspectScale": aspect_scale,
                "boundingCoords": bounding_coords,
                "scaleLimit": scale_limit,
                "nameProperty": name_property,
                "selectedMode": selected_mode,
                "center": center,
                "zoom": zoom,
                "nameMap": name_map,
                "zlevel": z_level,
                "z": z,
                "left": pos_left,
                "top": pos_top,
                "right": pos_right,
                "bottom": pos_bottom,
                "geoIndex": geo_index,
                "seriesLayoutBy": series_layout_by,
                "datasetIndex": dataset_index,
                "mapValueCalculation": map_value_calculation,
                "showLegendSymbol": is_map_symbol_show,
                "layoutCenter": layout_center,
                "layoutSize": layout_size,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": {
                    "label": emphasis_label_opts,
                    "itemStyle": emphasis_itemstyle_opts,
                },
            }
        )
        return self


class Map(Chart, MapMixin):
    def add_geo_json(self, geo_json: dict):
        self._geo_json = geo_json
        return self
