import os
from unittest.mock import patch

from nose.tools import assert_equal, raises

from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from pyecharts.render.snapshot import (
    save_as,
    save_as_png,
    save_as_text,
    decode_base64,
)


def _gen_faker_engine(content: str):
    class Engine:
        def __init__(self, content):
            self.content = content

        def make_snapshot(self, *args, **kwargs):
            return self.content

    return Engine(content)


def test_decode_base64():
    assert decode_base64(data="abcde12") == b"i\xb7\x1d{]"


def test_save_as_png():
    save_as_png(image_data=b"i\xb7\x1d{]", output_name="text_png.png")
    os.unlink("text_png.png")


def test_save_as_text():
    save_as_text(image_data="test data", output_name="test_txt.txt")
    os.unlink("test_txt.txt")


def test_save_as():
    with open("test/fixtures/img1.jpg", "rb") as f:
        image_bytes = f.read()
    save_as(image_data=image_bytes, output_name="test_pdf.pdf", file_type="pdf")
    os.unlink("test_pdf.pdf")
    save_as(image_data=image_bytes, output_name="test_gif.gif", file_type="gif")
    os.unlink("test_gif.gif")
    save_as(image_data=image_bytes, output_name="test_eps.eps", file_type="eps")
    os.unlink("test_eps.eps")


@patch("pyecharts.render.engine.write_utf8_html_file")
def _gen_bar_chart(fake_writer) -> str:
    c = (
        Bar()
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("series0", [1, 2, 4])
        .add_yaxis("series1", [2, 3, 6])
    )
    c.render()
    filename, _ = fake_writer.call_args[0]
    return filename


@raises(OSError)
def test_make_snapshot_raise_os_error():
    eng = _gen_faker_engine("fake content")
    make_snapshot(eng, _gen_bar_chart(), "make_snapshot.png")


@raises(TypeError)
def test_make_snapshot_raise_type_error():
    eng = _gen_faker_engine("fake content1,content2")
    make_snapshot(eng, _gen_bar_chart(), "make_snapshot.pngx")


@patch("pyecharts.render.snapshot.save_as_png")
def test_make_snapshot_png(fake_writer):
    eng = _gen_faker_engine("fake content1,content2")
    make_snapshot(eng, _gen_bar_chart(), "make_snapshot.png")
    _ = fake_writer.call_args[0]
    assert_equal("test ok", "test ok")


@patch("pyecharts.render.snapshot.save_as")
def test_make_snapshot_gif(fake_writer):
    eng = _gen_faker_engine("fake content1,content2")
    make_snapshot(eng, _gen_bar_chart(), "make_snapshot.gif")
    _ = fake_writer.call_args[0]
    assert_equal("test ok", "test ok")


@patch("pyecharts.render.snapshot.save_as_text")
def test_make_snapshot_text(fake_writer):
    eng = _gen_faker_engine("fake content1,content2")
    make_snapshot(eng, _gen_bar_chart(), "make_snapshot.svg")
    _ = fake_writer.call_args[0]
    assert_equal("test ok", "test ok")


@patch("pyecharts.render.snapshot.save_as_text")
def test_make_snapshot_text_v1(fake_writer):
    eng = _gen_faker_engine("fake content1,content2")
    make_snapshot(
        engine=eng,
        file_name=_gen_bar_chart(),
        output_name="make_snapshot.svg",
        is_remove_html=True,
    )
    _ = fake_writer.call_args[0]
    assert_equal("test ok", "test ok")
