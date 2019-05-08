from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Map, Page

C = Collector()


@C.funcs
def map_base() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    )
    return c


@C.funcs
def map_without_label() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-不显示Label"))
    )
    return c


@C.funcs
def map_visualmap() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    return c


@C.funcs
def map_visualmap_piecewise() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
        )
    )
    return c


@C.funcs
def map_world() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.country, Faker.values())], "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-世界地图"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    return c


@C.funcs
def map_guangdong() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.guangdong_city, Faker.values())], "广东")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-广东地图"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
