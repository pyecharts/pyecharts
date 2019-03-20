# coding=utf-8

from ...charts.chart import AxisChart
from ...options import AxisOpts, EffectOpts, InitOpts, LabelOpts
from ...types import ListTuple, Numeric, Optional, Union


class EffectScatter(AxisChart):
    """
    <<< 带有涟漪特效动画的散点图 >>>

    利用动画特效可以将某些想要突出的数据进行视觉突出。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[AxisOpts().opts])

    def add_yaxis(
        self,
        name: str,
        y_axis: ListTuple,
        *,
        symbol: Optional[str] = None,
        symbol_size: Numeric = 10,
        label_opts: Union[LabelOpts, dict] = LabelOpts,
        effect_opts: Union[EffectOpts, dict] = EffectOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(effect_opts, EffectOpts):
            effect_opts = effect_opts.opts

        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "effectScatter",
                "name": name,
                "showEffectOn": "render",
                "rippleEffect": effect_opts,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "data": [list(z) for z in zip(self._xaxis_data, y_axis)],
                "label": label_opts,
            }
        )
        return self
