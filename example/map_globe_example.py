import pyecharts.options as opts
from example.commons import POPULATION
from pyecharts.charts import MapGlobe


def map_globe_base():
    data = [x for _, x in POPULATION[1:]]
    low, high = min(data), max(data)

    mg = (
        MapGlobe()
        .add_schema()
        .add(
            maptype="world",
            series_name="World Population",
            data_pair=POPULATION[1:],
            is_map_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                min_=low,
                max_=high,
                range_text=["max", "min"],
                is_calculable=True,
                range_color=["lightskyblue", "yellow", "orangered"],
            )
        )
    )
    mg.render()
