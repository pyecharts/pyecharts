from ... import options as opts
from ... import types
from ...charts.basic_charts.map import MapMixin
from ...charts.chart import Chart3D
from ...globals import ChartType
from ...options import InitOpts


class Map3D(Chart3D, MapMixin):
    """
    3D map
    """

    def __init__(self, init_opts: types.Init = InitOpts()):
        super().__init__(init_opts)
        self._3d_chart_type = "map3D"

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
                "type": ChartType.MAP3D,
                "name": series_name,
                "symbol": symbol,
                "label": label_opts,
                "coordinateSystem": "geo3D",
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

    def add_schema(self, maptype: str = "china", box_opts: dict = None):
        self.js_dependencies.add(maptype)
        self.options.update(geo3D={"map": maptype})
        return self
