from unittest.mock import patch

from nose.tools import assert_greater, assert_in


from pyecharts.charts import Custom
from pyecharts.commons.utils import JsCode


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_custom_base(fake_writer):
    c = Custom().add(
        series_name="",
        render_item=JsCode(
            """
            function (params, api) {
                var categoryIndex = api.value(0);
                var start = api.coord([api.value(1), categoryIndex]);
                var end = api.coord([api.value(2), categoryIndex]);
                var height = api.size([0, 1])[1] * 0.6;
                var rectShape = echarts.graphic.clipRectByRect({
                    x: start[0],
                    y: start[1] - height / 2,
                    width: end[0] - start[0],
                    height: height
                }, {
                    x: params.coordSys.x,
                    y: params.coordSys.y,
                    width: params.coordSys.width,
                    height: params.coordSys.height
                });
                return rectShape && {
                    type: 'rect',
                    shape: rectShape,
                    style: api.style()
                };
            }
            """
        ),
        data=None,
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_greater(len(content), 2000)
    assert_in("renderItem", content)
