from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import EffectScatter, Page
from pyecharts.globals import SymbolType

C = Collector()


@C.funcs
def effectscatter_base() -> EffectScatter:
    c = (
        EffectScatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
    )
    return c


@C.funcs
def effectscatter_splitline() -> EffectScatter:
    c = (
        EffectScatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="EffectScatter-显示分割线"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        )
    )
    return c


@C.funcs
def effectscatter_symbol() -> EffectScatter:
    c = (
        EffectScatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("", Faker.values(), symbol=SymbolType.ARROW)
    ).set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-不同Symbol"))
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
