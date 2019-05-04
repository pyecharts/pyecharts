from unittest.mock import patch
from pyecharts import options as opts
from pyecharts.charts import BMap

BAIDU_MAP_API_PREFIX = 'http://api.map.baidu.com/api?v=2.0'


@patch('pyecharts.render.engine.write_utf8_html_file')
def test_baidu_map(fake_writer):
    fake_api_key = "fake_application_key"
    provinces = ["London"]
    values = [1]
    bmap = (
        BMap()
        .add_schema(
            baidu_ak=fake_api_key,
            center=[-0.118092, 51.509865],
        ).add_coordinate('London', -0.118092, 51.509865)
        .add(
            "bmap",
            [list(z) for z in zip(provinces, values)],
            label_opts=opts.LabelOpts(formatter="{b}"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="BMap-基本示例"))
    )
    bmap.render('render.html')
    content = fake_writer.call_args[0][1]
    expected_baidu_key = f'src="{BAIDU_MAP_API_PREFIX}&ak={fake_api_key}"'
    expected_map_type = '"coordinateSystem": "bmap"'
    assert expected_baidu_key in content, "missing baidu api key"
    assert expected_map_type in content, "non bmap found"
