from example.commons import Collector
from pyecharts import options as opts
from pyecharts.charts import Page, PictorialBar
from pyecharts.globals import SymbolType

C = Collector()


@C.funcs
def pictorialbar_base() -> PictorialBar:
    c = (
        PictorialBar()
        .add_xaxis(["山西", "四川", "西藏", "北京", "上海", "内蒙古", "云南", "黑龙江", "广东", "福建"])
        .add_yaxis(
            "",
            [13, 42, 67, 81, 86, 94, 166, 220, 249, 262],
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=18,
            symbol_repeat="fixed",
            symbol_offset=[0, 0],
            is_symbol_clip=True,
            symbol=SymbolType.ROUND_RECT,
        )
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全国各省份人口数量（虚假数据）"),
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )
    )

    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
