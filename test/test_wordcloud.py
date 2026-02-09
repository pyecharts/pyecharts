import unittest
from unittest.mock import patch

from pyecharts.charts import WordCloud
from pyecharts.exceptions import WordCloudMaskImageException

words = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
]


class TestWordcloudChart(unittest.TestCase):
    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_wordcloud_base(self, fake_writer):
        c = WordCloud().add("", words, word_size_range=[20, 100])
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_wordcloud_shapes(self, fake_writer):
        c = WordCloud().add("", words, word_size_range=[20, 100], shape="cardioid")
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    def test_wordcloud_error_url(self):
        try:
            c = WordCloud().add(
                "", words, word_size_range=[20, 100], mask_image="error images_url"
            )
            c.render()
        except WordCloudMaskImageException as err:
            self.assertEqual(type(err), WordCloudMaskImageException)
            assert err.__str__() != ""

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_wordcloud_mask_image(self, fake_writer):
        c = WordCloud().add(
            "",
            words,
            word_size_range=[20, 100],
            shape="cardioid",
            mask_image="test/fixtures/img.png",
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")

    @patch("pathlib.Path.is_file", side_effect=OSError("Simulated OS Error"))
    def test_encode_image_to_base64_os_error(self, mock_is_file):
        """
        测试当 Path.is_file 抛出 OSError 时，_encode_image_to_base64 返回原始参数。
        """
        # 构造一个无效路径
        invalid_path = "/invalid/path/to/image.png"

        # 创建 WordCloud 实例并调用方法
        wordcloud = WordCloud()
        result = wordcloud._encode_image_to_base64(invalid_path)

        # 验证返回值是原始路径
        self.assertEqual(result, invalid_path)

    @patch("pathlib.Path.exists", side_effect=OSError("Simulated OS Error"))
    def test_encode_image_to_base64_os_error_on_exists(self, mock_exists):
        """
        测试当 Path.exists 抛出 OSError 时，_encode_image_to_base64 返回原始参数。
        """
        # 构造一个无效路径
        invalid_path = "/another/invalid/path.jpg"

        # 创建 WordCloud 实例并调用方法
        wordcloud = WordCloud()
        result = wordcloud._encode_image_to_base64(invalid_path)

        # 验证返回值是原始路径
        self.assertEqual(result, invalid_path)
