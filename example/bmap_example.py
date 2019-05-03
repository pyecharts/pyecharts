from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import BMap, Page

C = Collector()


@C.funcs
def bmap_base() -> BMap:

    c = (
        BMap()
        .add_schema(
            baidu_ak="Uf1rIjuIVVXxDwEy0iEU0tApwdoqGeGn",
            center=[120.13066322374, 30.240018034923],
        )
        .add(
            "bmap",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
