from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot


def bar_chart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c


def render_chart_by_selenium():
    from snapshot_selenium import snapshot

    make_snapshot(snapshot, bar_chart().render(), "bar0.png")


def render_chart_by_phantomjs():
    from snapshot_phantomjs import snapshot

    make_snapshot(snapshot, bar_chart().render(), "bar1.png")


render_chart_by_phantomjs()
render_chart_by_selenium()
