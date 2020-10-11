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
        is_selected: bool = True,
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
        layout_center: types.Optional[types.Sequence[str]] = None,
        layout_size: types.Union[str, types.Numeric] = None,
        label_opts: types.Label = opts.LabelOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_label_opts: types.Label = None,
        emphasis_itemstyle_opts: types.ItemStyle = None,
    ):
        self.js_dependencies.add(maptype)

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

        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.MAP,
                "name": series_name,
                "symbol": symbol,
                "label": label_opts,
                "mapType": maptype,
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
    pass
