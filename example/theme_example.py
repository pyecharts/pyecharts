from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page
from pyecharts.globals import ThemeType

C = Collector()


@C.funcs
def theme_default() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-default"))
    )
    return c


@C.funcs
def theme_light() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-light"))
    )
    return c


@C.funcs
def theme_dark() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-dark"))
    )
    return c


@C.funcs
def theme_chalk() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-chalk"))
    )
    return c


@C.funcs
def theme_essos() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-essos"))
    )
    return c


@C.funcs
def theme_infographic() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-infographic"))
    )
    return c


@C.funcs
def theme_macarons() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-macarons"))
    )
    return c


@C.funcs
def theme_purple_passion() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-purple-passion"))
    )
    return c


@C.funcs
def theme_roma() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-roma"))
    )
    return c


@C.funcs
def theme_romantic() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-romantic"))
    )
    return c


@C.funcs
def theme_shine() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-shine"))
    )
    return c


@C.funcs
def theme_vintage() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-vintage"))
    )
    return c


@C.funcs
def theme_walden() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-walden"))
    )
    return c


@C.funcs
def theme_westeros() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-westeros"))
    )
    return c


@C.funcs
def theme_wonderland() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .add_yaxis("商家C", Faker.values())
        .add_yaxis("商家D", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("Theme-wonderland"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
