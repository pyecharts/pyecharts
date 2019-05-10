import json
import os

from example.commons import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import BMap, Page
from pyecharts.globals import BMapType

C = Collector()
BAIDU_MAP_AK = os.environ.get("BAIDU_MAP_AK", "FAKE_AK")


@C.funcs
def bmap_base() -> BMap:

    c = (
        BMap()
        .add_schema(baidu_ak=BAIDU_MAP_AK, center=[120.13066322374, 30.240018034923])
        .add(
            "bmap",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"))
    )
    return c


@C.funcs
def bmap_lines() -> BMap:
    with open(
        os.path.join("fixtures", "hangzhou-tracks.json"), "r", encoding="utf-8"
    ) as f:
        j = json.load(f)
    c = (
        BMap()
        .add_schema(
            baidu_ak=BAIDU_MAP_AK,
            center=[120.13066322374, 30.240018034923],
            zoom=14,
            is_roam=True,
            map_style={
                "styleJson": [
                    {
                        "featureType": "water",
                        "elementType": "all",
                        "stylers": {"color": "#d1d1d1"},
                    },
                    {
                        "featureType": "land",
                        "elementType": "all",
                        "stylers": {"color": "#f3f3f3"},
                    },
                    {
                        "featureType": "railway",
                        "elementType": "all",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "highway",
                        "elementType": "all",
                        "stylers": {"color": "#fdfdfd"},
                    },
                    {
                        "featureType": "highway",
                        "elementType": "labels",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "geometry",
                        "stylers": {"color": "#fefefe"},
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "geometry.fill",
                        "stylers": {"color": "#fefefe"},
                    },
                    {
                        "featureType": "poi",
                        "elementType": "all",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "green",
                        "elementType": "all",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "subway",
                        "elementType": "all",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "manmade",
                        "elementType": "all",
                        "stylers": {"color": "#d1d1d1"},
                    },
                    {
                        "featureType": "local",
                        "elementType": "all",
                        "stylers": {"color": "#d1d1d1"},
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "labels",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "boundary",
                        "elementType": "all",
                        "stylers": {"color": "#fefefe"},
                    },
                    {
                        "featureType": "building",
                        "elementType": "all",
                        "stylers": {"color": "#d1d1d1"},
                    },
                    {
                        "featureType": "label",
                        "elementType": "labels.text.fill",
                        "stylers": {"color": "#999999"},
                    },
                ]
            },
        )
        .add(
            "",
            type_="lines",
            data_pair=j,
            is_polyline=True,
            is_large=True,
            linestyle_opts=opts.LineStyleOpts(color="purple", opacity=0.6, width=1),
        )
        .add_control_panel(
            maptype_control_opts=opts.BMapTypeControl(
                type_=BMapType.MAPTYPE_CONTROL_DROPDOWN
            ),
            scale_control_opts=opts.BMapScaleControlOpts(),
            overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-杭州热门步行路线"))
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
