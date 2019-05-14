from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Funnel, Page

C = Collector()


@C.funcs
def funnel_base() -> Funnel:
    c = (
        Funnel()
        .add("商品", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))
    )
    return c


@C.funcs
def funnel_label_inside() -> Funnel:
    c = (
        Funnel()
        .add(
            "商品",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            label_opts=opts.LabelOpts(position="inside"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Label（inside)"))
    )
    return c


@C.funcs
def funnel_sort_ascending() -> Funnel:
    c = (
        Funnel()
        .add(
            "商品",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Sort（ascending）"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
