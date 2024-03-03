from unittest.mock import patch

from nose.tools import assert_equal, assert_in, assert_not_in

from pyecharts.charts import WordCloud
from pyecharts.commons.utils import JsCode
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


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_wordcloud_base(fake_writer):
    c = WordCloud().add("", words, word_size_range=[20, 100])
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_wordcloud_shapes(fake_writer):
    c = WordCloud().add("", words, word_size_range=[20, 100], shape="cardioid")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


def test_wordcloud_error_url():
    try:
        c = WordCloud().add(
            "", words, word_size_range=[20, 100], mask_image="error images_url"
        )
        c.render()
    except WordCloudMaskImageException as err:
        assert_equal(type(err), WordCloudMaskImageException)
        assert err.__str__() != ""


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_wordcloud_mask_image(fake_writer):
    c = WordCloud().add(
        "",
        words,
        word_size_range=[20, 100],
        shape="cardioid",
        mask_image="test/fixtures/img.png",
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_equal(c.theme, "white")
    assert_equal(c.renderer, "canvas")


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_wordcloud_encode_image_to_base64_os_error(fake_writer):
    error_path = "A" * 1000
    c = WordCloud().add(
        "",
        words,
        word_size_range=[20, 100],
        shape="cardioid",
        mask_image=f"{error_path}"
    )
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in(error_path, content)
    assert_not_in("data:image/", content)
