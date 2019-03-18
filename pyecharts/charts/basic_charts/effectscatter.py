# coding=utf-8

from ...charts.chart import Chart
from ...options import AxisOpts, EffectOpts, InitOpts, LabelOpts
from ...types import *


class EffectScatter(Chart):
    """
    <<< 带有涟漪特效动画的散点图 >>>

    利用动画特效可以将某些想要突出的数据进行视觉突出。
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=AxisOpts().opts)
        self.__xaxis_data = None

    def add_xaxis(self, xaxis_data: ListTuple):
        self.options.update(xAxis=AxisOpts().opts)
        self.options["xAxis"].update(data=xaxis_data)
        self.__xaxis_data = xaxis_data
        return self

    def add_yaxis(
        self,
        name: str,
        y_axis: ListTuple,
        symbol_size: Numeric = 10,
        symbol: Optional[str] = None,
        label_opts: LabelOpts = LabelOpts,
        effect_opts: EffectOpts = EffectOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(effect_opts, EffectOpts):
            effect_opts = effect_opts.opts

        # xaxis, yaxis = chart["xy_axis"]
        # show split line, because by default split line is hidden for xaxis
        # xaxis[0]["splitLine"]["show"] = True
        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "effectScatter",
                "name": name,
                "showEffectOn": "render",
                "rippleEffect": effect_opts,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "data": [list(z) for z in zip(self.__xaxis_data, y_axis)],
                "label": label_opts,
            }
        )
