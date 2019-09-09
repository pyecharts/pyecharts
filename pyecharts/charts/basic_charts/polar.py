from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...commons.utils import JsCode
from ...globals import ChartType


class Polar(Chart):
    """
    <<< Polar >>>

    Polar coordinates can be used for scatter and polyline graphs.
    """

    def __init__(self, init_opts: types.Init = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.add_schema()

    def add_schema(
        self,
        radiusaxis_opts: types.RadiusAxis = opts.RadiusAxisOpts(),
        angleaxis_opts: types.AngleAxis = opts.AngleAxisOpts(),
    ):
        if isinstance(angleaxis_opts, opts.AngleAxisOpts):
            angleaxis_opts = angleaxis_opts.opts
        if isinstance(radiusaxis_opts, opts.RadiusAxisOpts):
            radiusaxis_opts = radiusaxis_opts.opts
        self.options.update(radiusAxis=radiusaxis_opts, angleAxis=angleaxis_opts)
        return self

    def add(
        self,
        series_name: str,
        data: types.Sequence,
        *,
        is_selected: bool = True,
        type_: str = "line",
        symbol: types.Optional[str] = None,
        symbol_size: types.Numeric = 4,
        stack: types.Optional[str] = None,
        label_opts: types.Label = opts.LabelOpts(is_show=False),
        areastyle_opts: types.AreaStyle = opts.AreaStyleOpts(),
        effect_opts: types.Effect = opts.EffectOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
    ):
        self._append_legend(series_name, is_selected)
        self.options.update(polar={})

        if type_ in (ChartType.SCATTER, ChartType.LINE, ChartType.BAR):
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "polar",
                    "symbol": symbol,
                    "symbolSize": symbol_size,
                    "data": data,
                    "stack": stack,
                    "label": label_opts,
                    "areaStyle": areastyle_opts,
                    "tooltip": tooltip_opts,
                    "itemStyle": itemstyle_opts,
                }
            )

        elif type_ == ChartType.EFFECT_SCATTER:
            self.options.get("series").append(
                {
                    "type": type_,
                    "name": series_name,
                    "coordinateSystem": "polar",
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

        if label_opts.get("show"):
            self.options.get("series").append(
                {
                    "type": ChartType.CUSTOM,
                    "coordinateSystem": "polar",
                    # TODO: 提供自定义 function
                    "renderItem": JsCode(
                        """function(params, api) {
                        var values = [api.value(0), api.value(1)];
                        var coord = api.coord(values);
                        return {
                            type: 'text',
                            position: [3 * Math.sin(coord[3]), 3 * Math.cos(coord[3])],
                            rotation: coord[3] + Math.PI / 2,
                            origin: [coord[0], coord[1]],
                            style: {
                                text: api.value(1),
                                fill: 'black',
                                fontSize: 12,
                                textAlign: 'right',
                                textVerticalAlign: 'middle',
                                x: coord[0],
                                y: coord[1]
                            }
                        };
                    }"""
                    ),
                    "data": data,
                }
            )
        return self
