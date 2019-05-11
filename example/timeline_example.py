from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Map, Page, Pie, Timeline

C = Collector()


@C.funcs
def timeline_bar() -> Timeline:
    x = Faker.choose()
    bar0 = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("某商店2015年营业额"))
    )
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
        .add(bar0, "2015年")
        .add(bar1, "2016年")
        .add(bar2, "2017年")
        .add(bar3, "2018年")
        .add(bar4, "2019年")
    )
    return tl


@C.funcs
def timeline_pie() -> Timeline:
    attr = Faker.choose()
    pie0 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("某商店2015年营业额"))
    )
    pie1 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("某商店2016年营业额"))
    )
    pie2 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("某商店2017年营业额"))
    )
    pie3 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("某商店2018年营业额"))
    )
    pie4 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("某商店2019年营业额"))
    )
    tl = (
        Timeline()
        .add(pie0, "2015年")
        .add(pie1, "2016年")
        .add(pie2, "2017年")
        .add(pie3, "2018年")
        .add(pie4, "2019年")
    )
    return tl


@C.funcs
def timeline_map() -> Timeline:
    map0 = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-2015年某些数据"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    map1 = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-2016年某些数据"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    map2 = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-2017年某些数据"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    map3 = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-2018年某些数据"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    map4 = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-2019年某些数据"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    tl = (
        Timeline()
        .add(map0, "2015年")
        .add(map1, "2016年")
        .add(map2, "2017年")
        .add(map3, "2018年")
        .add(map4, "2019年")
    )
    return tl


Page().add(*[fn() for fn, _ in C.charts]).render()
