import pyecharts.options as opts
from pyecharts.charts import Bar, Page
from pyecharts.example.commons import CLOTHES, gen_random_data
from pyecharts.render import make_snapshot


def bar_base() -> Bar:
    bar = Bar()
    bar.add_xaxis(CLOTHES).add_yaxis(
        "series0", gen_random_data(len(CLOTHES))
    ).add_yaxis("series1", gen_random_data(len(CLOTHES)))
    return bar


def bar_title() -> Bar:
    bar = bar_base()
    bar.set_global_opts(title_opts=opts.TitleOpts(title="我是主标题", subtitle="我是副标题"))
    return bar


page = Page()
page.add(bar_base(), bar_title())
page.render()
