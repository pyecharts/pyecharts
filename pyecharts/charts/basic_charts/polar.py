from ... import options as opts
from ...charts.chart import Chart
from ...commons.types import Numeric, Optional, Sequence, Union
from ...globals import ChartType


class Polar(Chart):
    """
    <<< Polar >>>

    Polar coordinates can be used for scatter and polyline graphs.
    """

    def __init__(self, init_opts: opts.InitOpts = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.add_schema()

    def add_schema(
        self,
        radiusaxis_opts: Union[opts.RadiusAxisOpts, dict] = opts.RadiusAxisOpts(),
        angleaxis_opts: Union[opts.AngleAxisOpts, dict] = opts.AngleAxisOpts(),
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
        data: Sequence,
        *,
        is_selected: bool = True,
        type_: str = "line",
        symbol: Optional[str] = None,
        symbol_size: Numeric = 4,
        stack: Optional[str] = None,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        areastyle_opts: Union[opts.AreaStyleOpts, dict] = opts.AreaStyleOpts(),
        effect_opts: Union[opts.EffectOpts, dict] = opts.EffectOpts(),
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,
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
        return self
