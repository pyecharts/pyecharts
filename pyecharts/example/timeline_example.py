# coding=utf-8
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline, Page
from pyecharts.example.commons import Faker

charts = []


def collect_charts(fn):
    charts.append((fn, fn.__name__))
    return fn


@collect_charts
def timeline_base() -> Timeline:
    x = Faker.choose()
    bar1 = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("某商店2016年营业额"))
    )
    bar2 = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("某商店2017年营业额"))
    )
    bar3 = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("某商店2018年营业额"))
    )
    bar4 = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("某商店2019年营业额"))
    )

    tl = (
        Timeline()
        .add(bar1, "2016年")
        .add(bar2, "2017年")
        .add(bar3, "2018年")
        .add(bar4, "2019年")
    )
    return tl


Page().add(*[fn() for fn, _ in charts]).render()
