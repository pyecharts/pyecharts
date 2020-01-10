import json
import os

from pyecharts import options as opts
from pyecharts.charts import BMap, Page
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector, Faker
from pyecharts.globals import BMapType, ChartType

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
def bmap_heatmap() -> BMap:
    c = (
        BMap()
        .add_schema(baidu_ak=BAIDU_MAP_AK, center=[120.13066322374, 30.240018034923])
        .add(
            "bmap",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_="heatmap",
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="BMap-热力图"),
            visualmap_opts=opts.VisualMapOpts(),
        )
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
            maptype_control_opts=opts.BMapTypeControlOpts(
                type_=BMapType.MAPTYPE_CONTROL_DROPDOWN
            ),
            scale_control_opts=opts.BMapScaleControlOpts(),
            overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-杭州热门步行路线"))
    )
    return c


@C.funcs
def bmap_custom() -> BMap:
    with open(
        os.path.join("fixtures", "bmap-custom-data.json"), "r", encoding="utf-8"
    ) as f:
        j = json.load(f)
    color_list = ["#070093", "#1c3fbf", "#1482e5", "#70b4eb", "#b4e0f3", "#ffffff"]
    c = (
        BMap()
        .add_schema(
            baidu_ak=BAIDU_MAP_AK,
            center=[116.46, 39.92],
            zoom=11.8,
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
                        "stylers": {"color": "#999999"},
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
                        "stylers": {"color": "rgba(0,0,0,0)"},
                    },
                ]
            },
        )
        .add_js_funcs(
            """
        var lngExtent = [39.5, 40.6];
        var latExtent = [115.9, 116.8];
        var cellCount = [50, 50];
        var cellSizeCoord = [
            (lngExtent[1] - lngExtent[0]) / cellCount[0],
            (latExtent[1] - latExtent[0]) / cellCount[1]
        ];
        var gapSize = 0;

        function renderItem(params, api) {
            var lngIndex = api.value(0);
            var latIndex = api.value(1);
            var pointLeftTop = getCoord(params, api, lngIndex, latIndex);
            var pointRightBottom = getCoord(params, api, lngIndex + 1, latIndex + 1);

            return {
                type: 'rect',
                shape: {
                    x: pointLeftTop[0],
                    y: pointLeftTop[1],
                    width: pointRightBottom[0] - pointLeftTop[0],
                    height: pointRightBottom[1] - pointLeftTop[1]
                },
                style: api.style({
                    stroke: 'rgba(0,0,0,0.1)'
                }),
                styleEmphasis: api.styleEmphasis()
            };
        }

        function getCoord(params, api, lngIndex, latIndex) {
            var coords = params.context.coords || (params.context.coords = []);
            var key = lngIndex + '-' + latIndex;
            return coords[key] || (coords[key] = api.coord([
                +(latExtent[0] + lngIndex * cellSizeCoord[0]).toFixed(6),
                +(lngExtent[0] + latIndex * cellSizeCoord[1]).toFixed(6)
            ]));
        }
        """
        )
        .add(
            series_name="",
            data_pair=j["data"],
            type_=ChartType.CUSTOM,
            render_item=JsCode("renderItem"),
            itemstyle_opts=opts.ItemStyleOpts(color="yellow"),
            encode={"tooltip": 2},
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="BMap-Custom 图"),
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter=None),
            visualmap_opts=opts.VisualMapOpts(
                is_piecewise=True,
                pos_top="10",
                pos_left="10",
                is_inverse=True,
                pieces=[
                    {"value": i, "color": color_list[i]} for i in range(len(color_list))
                ],
                dimension=2,
                border_color="#ccc",
                border_width=2,
                background_color="#eee",
                range_opacity=0.7,
            ),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=110,
                        bottom=110,
                        z=100,
                    ),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_shape_opts=opts.GraphicShapeOpts(
                                width=400, height=50
                            ),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="rgba(0,0,0,0.3)"
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text="Made by pyecharts",
                                font="bold 26px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="#fff"
                                ),
                            ),
                        ),
                    ],
                )
            ],
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
