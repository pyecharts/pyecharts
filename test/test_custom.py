import unittest
from unittest.mock import patch

from pyecharts.charts import Custom
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType


class TestCustom(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_custom_base(self, fake_writer):
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
        self.assertGreater(len(content), 2000)
        self.assertIn("renderItem", content)

    def test_custom_echarts_x_with_error(self):
        c = Custom()
        try:
            c.register_echarts_x(chart_type=ChartType.LINE)
        except ValueError:
            pass

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_custom_echarts_x(self, fake_writer):
        for chart_type in [
            ChartType.VIOLIN,
            ChartType.STAGE,
            ChartType.DOUGHNUT,
            ChartType.CONTOUR,
            ChartType.BAR_RANGE,
            ChartType.LINE_RANGE,
        ]:
            c = (
                Custom()
                .register_echarts_x(chart_type=chart_type)
                .add(series_name="test", render_item=chart_type)
            )
            if chart_type != ChartType.DOUGHNUT:
                c.add_xaxis(xaxis_data=["a", "b", "c"])
            c.render()
            _, content = fake_writer.call_args[0]
            self.assertIn("renderItem", content)
            self.assertIn("xAxis", content)
