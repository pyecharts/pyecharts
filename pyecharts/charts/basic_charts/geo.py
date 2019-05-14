import json

from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Optional, Sequence, Union
from ...commons.utils import JsCode
from ...datasets import COORDINATES
from ...globals import ChartType, TooltipFormatterType


class GeoChartBase(Chart):
    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.set_global_opts()
        self._coordinates = COORDINATES
        self._zlevel = 1
        self._coordinate_system: Optional[str] = None

    def add_coordinate(self, name: str, longitude: Numeric, latitude: Numeric):
        self._coordinates.update({name: [longitude, latitude]})
        return self

    def add_coordinate_json(self, json_file: str):
        with open(json_file, "r", encoding="utf-8") as f:
            json_reader = json.load(f)
            for k, v in json_reader.items():
                self.add_coordinate(k, v[0], v[1])
        return self

    def get_coordinate(self, name: str) -> Optional[Sequence]:
        if name in self._coordinates:
            return self._coordinates[name]

    def add(
        self,
        series_name: str,
        data_pair: Sequence,
        type_: str = "scatter",
        *,
        is_selected: bool = True,
        symbol: Optional[str] = None,
        symbol_size: Numeric = 12,
        color: Optional[str] = None,
        is_polyline: bool = False,
        is_large: bool = False,
        large_threshold: Numeric = 2000,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        effect_opts: Union[opts.EffectOpts, dict] = opts.EffectOpts(),
        linestyle_opts: Union[opts.LineStyleOpts, dict] = opts.LineStyleOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
    ):
        self._zlevel += 1

        data = []
        if type_ == ChartType.LINES and self._coordinate_system == "bmap":
            data = data_pair
        else:
            for n, v in data_pair:
                if type_ == ChartType.LINES:
                    f, t = self.get_coordinate(n), self.get_coordinate(v)
                    data.append({"name": "{}->{}".format(n, v), "coords": [f, t]})
                else:
                    lng, lat = self.get_coordinate(n)
                    data.append({"name": n, "value": [lng, lat, v]})

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
                }
            )

        elif type_ == ChartType.LINES:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": self._coordinate_system,
                    "zlevel": self._zlevel,
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
                }
            )

        return self

    def set_global_opts(
        self,
        title_opts: Union[opts.TitleOpts, dict] = opts.TitleOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict] = opts.TooltipOpts(
            formatter=JsCode(TooltipFormatterType.GEO)
        ),
        legend_opts: Union[opts.LegendOpts, dict] = opts.LegendOpts(),
        toolbox_opts: Union[opts.ToolboxOpts, dict] = None,
        xaxis_opts: Union[opts.AxisOpts, dict, None] = None,
        yaxis_opts: Union[opts.AxisOpts, dict, None] = None,
        visualmap_opts: Union[opts.VisualMapOpts, dict, None] = None,
        datazoom_opts: Sequence[Union[opts.DataZoomOpts, dict, None]] = None,
    ):
        return super().set_global_opts(
            title_opts=title_opts,
            tooltip_opts=tooltip_opts,
            legend_opts=legend_opts,
            toolbox_opts=toolbox_opts,
            xaxis_opts=xaxis_opts,
            yaxis_opts=yaxis_opts,
            visualmap_opts=visualmap_opts,
            datazoom_opts=datazoom_opts,
        )


class Geo(GeoChartBase):
    """
    <<< geo coordinate system >>>

    support scatter plot and line
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self._coordinate_system: Optional[str] = "geo"

    def add_schema(
        self,
        maptype: str = "china",
        is_roam: bool = True,
        label_opts: Union[opts.LabelOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
        emphasis_itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
        emphasis_label_opts: Union[opts.LabelOpts, dict, None] = None,
    ):
        self.js_dependencies.add(maptype)
        self.options.update(
            geo={
                "map": maptype,
                "roam": is_roam,
                "label": label_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": {
                    "itemStyle": emphasis_itemstyle_opts,
                    "label": emphasis_label_opts,
                },
            }
        )
        return self
