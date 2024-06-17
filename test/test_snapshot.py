import os
import unittest
from io import BytesIO
from unittest.mock import patch

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


class TestSnapshotComponent(unittest.TestCase):
    def test_decode_base64(self):
        assert decode_base64(data="abcde12") == b"i\xb7\x1d{]"

    def test_save_as_png(self):
        save_as_png(image_data=b"i\xb7\x1d{]", output_name="text_png.png")
        os.unlink("text_png.png")

    def test_save_as_text(self):
        save_as_text(image_data="test data", output_name="test_txt.txt")
        os.unlink("test_txt.txt")

    def test_save_as(self):
        with open("test/fixtures/img1.jpg", "rb") as f:
            image_bytes = f.read()
        save_as(image_data=image_bytes, output_name="test_pdf.pdf", file_type="pdf")
        os.unlink("test_pdf.pdf")
        save_as(image_data=image_bytes, output_name="test_gif.gif", file_type="gif")
        os.unlink("test_gif.gif")
        save_as(image_data=image_bytes, output_name="test_eps.eps", file_type="eps")
        os.unlink("test_eps.eps")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def _gen_bar_chart(self, fake_writer) -> str:
        c = (
            Bar()
            .add_xaxis(["A", "B", "C"])
            .add_yaxis("series0", [1, 2, 4])
            .add_yaxis("series1", [2, 3, 6])
        )
        c.render()
        filename, _ = fake_writer.call_args[0]
        return filename

    def test_make_snapshot_raise_os_error(self):
        with self.assertRaises(OSError):
            eng = _gen_faker_engine("fake content")
            make_snapshot(eng, self._gen_bar_chart(), "make_snapshot.png")

    def test_make_snapshot_raise_type_error(self):
        with self.assertRaises(TypeError):
            eng = _gen_faker_engine("fake content1,content2")
            make_snapshot(eng, self._gen_bar_chart(), "make_snapshot.pngx")

    @patch("pyecharts.render.snapshot.save_as_png")
    def test_make_snapshot_png(self, fake_writer):
        eng = _gen_faker_engine("fake content1,content2")
        make_snapshot(eng, self._gen_bar_chart(), "make_snapshot.png")
        _ = fake_writer.call_args[0]
        self.assertEqual("test ok", "test ok")

    @patch("pyecharts.render.snapshot.save_as")
    def test_make_snapshot_gif(self, fake_writer):
        eng = _gen_faker_engine("fake content1,content2")
        make_snapshot(eng, self._gen_bar_chart(), "make_snapshot.gif")
        _ = fake_writer.call_args[0]
        self.assertEqual("test ok", "test ok")

    @patch("pyecharts.render.snapshot.save_as_text")
    def test_make_snapshot_text(self, fake_writer):
        eng = _gen_faker_engine("fake content1,content2")
        make_snapshot(eng, self._gen_bar_chart(), "make_snapshot.svg")
        _ = fake_writer.call_args[0]
        self.assertEqual("test ok", "test ok")

    @patch("pyecharts.render.snapshot.save_as_text")
    def test_make_snapshot_text_v1(self, fake_writer):
        eng = _gen_faker_engine("fake content1,content2")
        make_snapshot(
            engine=eng,
            file_name=self._gen_bar_chart(),
            output_name="make_snapshot.svg",
            is_remove_html=True,
        )
        _ = fake_writer.call_args[0]
        self.assertEqual("test ok", "test ok")


class TestSaveAs(unittest.TestCase):
    @patch("builtins.__import__", side_effect=ModuleNotFoundError)
    def test_save_as_module_not_found(self, mock_import):
        image_data = b"fake_image_data"
        output_name = "output.jpg"
        file_type = "JPEG"

        with self.assertRaises(Exception) as context:
            save_as(image_data, output_name, file_type)
            # 检查异常消息是否包含期望的提示信息
            self.assertTrue(
                f"Please install PIL for {file_type} image type." in
                str(context.exception),
            )
