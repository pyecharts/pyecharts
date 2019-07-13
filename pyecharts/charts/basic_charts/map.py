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
        data_pair: types.Sequence,
        maptype: str = "china",
        *,
        is_selected: bool = True,
        is_roam: bool = True,
        center: types.Optional[types.Sequence] = None,
        zoom: types.Optional[types.Numeric] = 1,
        name_map: types.Optional[dict] = None,
        symbol: types.Optional[str] = None,
        is_map_symbol_show: bool = True,
        label_opts: types.Label = opts.LabelOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_label_opts: types.Label = None,
        emphasis_itemstyle_opts: types.ItemStyle = None,
    ):
        self.js_dependencies.add(maptype)
        data = [{"name": n, "value": v} for n, v in data_pair]
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
                "center": center,
                "zoom": zoom,
                "nameMap": name_map,
                "showLegendSymbol": is_map_symbol_show,
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
