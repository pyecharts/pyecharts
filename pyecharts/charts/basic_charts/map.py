from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Optional, Sequence, Union
from ...globals import ChartType


class Map(Chart):
    """
    <<< Map >>>

    Map are mainly used for visualization of geographic area data.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        series_name: str,
        data_pair: Sequence,
        maptype: str = "china",
        *,
        is_selected: bool = True,
        is_roam: bool = True,
        center: Optional[Sequence] = None,
        zoom: Optional[Numeric] = 1,
        name_map: Optional[dict] = None,
        symbol: Optional[str] = None,
        is_map_symbol_show: bool = True,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
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
            }
        )
        return self
