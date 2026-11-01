import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.components import Image
from pyecharts.globals import CurrentConfig, NotebookType


class TestImageComponent(unittest.TestCase):
    def setUp(self):
        self.test_src = "http://test-src.com/test.png"

    def _gen_image(self) -> Image:
        image = Image()
        image.add(src=self.test_src)
        return image

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_image_base(self, fake_writer):
        image = self._gen_image()
        image.render()
        _, content = fake_writer.call_args[0]
        self.assertIn(self.test_src, content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_image_base_v1(self, fake_writer):
        image = Image()
        image.add(src=self.test_src, style_opts={"align": "center"})
        image.set_global_opts(title_opts=opts.ComponentTitleOpts(title="Image Test"))
        image.render()
        _, content = fake_writer.call_args[0]
        self.assertIn(self.test_src, content)

    def test_image_render_notebook(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
        image = self._gen_image()
        content = image.render_notebook().__html__()
        self.assertIn(self.test_src, content)

    def test_images_render_embed(self):
        image = self._gen_image()
        s = image.render_embed()
        assert s is not None
