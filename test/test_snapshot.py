from unittest.mock import patch

from nose.tools import assert_equal, raises

from pyecharts.charts import Bar
from pyecharts.render import make_snapshot


def _gen_faker_engine(content: str):
    class Engine:
        def __init__(self, content):
            self.content = content

        def make_snapshot(self, *args, **kwargs):
            return self.content

    return Engine(content)


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
