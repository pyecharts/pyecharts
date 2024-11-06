import unittest
from datetime import datetime
from unittest.mock import patch

from pyecharts.charts import Bar
from pyecharts.options import InitOpts, RenderOpts
from pyecharts.globals import CurrentConfig
from pyecharts.charts.base import Base, default
from pyecharts.options.series_options import AnimationOpts


class TestBaseClass(unittest.TestCase):

    def test_base_add_functions(self):
        c = Base()
        c.add_js_funcs("console.log('hello')", "console.log('hello')")
        self.assertEqual(1, len(c.js_functions.items))
        self.assertEqual(["console.log('hello')"], c.js_functions.items)

    def test_base_add_events(self):
        c = Base()
        c.add_js_events("console.log('hello')", "console.log('hello')")
        self.assertEqual(1, len(c.js_events.items))
        self.assertEqual(["console.log('hello')"], c.js_events.items)

    def test_base_init_funcs(self):
        c0 = Base({"width": "100px", "height": "200px"})
        self.assertEqual(c0.width, "100px")
        self.assertEqual(c0.height, "200px")

        c1 = Base(dict(width="110px", height="210px"))
        self.assertEqual(c1.width, "110px")
        self.assertEqual(c1.height, "210px")
        self.assertNotIn(c1.js_host, ["", None])

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_render(self, fake_writer):
        my_render_content = "my_render_content"
        bar = Bar()
        bar.add_xaxis(["1"]).add_yaxis("", [1]).render(
            my_render_content=my_render_content
        )
        assert "test ok" == "test ok"

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_render_js_host_none(self, fake_writer):
        my_render_content = "my_render_content"
        bar = Bar()
        bar.add_xaxis(["1"]).add_yaxis("", [1])
        # Hack to test
        bar.js_host = None
        # Render
        bar.render(my_render_content=my_render_content)
        self.assertEqual(bar.js_host, CurrentConfig.ONLINE_HOST)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_render_embed_js(self, _):
        c = Base(render_opts=RenderOpts(is_embed_js=True))
        # Embedded JavaScript
        content = c.render_embed()
        self.assertNotIn(
            CurrentConfig.ONLINE_HOST, content, "Embedding JavaScript fails"
        )
        # No embedded JavaScript
        c.render_options.update(embed_js=False)
        content = c.render_embed()
        self.assertIn(
            CurrentConfig.ONLINE_HOST, content, "Embedded JavaScript cannot be closed"
        )

    def test_base_render_options(self):
        c0 = Base(render_opts=RenderOpts(is_embed_js=True))
        self.assertEqual(c0.render_options.get("embed_js"), True)

    def test_base_iso_format(self):
        mock_time_str = "2022-04-14 14:42:00"
        mock_time = datetime.strptime(mock_time_str, "%Y-%m-%d %H:%M:%S")
        assert default(mock_time) == "2022-04-14T14:42:00"

    def test_base_animation_option(self):
        c0 = Base(init_opts=InitOpts(animation_opts=AnimationOpts(animation=False)))
        self.assertEqual(c0.options.get("animation"), False)

        c1 = Base({"animationOpts": {"animation": False}})
        self.assertEqual(c1.options.get("animation"), False)

    def test_base_chart_id(self):
        c0 = Base(init_opts=InitOpts(chart_id="1234567"))
        self.assertEqual(c0.chart_id, "1234567")

        c1 = Base(init_opts=InitOpts(chart_id="1234567"))
        self.assertEqual(c1.get_chart_id(), "1234567")

    def test_use_echarts_stat(self):
        c0 = Base().use_echarts_stat()
        self.assertEqual(c0.js_dependencies.items, ["echarts", "echarts-stat"])
