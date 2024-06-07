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

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_wordcloud_encode_image_to_base64_os_error(self, fake_writer):
        error_path = "A" * 1000
        c = WordCloud().add(
            "",
            words,
            word_size_range=[20, 100],
            shape="cardioid",
            mask_image=f"{error_path}",
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn(error_path, content)
        self.assertNotIn("data:image/", content)
