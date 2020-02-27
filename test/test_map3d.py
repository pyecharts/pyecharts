from unittest.mock import patch

from nose.tools import assert_in

from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.faker import Faker
from pyecharts.globals import ChartType


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_map3d_base(fake_writer):
    c = (
        Map3D()
        .add_schema()
        .add(
            "商家A",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
            maptype="china",
        )
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("map3D", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_map3d_schema(fake_writer):
    c = (
        Map3D()
        .add_schema(
            itemstyle_opts=opts.ItemStyleOpts(),
            map3d_label=opts.Map3DLabelOpts(),
            light_opts=opts.Map3DLightOpts(),
            view_control_opts=opts.Map3DViewControlOpts(),
            post_effect_opts=opts.Map3DPostEffectOpts(),
            realistic_material_opts=opts.Map3DRealisticMaterialOpts(),
            lambert_material_opts=opts.Map3DLambertMaterialOpts(),
            color_material_opts=opts.Map3DColorMaterialOpts(),
        )
        .add(
            series_name="商家A",
            data_pair=[list(z) for z in zip(Faker.provinces, Faker.values())],
            maptype="china",
            type_=ChartType.LINES3D,
            effect=opts.Lines3DEffectOpts(),
        )
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("itemStyle", content)
    assert_in("label", content)
    assert_in("light", content)
    assert_in("viewControl", content)
    assert_in("postEffect", content)
    assert_in("realisticMaterial", content)
    assert_in("lambertMaterial", content)
    assert_in("colorMaterial", content)
