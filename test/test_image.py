from unittest.mock import patch

from nose.tools import assert_in

from pyecharts import options as opts
from pyecharts.components import Image
from pyecharts.globals import CurrentConfig, NotebookType

TEST_SRC = "http://test-src.com/test.png"


def _gen_image() -> Image:
    image = Image()
    image.add(src=TEST_SRC)
    return image


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_image_base(fake_writer):
    image = _gen_image()
    image.render()
    _, content = fake_writer.call_args[0]
    assert_in(TEST_SRC, content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_image_base_v1(fake_writer):
    image = Image()
    image.add(src=TEST_SRC, style_opts={"align": "center"})
    image.set_global_opts(title_opts=opts.ComponentTitleOpts(title="Image Test"))
    image.render()
    _, content = fake_writer.call_args[0]
    assert_in(TEST_SRC, content)


def test_image_render_notebook():
    CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
    image = _gen_image()
    content = image.render_notebook().__html__()
    assert_in(TEST_SRC, content)


def test_images_render_embed():
    image = _gen_image()
    s = image.render_embed()
    assert s is not None
