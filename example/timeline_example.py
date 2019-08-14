from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Map, Page, Pie, Timeline

C = Collector()


@C.funcs
def timeline_bar() -> Timeline:
    x = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl


@C.funcs
def timeline_pie() -> Timeline:
    attr = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        pie = (
            Pie()
            .add(
                "商家A",
                [list(z) for z in zip(attr, Faker.values())],
                rosetype="radius",
                radius=["30%", "55%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(pie, "{}年".format(i))
    return tl


@C.funcs
def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2015, 2020):
        map0 = (
            Map()
            .add(
                "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Map-{}年某些数据".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=200),
            )
        )
        tl.add(map0, "{}年".format(i))
    return tl


@C.funcs
def timeline_with_multi_axis():
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl


Page().add(*[fn() for fn, _ in C.charts]).render()
