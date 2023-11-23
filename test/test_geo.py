from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts.globals import ChartType, SymbolType


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_base(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


def test_geo_add_coord_json():
    c = (
        Geo()
        .add_schema(maptype="china")
        .add_coordinate_json(json_file="test/fixtures/city_coordinates.json")
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    assert_equal(c.theme, "white")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_custom(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "geo",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_=ChartType.CUSTOM,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Geo-EffectScatter"))
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_effectscatter(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "geo",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_=ChartType.EFFECT_SCATTER,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Geo-EffectScatter"))
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_heatmap(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "geo",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-HeatMap"),
        )
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_lines(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "",
            [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
            type_=ChartType.EFFECT_SCATTER,
            color="white",
        )
        .add(
            "geo",
            [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=6, color="blue"
            ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Lines"))
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_extra_geo_parameters(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china", center=[39, 117.7], zoom=9)
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
    c.render()
    _, content = fake_writer.call_args[0]
    center_string = """
        "center": [
            39,
            117.7
        ],
    """
    assert_in(center_string, content)
    assert_in('"zoom": 9', content)


def _geo_chart() -> Geo:
    return (
        Geo()
        .add_schema(maptype="china", center=[39, 117.7], zoom=9)
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )


def test_geo_dump_options():
    c = _geo_chart()
    formatter = """"formatter": function (params) {        return params.name + ' : ' + params.value[2];    }"""  # noqa
    assert_in(formatter, c.dump_options())


def test_geo_dump_options_with_quotes():
    c = _geo_chart()
    formatter = """"formatter": "function (params) {        return params.name + ' : ' + params.value[2];    }"""  # noqa
    assert_in(formatter, c.dump_options_with_quotes())


def test_geo_add_geo_json():
    geo_json = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "coordinates": [
                        [
                            [118.57812, 26.557402],
                            [118.590394, 26.553081],
                            [118.617087, 26.553059],
                            [118.616111, 26.527755],
                            [118.604148, 26.504904],
                            [118.608376, 26.497294],
                            [118.59623, 26.478385],
                            [118.578807, 26.473754],
                            [118.56458, 26.465373],
                            [118.554474, 26.445927],
                            [118.566533, 26.432851],
                            [118.54632, 26.417928],
                            [118.548079, 26.396854],
                            [118.560868, 26.378456],
                            [118.566104, 26.358824],
                            [118.589836, 26.373463],
                            [118.590222, 26.359802],
                            [118.595801, 26.347859],
                            [118.60369, 26.350515],
                            [118.621191, 26.361783],
                            [118.631475, 26.354788],
                            [118.656162, 26.340797],
                            [118.662964, 26.322656],
                            [118.653222, 26.313452],
                            [118.661204, 26.296272],
                            [118.664809, 26.270524],
                            [118.678076, 26.279442],
                            [118.68585, 26.28836],
                            [118.697277, 26.287725],
                            [118.693599, 26.305557],
                            [118.699533, 26.311078],
                            [118.724644, 26.337465],
                            [118.75152, 26.330542],
                            [118.76682, 26.327157],
                            [118.775794, 26.325234],
                            [118.797129, 26.340542],
                            [118.800059, 26.357136],
                            [118.785137, 26.365115],
                            [118.771085, 26.385377],
                            [118.750534, 26.390836],
                            [118.761617, 26.420202],
                            [118.745161, 26.427236],
                            [118.732826, 26.437957],
                            [118.734248, 26.45448],
                            [118.737767, 26.472405],
                            [118.748152, 26.481723],
                            [118.754353, 26.487893],
                            [118.748195, 26.494063],
                            [118.748238, 26.506403],
                            [118.762057, 26.508959],
                            [118.780881, 26.504741],
                            [118.784598, 26.491919],
                            [118.798615, 26.484013],
                            [118.805766, 26.474876],
                            [118.794544, 26.459227],
                            [118.809178, 26.445137],
                            [118.805487, 26.430479],
                            [118.822825, 26.420838],
                            [118.85278, 26.438461],
                            [118.878615, 26.469605],
                            [118.898227, 26.473649],
                            [118.91784, 26.472777],
                            [118.949511, 26.464885],
                            [118.951619, 26.487056],
                            [118.943747, 26.493838],
                            [118.942741, 26.507994],
                            [118.962064, 26.530816],
                            [118.997866, 26.528448],
                            [119.000968, 26.556946],
                            [119.009563, 26.560258],
                            [119.015767, 26.581621],
                            [119.032957, 26.594999],
                            [119.062507, 26.602235],
                            [119.075945, 26.587083],
                            [119.06329, 26.569473],
                            [119.076433, 26.569869],
                            [119.092152, 26.562702],
                            [119.101005, 26.572732],
                            [119.103604, 26.555941],
                            [119.119788, 26.539555],
                            [119.132, 26.538732],
                            [119.144213, 26.536681],
                            [119.171383, 26.548551],
                            [119.194922, 26.568383],
                            [119.212185, 26.547589],
                            [119.218757, 26.53412],
                            [119.229448, 26.526792],
                            [119.251174, 26.53241],
                            [119.253859, 26.546561],
                            [119.272336, 26.541055],
                            [119.281139, 26.534343],
                            [119.287711, 26.577995],
                            [119.301835, 26.593391],
                            [119.329006, 26.578699],
                            [119.354338, 26.599587],
                            [119.363191, 26.603281],
                            [119.376544, 26.604515],
                            [119.381656, 26.62171],
                            [119.397376, 26.627859],
                            [119.387272, 26.641423],
                            [119.375795, 26.639028],
                            [119.358824, 26.632951],
                            [119.351467, 26.648969],
                            [119.326158, 26.676212],
                            [119.261119, 26.690807],
                            [119.241593, 26.742684],
                            [119.226535, 26.728854],
                            [119.204611, 26.727288],
                            [119.182686, 26.729403],
                            [119.167628, 26.711891],
                            [119.146452, 26.731884],
                            [119.115663, 26.73961],
                            [119.047905, 26.728693],
                            [119.045955, 26.74669],
                            [119.054992, 26.764685],
                            [119.051092, 26.776147],
                            [119.042385, 26.776575],
                            [119.033679, 26.770872],
                            [119.012146, 26.761305],
                            [118.982497, 26.773075],
                            [118.945981, 26.77013],
                            [118.926007, 26.749652],
                            [118.882686, 26.738982],
                            [118.887478, 26.757469],
                            [118.903255, 26.76737],
                            [118.923824, 26.795751],
                            [118.890803, 26.813278],
                            [118.843328, 26.798569],
                            [118.827143, 26.786924],
                            [118.795852, 26.783859],
                            [118.771428, 26.805618],
                            [118.741511, 26.818793],
                            [118.728195, 26.830895],
                            [118.722432, 26.851573],
                            [118.739746, 26.856167],
                            [118.696095, 26.869031],
                            [118.664633, 26.86214],
                            [118.63317, 26.855248],
                            [118.620069, 26.839818],
                            [118.635807, 26.832963],
                            [118.638444, 26.810674],
                            [118.625974, 26.788073],
                            [118.623117, 26.769147],
                            [118.600382, 26.7093],
                            [118.582339, 26.703842],
                            [118.569788, 26.680592],
                            [118.57902, 26.673354],
                            [118.594415, 26.673546],
                            [118.594991, 26.656748],
                            [118.587905, 26.631739],
                            [118.57812, 26.557402],
                        ]
                    ],
                    "type": "Polygon",
                },
            }
        ],
    }

    c = Geo()
    c.add_geo_json(geo_json=geo_json)
    assert_equal(c._geo_json, geo_json)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_scatter_gl(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "geo",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_=ChartType.SCATTERGL,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_lines_gl(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "geo",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_=ChartType.LINESGL,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_flow_gl(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "geo",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            type_=ChartType.FLOWGL,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_pie(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            series_name="广东省",
            data_pair=[
                ("A", 10), ("B", 20), ("C", 30), ("D", 50)
            ],
            type_=ChartType.PIE,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Geo-Pie"),
            legend_opts={}
        )
    )
    assert_equal(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_item_base(fake_writer):
    data_pair = [
        opts.GeoItem(longitude=121.97, latitude=30.88, name="公园", value=12),
    ]
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(series_name="测试数据", data_pair=data_pair)
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-基本示例"),
        )
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")
